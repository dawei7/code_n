"""``POST /api/debug/sessions`` and ``WS /ws/debug/{id}``.

This module wires the ``DebugController`` to the frontend:

  * ``POST /api/debug/sessions`` starts a new session: writes
    the source to a temp file, spawns the debug worker,
    connects the DAP client. Returns a session id and a
    WebSocket URL.
  * ``WS /ws/debug/{id}`` is the live control channel. The
    client sends:
      * ``{"type": "set_breakpoints", "lines": [...]}``
      * ``{"type": "continue"}``
      * ``{"type": "step", "mode": "over" | "in" | "out"}``
      * ``{"type": "stop"}``
    The server sends:
      * ``{"type": "stopped", "line": N, "frame_id": N, "locals": [...]}``
      * ``{"type": "continued"}``
      * ``{"type": "exited", "result": {...}, "passed": bool}``
      * ``{"type": "output", "stream": "stdout"|"stderr", "text": "..."}``

The session is per-WebSocket: when the WS closes, the
controller is stopped and the subprocess is killed. There's
no "resume session" — every Debug click is a fresh run.
"""
from __future__ import annotations

import asyncio
import json
import logging
import secrets
from typing import Any, Optional

from fastapi import APIRouter, HTTPException, WebSocket, WebSocketDisconnect
from pydantic import BaseModel

from server.app.debug_controller import DebugController


log = logging.getLogger(__name__)


router = APIRouter()
ws_router = APIRouter()  # WebSocket routes are NOT prefixed
                          # with /api (the WS URL is /ws/...,
                          # not /api/ws/...).


# All active sessions, keyed by session id. Sessions are
# created in POST /api/debug/sessions and removed when the
# WebSocket closes (or stop() is called).
_SESSIONS: dict[str, "DebugSession"] = {}


# ---- Request schema for POST /api/debug/sessions ----


class StartSessionRequest(BaseModel):
    challenge_id: str
    source: str
    n: int
    seed: Optional[int] = None


class StartSessionResponse(BaseModel):
    session_id: str
    ws_url: str


class DebugSession:
    """Wraps a :class:`DebugController` for a single session.

    The WebSocket handler owns the lifecycle; we keep a small
    reference here so the controller can be looked up by id
    (and so the GC can clean it up if the WS handler is
    interrupted).
    """

    def __init__(self, controller: DebugController) -> None:
        self.controller = controller

    async def stop(self) -> None:
        try:
            await self.controller.stop()
        except Exception as e:
            log.warning("DebugSession.stop() failed: %s", e)


# ---- POST /api/debug/sessions ----


@router.post("/debug/sessions")
async def start_session(body: StartSessionRequest) -> StartSessionResponse:
    """Start a new debug session. Returns a session id and
    WebSocket URL the client can connect to."""
    session_id = secrets.token_urlsafe(16)
    controller = DebugController(
        challenge_id=body.challenge_id,
        source=body.source,
        n=body.n,
        seed=body.seed,
    )
    _SESSIONS[session_id] = DebugSession(controller)
    # Spawn the worker + connect DAP. The HTTP response only
    # fires once the worker is ready (or it 500s). Subsequent
    # control flows over the WebSocket.
    try:
        await controller.start(breakpoints=[])
    except Exception as e:
        _SESSIONS.pop(session_id, None)
        try:
            await controller.stop()
        except Exception:
            pass
        raise HTTPException(status_code=500, detail=f"failed to start debug session: {e}")
    return StartSessionResponse(
        session_id=session_id,
        ws_url=f"/ws/debug/{session_id}",
    )


# ---- WS /ws/debug/{session_id} ----


@ws_router.websocket("/ws/debug/{session_id}")
async def debug_socket(websocket: WebSocket, session_id: str) -> None:
    """WebSocket control channel for one debug session.

    We accept the WS, then drive the controller in a
    long-running coroutine. The client sends commands; we
    push stopped/continued/exited events back.
    """
    session = _SESSIONS.get(session_id)
    if session is None:
        await websocket.close(code=4404, reason="unknown session")
        return
    await websocket.accept()
    controller = session.controller
    try:
        # The first message from the client is "ready" (or
        # we could just go right into waiting for stopped).
        # We send the first stopped event right after
        # launch/configurationDone — the WS just delivers it.
        stop_task = asyncio.create_task(_wait_and_send_stop(websocket, controller))
        while True:
            try:
                raw = await websocket.receive_text()
            except WebSocketDisconnect:
                break
            try:
                msg = json.loads(raw)
            except json.JSONDecodeError:
                continue
            await _handle_client_message(websocket, controller, msg)
            if msg.get("type") == "stop":
                break
        # Cancel the stop-watcher; we're done.
        stop_task.cancel()
        try:
            await stop_task
        except (asyncio.CancelledError, Exception):
            pass
    except WebSocketDisconnect:
        pass
    finally:
        try:
            await session.stop()
        except Exception:
            pass
        _SESSIONS.pop(session_id, None)


