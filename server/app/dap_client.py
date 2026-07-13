"""Small Debug Adapter Protocol client used by the in-app debugger."""
from __future__ import annotations

import asyncio
import json
import subprocess
from asyncio.subprocess import Process
from collections import defaultdict
from typing import Any


class DAPError(RuntimeError):
    """Raised when the debug adapter reports a failed request."""


class DAPClient:
    def __init__(self) -> None:
        self._process: Process | None = None
        self._reader: asyncio.StreamReader | None = None
        self._writer: asyncio.StreamWriter | None = None
        self._seq = 1
        self._pending: dict[int, asyncio.Future[dict[str, Any]]] = {}
        self._events: asyncio.Queue[dict[str, Any]] = asyncio.Queue()
        self._event_waiters: dict[str, list[asyncio.Future[dict[str, Any]]]] = defaultdict(list)
        self._reader_task: asyncio.Task[None] | None = None
        self._stdout_task: asyncio.Task[None] | None = None
        self._stderr_task: asyncio.Task[None] | None = None
        self._write_lock = asyncio.Lock()

    async def start(
        self,
        executable: str,
        args: list[str],
        *,
        cwd: str,
        env: dict[str, str],
        connect_host: str | None = None,
        connect_port: int | None = None,
    ) -> None:
        if connect_host is not None and connect_port is not None:
            await self._start_tcp_adapter(
                executable,
                args,
                cwd=cwd,
                env=env,
                connect_host=connect_host,
                connect_port=connect_port,
            )
            return

        self._process = await asyncio.create_subprocess_exec(
            executable,
            *args,
            cwd=cwd,
            env=env,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        self._reader = self._process.stdout
        self._writer = self._process.stdin
        self._reader_task = asyncio.create_task(self._read_loop())
        if self._process.stderr:
            self._stderr_task = asyncio.create_task(self._drain_stream(self._process.stderr))

    async def stop(self) -> None:
        if self._reader_task:
            self._reader_task.cancel()
        if self._stdout_task:
            self._stdout_task.cancel()
        if self._stderr_task:
            self._stderr_task.cancel()
        if self._writer and not self._writer.is_closing():
            self._writer.close()
            try:
                await self._writer.wait_closed()
            except (BrokenPipeError, ConnectionResetError):
                pass
        if self._process and self._process.returncode is None:
            self._process.terminate()
            try:
                await asyncio.wait_for(self._process.wait(), timeout=2)
            except asyncio.TimeoutError:
                self._process.kill()

    async def request(self, command: str, arguments: dict[str, Any] | None = None) -> dict[str, Any]:
        if not self._process or not self._writer:
            raise DAPError("debug adapter is not running")
        seq = self._seq
        self._seq += 1
        loop = asyncio.get_running_loop()
        future: asyncio.Future[dict[str, Any]] = loop.create_future()
        self._pending[seq] = future
        await self._write(
            {
                "seq": seq,
                "type": "request",
                "command": command,
                "arguments": arguments or {},
            }
        )
        message = await future
        if not message.get("success", False):
            raise DAPError(str(message.get("message") or f"{command} failed"))
        body = message.get("body")
        return body if isinstance(body, dict) else {}

    async def events(self) -> dict[str, Any]:
        return await self._events.get()

    async def wait_for_event(self, event_name: str, timeout: float = 5.0) -> dict[str, Any]:
        loop = asyncio.get_running_loop()
        future: asyncio.Future[dict[str, Any]] = loop.create_future()
        self._event_waiters[event_name].append(future)
        return await asyncio.wait_for(future, timeout=timeout)

    async def _write(self, message: dict[str, Any]) -> None:
        assert self._writer
        payload = json.dumps(message, separators=(",", ":")).encode("utf-8")
        header = f"Content-Length: {len(payload)}\r\n\r\n".encode("ascii")
        async with self._write_lock:
            self._writer.write(header + payload)
            await self._writer.drain()

    async def _read_loop(self) -> None:
        assert self._reader
        reader = self._reader
        while True:
            headers: dict[str, str] = {}
            while True:
                line = await reader.readline()
                if not line:
                    self._fail_pending("debug adapter exited")
                    return
                text = line.decode("ascii", errors="replace").strip()
                if not text:
                    break
                key, _, value = text.partition(":")
                headers[key.lower()] = value.strip()
            length = int(headers.get("content-length", "0"))
            if length <= 0:
                continue
            try:
                raw = await reader.readexactly(length)
            except asyncio.IncompleteReadError:
                self._fail_pending("debug adapter exited")
                return
            message = json.loads(raw.decode("utf-8"))
            message_type = message.get("type")
            if message_type == "response":
                request_seq = message.get("request_seq")
                future = self._pending.pop(request_seq, None)
                if future and not future.done():
                    future.set_result(message)
            elif message_type == "event":
                event_name = str(message.get("event", ""))
                for future in self._event_waiters.pop(event_name, []):
                    if not future.done():
                        future.set_result(message)
                await self._events.put(message)

    async def _start_tcp_adapter(
        self,
        executable: str,
        args: list[str],
        *,
        cwd: str,
        env: dict[str, str],
        connect_host: str,
        connect_port: int,
    ) -> None:
        self._process = await asyncio.create_subprocess_exec(
            executable,
            *args,
            cwd=cwd,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        if self._process.stdout:
            self._stdout_task = asyncio.create_task(self._drain_stream(self._process.stdout))
        if self._process.stderr:
            self._stderr_task = asyncio.create_task(self._drain_stream(self._process.stderr))

        last_error: OSError | None = None
        loop = asyncio.get_running_loop()
        deadline = loop.time() + 5.0
        while loop.time() < deadline:
            if self._process.returncode is not None:
                raise DAPError("debug adapter exited")
            try:
                self._reader, self._writer = await asyncio.open_connection(connect_host, connect_port)
                self._reader_task = asyncio.create_task(self._read_loop())
                return
            except OSError as exc:
                last_error = exc
                await asyncio.sleep(0.05)
        raise DAPError(f"could not connect to debug adapter: {last_error}")

    async def _drain_stream(self, stream: asyncio.StreamReader) -> None:
        while await stream.readline():
            pass

    def _fail_pending(self, message: str) -> None:
        for future in self._pending.values():
            if not future.done():
                future.set_exception(DAPError(message))
        self._pending.clear()
