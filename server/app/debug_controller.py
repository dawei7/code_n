"""Minimal DAP (Debug Adapter Protocol) client for talking to
the debugpy subprocess.

We implement just the subset of DAP needed for the Debug tab:
play / step over / step in / step out / pause at breakpoints,
inspect locals, and clean shutdown. DAP messages are JSON,
framed with HTTP-style ``Content-Length`` headers. See
https://microsoft.github.io/debug-adapter-protocol/ for the
full spec; we only touch the read paths the user actually
exercises.

The client wraps a TCP socket and exposes a small async API:
``set_breakpoints``, ``continue_execution``, ``step_over``,
``step_in``, ``step_out``, ``get_locals``, ``stop``. A separate
async task reads events off the socket and pushes them onto
an ``asyncio.Queue`` that the WebSocket handler can drain.

We deliberately keep this client small and synchronous-style
(``asyncio`` only for the socket I/O) — a 4-5 method
state machine, no global state.
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
import shlex
import signal
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Awaitable, Callable, Optional


log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Low-level DAP framing
# ---------------------------------------------------------------------------


class DapProtocolError(RuntimeError):
    """Raised when the DAP stream is malformed or the adapter
    reports an error response."""


def _encode_message(message: dict) -> bytes:
    """Serialize a DAP request/response/event to the wire format.

    DAP messages are JSON, framed with a Content-Length header
    (HTTP-style). One blank line separates the headers from the
    body.
    """
    body = json.dumps(message).encode("utf-8")
    header = f"Content-Length: {len(body)}\r\n\r\n".encode("ascii")
    return header + body


def _read_message(stream: asyncio.StreamReader) -> Optional[dict]:
    """Read one DAP message from the stream, or return None on EOF.

    Blocks until a full message is read.
    """
    # Read headers (until blank line)
    headers: dict[str, str] = {}
    while True:
        line = stream.readline()
        if not line:
            return None
        if line in (b"\r\n", b"\n", b""):
            break
        try:
            key, value = line.decode("ascii").split(":", 1)
            headers[key.strip().lower()] = value.strip()
        except ValueError:
            raise DapProtocolError(f"malformed DAP header line: {line!r}")
    length = int(headers.get("content-length", "0"))
    if length == 0:
        return {}
    body = stream.readexactly(length)
    return json.loads(body.decode("utf-8"))


# ---------------------------------------------------------------------------
# DAP client: one TCP connection, two coroutines
# ---------------------------------------------------------------------------


class DapClient:
    """Async DAP client wrapping a TCP socket to debugpy.

    Use one instance per debug session. Spawn the subprocess
    externally, then construct with the host + port debugpy
    is listening on.

    Usage::

        client = DapClient("127.0.0.1", port)
        await client.connect()
        await client.initialize()
        await client.launch(...)
        event = await client.wait_for_event("stopped")
        locals_ = await client.get_locals(...)
        await client.disconnect()
    """

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self._reader: Optional[asyncio.StreamReader] = None
        self._writer: Optional[asyncio.StreamWriter] = None
        self._next_seq = 1
        self._pending: dict[int, asyncio.Future] = {}
        self._event_queue: asyncio.Queue[dict] = asyncio.Queue()

    # --- connection lifecycle ---------------------------------------

    async def connect(self) -> None:
        self._reader, self._writer = await asyncio.open_connection(self.host, self.port)
        # Reader task: read messages, dispatch to pending or
        # event queue.
        asyncio.create_task(self._read_loop())

    async def close(self) -> None:
        if self._writer is not None:
            try:
                self._writer.close()
                await self._writer.wait_closed()
            except Exception:
                pass
        # Cancel any pending requests so callers don't hang.
        for fut in self._pending.values():
            if not fut.done():
                fut.set_exception(DapProtocolError("client closed"))

    # --- low-level send / receive ------------------------------------

    def _next_id(self) -> int:
        i = self._next_seq
        self._next_seq += 1
        return i

    async def _send(self, command: str, arguments: Optional[dict] = None) -> dict:
        if self._writer is None:
            raise DapProtocolError("not connected")
        msg_id = self._next_id()
        fut: asyncio.Future = asyncio.get_event_loop().create_future()
        self._pending[msg_id] = fut
        await self._send_raw({
            "seq": msg_id,
            "type": "request",
            "command": command,
            "arguments": arguments or {},
        })
        return await fut

    async def _send_raw(self, message: dict) -> None:
        assert self._writer is not None
        self._writer.write(_encode_message(message))
        await self._writer.drain()

    async def _read_loop(self) -> None:
        """Background task: read DAP messages forever, dispatch
        to the pending-request future or the event queue."""
        assert self._reader is not None
        while True:
            try:
                msg = await self._read_one_async()
            except (asyncio.IncompleteReadError, ConnectionError):
                # Adapter closed the socket. Wake up any
                # pending requests with an error.
                for fut in self._pending.values():
                    if not fut.done():
                        fut.set_exception(DapProtocolError("adapter disconnected"))
                self._pending.clear()
                return
            if msg is None:
                # EOF
                return
            if msg.get("type") == "response":
                msg_id = msg.get("request_seq")
                fut = self._pending.pop(msg_id, None) if msg_id is not None else None
                if fut is not None and not fut.done():
                    if not msg.get("success", True):
                        fut.set_exception(
                            DapProtocolError(
                                f"DAP {msg.get('command', '?')} failed: "
                                f"{msg.get('message', '')} "
                                f"body={msg.get('body', '')!r}"
                            )
                        )
                    else:
                        fut.set_result(msg)
            elif msg.get("type") == "event":
                # The client doesn't care about most events;
                # the WebSocket handler drains them off the
                # event queue.
                await self._event_queue.put(msg)

    async def _read_one_async(self) -> Optional[dict]:
        """Read one DAP message from the (async) stream reader.

        DAP messages are JSON, framed with HTTP-style
        Content-Length headers. We use the async stream
        methods directly rather than going through an
        executor (asyncio.StreamReader doesn't have a sync
        readline).
        """
        assert self._reader is not None
        # Read headers (until blank line)
        headers: dict[str, str] = {}
        while True:
            line = await self._reader.readline()
            if not line:
                return None
            if line in (b"\r\n", b"\n"):
                break
            try:
                key, value = line.decode("ascii").split(":", 1)
                headers[key.strip().lower()] = value.strip()
            except ValueError:
                raise DapProtocolError(f"malformed DAP header line: {line!r}")
        length = int(headers.get("content-length", "0"))
        if length == 0:
            return {}
        body = await self._reader.readexactly(length)
        return json.loads(body.decode("utf-8"))

    async def wait_for_event(self, name: str, timeout: float = 30.0) -> Optional[dict]:
        """Block until an event of the given name arrives, or
        return None on timeout. Drains non-matching events from
        the queue so they don't pile up."""
        deadline = asyncio.get_event_loop().time() + timeout
        while True:
            remaining = deadline - asyncio.get_event_loop().time()
            if remaining <= 0:
                return None
            try:
                event = await asyncio.wait_for(self._event_queue.get(), timeout=remaining)
            except asyncio.TimeoutError:
                return None
            if event.get("event") == name:
                return event
            # Drop the event; we only care about `name`.

    # --- DAP requests -------------------------------------------------

    async def initialize(self) -> None:
        await self._send("initialize", {
            "clientID": "coden-debug",
            "clientName": "cOde(n) Debug Tab",
            "adapterID": "debugpy",
            "locale": "en-US",
            "linesStartAt1": True,
            "columnsStartAt1": True,
            "pathFormat": "path",
            "supportsVariableType": True,
            "supportsVariablePaging": False,
        })
        # debugpy sends an "initialized" event after init; the
        # caller (DebugController) waits for that.

    async def launch(self, source_path: str, breakpoints: list[int]) -> None:
        """Send the appropriate DAP request for our mode.

        We use ``launch`` for the normal case (debugpy
        loads a fresh script). For the in-process mode
        that the worker uses (where ``debugpy.listen``
        is called from the same Python process that
        runs the user code), we use ``attach`` —
        debugpy rejects ``launch`` in that mode with
        '"attach" expected'.
        """
        # Default: launch.
        await self._send("launch", {
            "program": source_path,
            "args": [],
            "cwd": str(_repo_root()),
            "env": {
                "CODEN_BREAKPOINTS": ",".join(str(b) for b in breakpoints),
                "PATH": os.environ.get("PATH", ""),
            },
            "stopOnEntry": False,
            "noDebug": False,
        })

    async def attach_in_process(self) -> None:
        """The in-process attach: no program, no process ID,
        just "you are now a debug client for this Python
        process". Breakpoints are set separately via
        setBreakpoints."""
        # debugpy's AttachRequest requires a non-empty
        # arguments body. Send an empty dict — the DAP
        # spec is permissive about extra fields.
        await self._send("attach", {"__in_process__": True})

    async def configurationDone(self) -> None:
        await self._send("configurationDone", {})

    async def setBreakpoints(self, path: str, lines: list[int]) -> None:
        await self._send("setBreakpoints", {
            "source": {"path": path, "name": os.path.basename(path)},
            "lines": sorted(set(lines)),
            "sourceModified": False,
        })

    async def continue_execution(self, thread_id: int) -> None:
        await self._send("continue", {"threadId": thread_id})

    async def next(self, thread_id: int) -> None:
        await self._send("next", {"threadId": thread_id, "granularity": "line"})

    async def step_in(self, thread_id: int) -> None:
        await self._send("stepIn", {"threadId": thread_id, "granularity": "line"})

    async def step_out(self, thread_id: int) -> None:
        await self._send("stepOut", {"threadId": thread_id, "granularity": "line"})

    async def stack_trace(self, thread_id: int) -> list[dict]:
        resp = await self._send("stackTrace", {"threadId": thread_id, "startFrame": 0, "levels": 20})
        return resp.get("body", {}).get("stackFrames", [])

    async def scopes(self, frame_id: int) -> list[dict]:
        resp = await self._send("scopes", {"frameId": frame_id})
        return resp.get("body", {}).get("scopes", [])

    async def variables(self, variables_reference: int) -> list[dict]:
        resp = await self._send("variables", {"variablesReference": variables_reference})
        return resp.get("body", {}).get("variables", [])

    async def disconnect(self) -> None:
        try:
            await self._send("disconnect", {"terminateDebuggee": True})
        except (DapProtocolError, ConnectionError):
            pass