async def _wait_and_send_stop(websocket: WebSocket, controller: DebugController) -> None:
    """Background task: wait for the next stopped event from
    debugpy, push it over the WS, then loop. Exits when the
    subprocess terminates (sends `exited`)."""
    try:
        while True:
            state = await controller.wait_for_stop(timeout=15.0)
            if state is None:
                # Timeout — check whether the subprocess is
                # still alive.
                if controller._proc is None or controller._proc.poll() is not None:
                    # Worker exited. Read final stdout.
                    final_result = _read_final_result(controller)
                    await websocket.send_json({
                        "type": "exited",
                        "result": final_result,
                        "passed": _is_passing(final_result),
                    })
                    return
                continue
            await websocket.send_json({
                "type": "stopped",
                "line": state.current_line,
                "frame_id": state.current_frame_id,
                "thread_id": state.thread_id,
                "reason": state.stopped_reason,
                "locals": state.locals,
            })
    except Exception as e:
        log.warning("debug WS stop-watcher ended: %s", e)


async def _handle_client_message(
    websocket: WebSocket, controller: DebugController, msg: dict
) -> None:
    t = msg.get("type")
    if t == "set_breakpoints":
        lines = msg.get("lines") or []
        try:
            await controller.set_breakpoints([int(x) for x in lines])
        except Exception as e:
            await websocket.send_json({"type": "error", "message": f"set_breakpoints: {e}"})
    elif t == "continue":
        try:
            await controller.continue_execution()
            await websocket.send_json({"type": "continued"})
        except Exception as e:
            await websocket.send_json({"type": "error", "message": f"continue: {e}"})
    elif t == "step":
        mode = msg.get("mode")
        try:
            if mode == "over":
                await controller.step_over()
            elif mode == "in":
                await controller.step_in()
            elif mode == "out":
                await controller.step_out()
            else:
                await websocket.send_json({"type": "error", "message": f"unknown step mode: {mode}"})
                return
            await websocket.send_json({"type": "continued"})
        except Exception as e:
            await websocket.send_json({"type": "error", "message": f"step: {e}"})
    elif t == "stop":
        # Final cleanup; the outer handler will see this and break.
        try:
            await controller.stop()
        except Exception:
            pass
    else:
        await websocket.send_json({"type": "error", "message": f"unknown type: {t}"})


def _read_final_result(controller: DebugController) -> dict:
    """Read the worker's stdout for the CODEN_RESULT: line."""
    if controller._proc is None or controller._proc.stdout is None:
        return {}
    try:
        # Read what's left in the pipe. The worker emits one
        # JSON line on stdout at the end; everything before
        # that is debugpy's own output.
        import os
        fd = controller._proc.stdout.fileno()
        # Non-blocking read of all available data.
        import select
        chunks = []
        while True:
            r, _, _ = select.select([fd], [], [], 0.0)
            if not r:
                break
            chunk = os.read(fd, 4096).decode("utf-8", errors="replace")
            if not chunk:
                break
            chunks.append(chunk)
        text = "".join(chunks)
    except Exception as e:
        log.debug("reading final result failed: %s", e)
        return {}
    for line in text.splitlines():
        if line.startswith("CODEN_RESULT:"):
            try:
                return json.loads(line[len("CODEN_RESULT:"):].strip())
            except json.JSONDecodeError:
                return {}
    return {}


def _is_passing(result: dict) -> bool:
    """The worker doesn't run the verify_fn (it's purely a
    debug session), so we don't have a 'passed' verdict from
    the engine. The frontend treats the run as "exploratory"
    — the verdict only matters for the regular Run path. We
    return True here just so the UI can show a neutral
    "exited" state."""
    return False  # explore mode; the player runs the regular
                  # "Run" path to get a verdict
