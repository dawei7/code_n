"""In-app Python debugger WebSocket powered by debugpy and DAP."""
from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path
from typing import Any

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from challenges.registry import CHALLENGE_REGISTRY
from server.app.config import CODEN_HOME, PROJECT_ROOT, SOLUTIONS_DIR
from server.app.dap_client import DAPClient, DAPError


router = APIRouter()


class DebugPythonUnavailable(RuntimeError):
    """Raised when a packaged build is missing its bundled debug runtime."""


def _is_packaged_server() -> bool:
    executable_name = Path(sys.executable).name.lower()
    return (
        os.environ.get("CODEN_PACKAGED_SERVER") == "1"
        or executable_name in {"coden-server.exe", "coden-server"}
    )


def _debug_python_exe() -> str:
    configured = os.environ.get("CODEN_DEBUG_PYTHON") or os.environ.get("CODEN_PYTHON_EXE")
    if configured and Path(configured).is_file():
        return configured
    if _is_packaged_server():
        expected = configured or "<missing CODEN_DEBUG_PYTHON>"
        raise DebugPythonUnavailable(
            "The bundled debug Python runtime is missing or invalid "
            f"({expected}). Rebuild the Windows app so resources/debug-python/python.exe "
            "is included."
        )
    if Path(sys.executable).name.lower() not in {"coden-server.exe", "coden-server"}:
        return sys.executable
    raise DebugPythonUnavailable("No usable Python interpreter is available for debugging.")


def _solution_path(challenge_id: str) -> Path:
    return SOLUTIONS_DIR / f"{challenge_id}.py"


def _runner_path() -> Path:
    user_runner = CODEN_HOME / "tools" / "debug_solution.py"
    if user_runner.is_file():
        return user_runner
    return PROJECT_ROOT / "tools" / "debug_solution.py"


def _project_path() -> Path:
    if (CODEN_HOME / "server").is_dir() and (CODEN_HOME / "challenges").is_dir():
        return CODEN_HOME
    return PROJECT_ROOT