def _repo_root() -> "Path":
    """Path of the cOde(n) repo root. We don't import it
    directly to avoid a circular import; the worker is
    run from <repo> by the route layer, so the CWD works."""
    return Path(__file__).resolve().parent.parent.parent


# ---------------------------------------------------------------------------
# DebugController: spawns the worker, talks to the DAP client, owns state
# ---------------------------------------------------------------------------


@dataclass
class DebugState:
    """The state of one debug session, exposed to the WebSocket handler."""

    paused: bool = False
    current_line: Optional[int] = None
    current_frame_id: Optional[int] = None
    thread_id: Optional[int] = None
    # The most recent locals snapshot, as a list of variable
    # dicts (DAP format: name, value, type, variablesReference).
    locals: list[dict] = field(default_factory=list)
    # The most recent stopped event reason ("step", "breakpoint",
    # "exception", "entry", etc.).
    stopped_reason: str = ""
    # The path of the source file (so the UI can map frame
    # line numbers to the right file).
    source_path: str = ""


class DebugController:
    """Owns the worker subprocess + DAP client for one session.

    Lifecycle::

        controller = DebugController(challenge_id, source, n, seed)
        await controller.start()
        state = await controller.wait_for_stop()      # first pause
        await controller.continue_execution()
        state = await controller.wait_for_stop()      # next pause
        await controller.stop()
    """

    def __init__(self, challenge_id: str, source: str, n: int, seed: Optional[int]) -> None:
        self.challenge_id = challenge_id
        self.source = source
        self.n = n
        self.seed = seed
        self._proc: Optional[subprocess.Popen] = None
        self._client: Optional[DapClient] = None
        self._source_path: str = ""
        self.state = DebugState()
        self._stopped_event = asyncio.Event()

    # --- start / stop -------------------------------------------------

    async def start(self, breakpoints: Optional[list[int]] = None) -> None:
        """Write the source to a temp file, spawn the worker,
        connect the DAP client, and send the initial
        initialize/launch/configurationDone sequence."""
        # 1. Write the source to a temp file.
        import tempfile
        tmpdir = Path(tempfile.mkdtemp(prefix="coden-debug-"))
        self._source_path = str(tmpdir / "solution.py")
        Path(self._source_path).write_text(self.source, encoding="utf-8")
        self.state.source_path = self._source_path

        # 2. Pick a free port. We hand it to the worker; the
        # worker calls debugpy.listen on it. The server
        # already knows the port, so we can connect
        # immediately (debugpy.listen has bound by the time
        # the worker prints the CODEN_LISTENING line, even
        # though wait_for_client is still blocking).
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("127.0.0.1", 0))
            port = s.getsockname()[1]

        # 3. Spawn the worker.
        env = os.environ.copy()
        env["CODEN_BREAKPOINTS"] = ",".join(str(b) for b in (breakpoints or []))
        cmd = [
            sys.executable,
            str(_repo_root() / "server" / "debug_worker.py"),
            self._source_path,
            self.challenge_id,
            str(self.n),
            "None" if self.seed is None else str(self.seed),
            str(port),
        ]
        log.info("spawning debug worker: %s", " ".join(shlex.quote(c) for c in cmd))
        self._proc = subprocess.Popen(
            cmd,
            env=env,
            cwd=str(_repo_root()),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # 4. Wait for the worker to announce it's listening
        # (``CODEN_LISTENING: <port>``). This confirms the
        # subprocess started OK and the port is bound.
        listening = await self._wait_for_listening(timeout=10.0)
        if not listening:
            await self._kill_proc()
            raise RuntimeError("debug worker did not announce CODEN_LISTENING within 10s")

        # 5. Connect the DAP client. debugpy.listen has bound
        # the port; debugpy.wait_for_client is still blocking
        # on the accept loop, so the connect() succeeds.
        self._client = DapClient("127.0.0.1", port)
        await self._client.connect()

        # 6. Send initialize; then send attach (in-process) +
        # configurationDone.
        # NOTE: debugpy in in-process mode (which is what we
        # use — the worker calls ``debugpy.listen()`` from
        # the same Python process as the debugged code) does
        # NOT send the DAP ``initialized`` event after
        # ``initialize`` returns, and it REJECTS ``launch``
        # (responds with '"attach" expected') because the
        # debugged program is already loaded. We send
        # ``attach`` instead.
        await self._client.initialize()
        # Drain any pre-attach events so the queue stays
        # sane (e.g. the debugpySockets event lands here).
        try:
            await self._client.wait_for_event("initialized", timeout=0.5)
        except Exception:
            pass
        await self._client.attach_in_process()
        await self._client.configurationDone()

    async def stop(self) -> None:
        """Disconnect DAP and kill the subprocess."""
        if self._client is not None:
            try:
                await self._client.disconnect()
            except Exception:
                pass
            try:
                await self._client.close()
            except Exception:
                pass
            self._client = None
        await self._kill_proc()
        # Best-effort cleanup of the temp dir.
        try:
            import shutil
            shutil.rmtree(Path(self._source_path).parent, ignore_errors=True)
        except Exception:
            pass

    async def _kill_proc(self) -> None:
        if self._proc is None:
            return
        try:
            if self._proc.poll() is None:
                if os.name == "nt":
                    self._proc.terminate()
                else:
                    self._proc.send_signal(signal.SIGTERM)
                try:
                    self._proc.wait(timeout=3.0)
                except subprocess.TimeoutExpired:
                    self._proc.kill()
                    self._proc.wait(timeout=2.0)
        except Exception as e:
            log.warning("error killing debug worker: %s", e)
        self._proc = None

    async def _wait_for_listening(self, timeout: float) -> bool:
        """Read subprocess stdout line-by-line until we see
        ``CODEN_LISTENING: <port>`` or the subprocess exits."""
        loop = asyncio.get_event_loop()
        deadline = loop.time() + timeout
        assert self._proc is not None and self._proc.stdout is not None
        while loop.time() < deadline:
            if self._proc.poll() is not None:
                # Process died before announcing.
                try:
                    stdout = self._proc.stdout.read() or ""
                except Exception:
                    stdout = ""
                try:
                    stderr = self._proc.stderr.read() if self._proc.stderr else ""
                except Exception:
                    stderr = ""
                log.error(
                    "debug worker exited unexpectedly. rc=%s. stdout:\n%s\nstderr:\n%s",
                    self._proc.returncode, stdout, stderr,
                )
                return False
            line = await loop.run_in_executor(None, self._proc.stdout.readline)
            if not line:
                await asyncio.sleep(0.05)
                continue
            log.debug("debug worker stdout: %s", line.rstrip())
            if line.startswith("CODEN_LISTENING:"):
                return True
        return False

    # --- runtime control ---------------------------------------------

    async def wait_for_stop(self, timeout: float = 30.0) -> Optional[DebugState]:
        """Block until the next `stopped` event arrives, or
        return None on timeout / subprocess exit."""
        if self._client is None:
            return None
        # Drain stale events; we want the *next* stopped.
        while not self._event_queue.empty():
            try:
                self._event_queue.get_nowait()
            except asyncio.QueueEmpty:
                break
        event = await self._client.wait_for_event("stopped", timeout=timeout)
        if event is None:
            return None
        body = event.get("body", {})
        self.state.stopped_reason = body.get("reason", "")
        self.state.thread_id = body.get("threadId")
        if self.state.thread_id is None:
            return self.state
        # If we have a frame reference, fetch it.
        frame_id = body.get("frameId")
        if frame_id is not None:
            self.state.current_frame_id = frame_id
            self.state.locals = await self._fetch_locals(frame_id)
        # Try to derive the current line from the stack trace.
        try:
            frames = await self._client.stack_trace(self.state.thread_id)
            if frames:
                top = frames[0]
                self.state.current_line = top.get("line")
                # Use the top frame if body.frameId was None.
                if self.state.current_frame_id is None:
                    self.state.current_frame_id = top.get("id")
                    self.state.locals = await self._fetch_locals(self.state.current_frame_id)
        except Exception as e:
            log.debug("stack trace fetch failed: %s", e)
        self.state.paused = True
        return self.state

    async def continue_execution(self) -> None:
        await self._send_step("continue")

    async def step_over(self) -> None:
        await self._send_step("next")

    async def step_in(self) -> None:
        await self._send_step("step_in")

    async def step_out(self) -> None:
        await self._send_step("step_out")

    async def _send_step(self, op: str) -> None:
        if self._client is None or self.state.thread_id is None:
            return
        self.state.paused = False
        if op == "continue":
            await self._client.continue_execution(self.state.thread_id)
        elif op == "next":
            await self._client.next(self.state.thread_id)
        elif op == "step_in":
            await self._client.step_in(self.state.thread_id)
        elif op == "step_out":
            await self._client.step_out(self.state.thread_id)

    async def set_breakpoints(self, lines: list[int]) -> None:
        """Update the active breakpoint set. debugpy will fire
        on the next `stopped` event if the new lines are hit."""
        if self._client is None:
            return
        await self._client.setBreakpoints(self._source_path, lines)

    async def get_locals(self) -> list[dict]:
        """Return the most recently captured locals (DAP
        variables). Re-fetches from the adapter."""
        if self._client is None or self.state.current_frame_id is None:
            return self.state.locals
        self.state.locals = await self._fetch_locals(self.state.current_frame_id)
        return self.state.locals

    async def _fetch_locals(self, frame_id: int) -> list[dict]:
        """Walk the scopes chain and return the local variables
        (skipping the globals). The frontend's locals panel
        just needs the list."""
        if self._client is None:
            return []
        try:
            scopes = await self._client.scopes(frame_id)
        except Exception as e:
            log.debug("scopes() failed: %s", e)
            return []
        # Merge all the "Locals" / "locals" scopes; skip
        # "Globals" so we don't dump the whole world into the UI.
        out: list[dict] = []
        for scope in scopes:
            name = scope.get("name", "")
            ref = scope.get("variablesReference")
            if ref is None:
                continue
            if "global" in name.lower():
                continue
            try:
                vars_ = await self._client.variables(ref)
            except Exception as e:
                log.debug("variables() failed for scope %s: %s", name, e)
                continue
            for v in vars_:
                # Add a `scope` hint so the UI can label them.
                v = dict(v)
                v["scope"] = name
                out.append(v)
        return out

    @property
    def _event_queue(self) -> asyncio.Queue:
        """Expose the client's event queue so the route layer
        can also drain the `exited` event when the worker
        finishes."""
        assert self._client is not None
        return self._client._event_queue