def _as_int(value: Any, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


@router.websocket("/debug/ws")
async def debug_ws(websocket: WebSocket) -> None:
    await websocket.accept()
    dap = DAPClient()
    send_lock = asyncio.Lock()
    relay_task: asyncio.Task[None] | None = None

    async def send(payload: dict[str, Any]) -> None:
        async with send_lock:
            await websocket.send_json(payload)

    async def start_session(payload: dict[str, Any]) -> None:
        nonlocal relay_task
        challenge_id = str(payload.get("challengeId") or "")
        if challenge_id not in CHALLENGE_REGISTRY:
            await send({"type": "error", "message": f"Unknown challenge: {challenge_id}"})
            return

        solution_path = _solution_path(challenge_id)
        if not solution_path.is_file():
            await send({"type": "error", "message": f"Solution file not found: {solution_path}"})
            return

        try:
            python_exe = _debug_python_exe()
        except DebugPythonUnavailable as exc:
            await send({"type": "error", "message": str(exc)})
            return
        project_path = _project_path()
        runner = _runner_path()
        if not runner.is_file():
            await send({"type": "error", "message": f"Debug runner not found: {runner}"})
            return

        env = os.environ.copy()
        for key in list(env):
            if key.upper() == "PYTHONHOME":
                env.pop(key, None)
        env["CODEN_HOME"] = str(CODEN_HOME)
        existing_pythonpath = "" if _is_packaged_server() else env.get("PYTHONPATH", "")
        env["PYTHONPATH"] = os.pathsep.join(
            p for p in [str(project_path), existing_pythonpath] if p
        )

        try:
            await dap.start(
                python_exe,
                ["-m", "debugpy.adapter"],
                cwd=str(project_path),
                env=env,
            )
            await dap.request(
                "initialize",
                {
                    "adapterID": "debugpy",
                    "clientID": "coden",
                    "clientName": "cOde(n)",
                    "pathFormat": "path",
                    "linesStartAt1": True,
                    "columnsStartAt1": True,
                    "supportsVariableType": True,
                    "supportsRunInTerminalRequest": False,
                },
            )
            launch_task = asyncio.create_task(
                dap.request(
                    "launch",
                    {
                        "name": "cOde(n) in-app debug",
                        "type": "python",
                        "request": "launch",
                        "program": str(runner),
                        "python": [python_exe],
                        "debugLauncherPython": python_exe,
                        "cwd": str(project_path),
                        "args": [
                            challenge_id,
                            "--n",
                            str(_as_int(payload.get("n"), 16)),
                            "--mode",
                            str(payload.get("mode") or "practice"),
                            "--no-hold",
                        ]
                        + (
                            ["--seed", str(payload.get("seed"))]
                            if payload.get("seed") is not None
                            else []
                        ),
                        "env": env,
                        "console": "internalConsole",
                        "justMyCode": False,
                        "stopOnEntry": False,
                    },
                )
            )
            await dap.wait_for_event("initialized")
            await _set_breakpoints(dap, solution_path, payload.get("breakpoints"))
            await dap.request("configurationDone")
            await launch_task
        except Exception as exc:
            await send({"type": "error", "message": _debug_start_error(exc, python_exe)})
            await dap.stop()
            return

        relay_task = asyncio.create_task(_relay_dap_events(dap, send))
        await send({"type": "started"})

    try:
        first = await websocket.receive_json()
        if not isinstance(first, dict) or first.get("type") != "start":
            await send({"type": "error", "message": "First debugger message must be 'start'."})
            return
        await start_session(first)

        while True:
            payload = await websocket.receive_json()
            if not isinstance(payload, dict):
                continue
            command = payload.get("type")
            try:
                if command == "continue":
                    await dap.request("continue", {"threadId": payload.get("threadId", 1)})
                elif command == "stepOver":
                    await dap.request("next", {"threadId": payload.get("threadId", 1)})
                elif command == "stepIn":
                    await dap.request("stepIn", {"threadId": payload.get("threadId", 1)})
                elif command == "stepOut":
                    await dap.request("stepOut", {"threadId": payload.get("threadId", 1)})
                elif command == "setBreakpoints":
                    await _set_breakpoints(dap, _solution_path(str(payload.get("challengeId") or "")), payload.get("breakpoints"))
                elif command == "stop":
                    await dap.request("disconnect", {"terminateDebuggee": True})
                    break
            except DAPError as exc:
                await send({"type": "error", "message": str(exc)})
    except WebSocketDisconnect:
        pass
    finally:
        if relay_task:
            relay_task.cancel()
        await dap.stop()


async def _set_breakpoints(dap: DAPClient, path: Path, raw_breakpoints: Any) -> None:
    breakpoints = raw_breakpoints if isinstance(raw_breakpoints, list) else []
    lines = sorted({int(line) for line in breakpoints if isinstance(line, int) and line > 0})
    await dap.request(
        "setBreakpoints",
        {
            "source": {"path": str(path)},
            "breakpoints": [{"line": line} for line in lines],
            "sourceModified": False,
        },
    )


async def _relay_dap_events(dap: DAPClient, send) -> None:
    while True:
        event = await dap.events()
        name = event.get("event")
        body = event.get("body") if isinstance(event.get("body"), dict) else {}
        if name == "output":
            await send({
                "type": "output",
                "category": body.get("category", "stdout"),
                "output": body.get("output", ""),
            })
        elif name == "stopped":
            await send(await _paused_payload(dap, body))
        elif name == "continued":
            await send({"type": "continued", "threadId": body.get("threadId")})
        elif name in {"exited", "terminated"}:
            await send({"type": "exited"})


async def _paused_payload(dap: DAPClient, body: dict[str, Any]) -> dict[str, Any]:
    thread_id = body.get("threadId")
    if thread_id is None:
        threads = await dap.request("threads")
        all_threads = threads.get("threads") if isinstance(threads.get("threads"), list) else []
        thread_id = all_threads[0].get("id") if all_threads else 1
    stack = await dap.request("stackTrace", {"threadId": thread_id, "startFrame": 0, "levels": 20})
    frames = stack.get("stackFrames") if isinstance(stack.get("stackFrames"), list) else []
    top = frames[0] if frames else {}
    scopes = []
    locals_out = []
    if top.get("id") is not None:
        scopes_body = await dap.request("scopes", {"frameId": top["id"]})
        scopes = scopes_body.get("scopes") if isinstance(scopes_body.get("scopes"), list) else []
    for scope in scopes:
        if str(scope.get("name", "")).lower() not in {"locals", "arguments"}:
            continue
        variables_reference = scope.get("variablesReference")
        if not variables_reference:
            continue
        variables = await dap.request("variables", {"variablesReference": variables_reference})
        for variable in variables.get("variables", []) if isinstance(variables.get("variables"), list) else []:
            locals_out.append({
                "name": variable.get("name", ""),
                "value": variable.get("value", ""),
                "type": variable.get("type", ""),
            })
    return {
        "type": "stopped",
        "reason": body.get("reason", "pause"),
        "threadId": thread_id,
        "line": top.get("line"),
        "column": top.get("column"),
        "path": (top.get("source") or {}).get("path") if isinstance(top.get("source"), dict) else None,
        "stack": [
            {
                "id": frame.get("id"),
                "name": frame.get("name"),
                "line": frame.get("line"),
                "path": (frame.get("source") or {}).get("path") if isinstance(frame.get("source"), dict) else None,
            }
            for frame in frames
        ],
        "locals": locals_out,
    }


def _debug_start_error(exc: Exception, python_exe: str) -> str:
    message = str(exc)
    if "No module named debugpy" in message or "debug adapter exited" in message:
        if _is_packaged_server():
            return (
                f"Could not start the bundled debugger with {python_exe}. "
                "Rebuild the Windows app so resources/debug-python contains "
                "python.exe and debugpy."
            )
        return (
            f"Could not start debugpy with {python_exe}. Install debugpy in that Python "
            "environment (`python -m pip install debugpy`) and try again."
        )
    return message
