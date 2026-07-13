"""In-app debugger WebSocket powered by Debug Adapter Protocol."""
from __future__ import annotations

import asyncio
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable
from xml.sax.saxutils import escape as xml_escape

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from challenges.registry import CHALLENGE_REGISTRY
from engine.languages import SUPPORTED_LANGUAGES, SupportedLanguage, normalize_language
from server.app.config import CODEN_HOME, PROJECT_ROOT
from server.app.user_solutions import active_solution_path
from server.app.dap_client import DAPClient, DAPError
from server.app.external_programs import (
    _cpp_function_harness,
    _csharp_function_harness,
    _dotnet_target_framework,
    _go_function_harness,
    _java_function_harness,
    _javascript_function_harness,
    _kotlin_function_harness,
    _run_process,
)
from server.app.validated_cases import InvalidCustomCase, NoValidatedCases, select_cases_for_run


router = APIRouter()


class DebugPythonUnavailable(RuntimeError):
    """Raised when a packaged build is missing its bundled debug runtime."""


class DebugPreparationError(RuntimeError):
    """Raised when a language-specific debug target cannot be built."""


@dataclass
class PreparedDebugSession:
    adapter_executable: str
    adapter_args: list[str]
    adapter_id: str
    cwd: str
    env: dict[str, str]
    launch_config: dict[str, Any]
    breakpoint_path: Path
    adapter_connect_host: str | None = None
    adapter_connect_port: int | None = None
    tempdir: tempfile.TemporaryDirectory[str] | None = None
    context: dict[str, Any] = field(default_factory=dict)

    def cleanup(self) -> None:
        if self.tempdir is not None:
            self.tempdir.cleanup()


@dataclass(frozen=True)
class JavaDebugTarget:
    main_class: str
    classpath: Path
    source_path: Path


_DEBUG_LABELS: dict[SupportedLanguage, str] = {
    "python": "Python",
    "cpp": "C++",
    "java": "Java",
    "csharp": "C#",
    "javascript": "JavaScript",
    "go": "Go",
    "kotlin": "Kotlin",
    "sql": "SQL",
    "bash": "Bash",
}


_DEBUG_INSTALL_HINTS: dict[SupportedLanguage, str] = {
    "python": "Install debugpy in the selected Python runtime.",
    "cpp": "Install LLVM lldb-dap or lldb-vscode plus g++ or clang++ on PATH, set CODEN_CPP_DEBUG_ADAPTER/CODEN_CPP_COMPILER, or place them under CODEN_DEBUG_TOOLS_DIR.",
    "java": "Install a JDK plus a Java debug adapter on PATH/debug-tools, or set CODEN_JAVAC, CODEN_JAVA, and CODEN_JAVA_DEBUG_ADAPTER.",
    "csharp": "Install netcoredbg and the .NET SDK on PATH, set CODEN_NETCOREDBG/CODEN_DOTNET, or place them under CODEN_DEBUG_TOOLS_DIR.",
    "javascript": "Install Node.js and a JavaScript DAP adapter, set CODEN_NODE and CODEN_JS_DEBUG_ADAPTER, or place them under CODEN_DEBUG_TOOLS_DIR.",
    "go": "Install Go plus delve/dlv, set CODEN_GO and CODEN_GO_DEBUG_ADAPTER, or place them under CODEN_DEBUG_TOOLS_DIR.",
    "kotlin": "Install Kotlin, Java, and a Java/Kotlin debug adapter, set CODEN_KOTLINC, CODEN_JAVA, and CODEN_JAVA_DEBUG_ADAPTER, or place them under CODEN_DEBUG_TOOLS_DIR.",
    "sql": "Run SQL against the in-memory database and inspect its result grid; statement-level DAP stepping is not available.",
    "bash": "Run Bash with stdin and file fixtures; shell DAP stepping is not available.",
}


_TOOL_ENV_OVERRIDES = {
    "lldb-dap": "CODEN_CPP_DEBUG_ADAPTER",
    "lldb-vscode": "CODEN_CPP_DEBUG_ADAPTER",
    "g++": "CODEN_CPP_COMPILER",
    "clang++": "CODEN_CPP_COMPILER",
    "javac": "CODEN_JAVAC",
    "java": "CODEN_JAVA",
    "dotnet": "CODEN_DOTNET",
    "netcoredbg": "CODEN_NETCOREDBG",
    "node": "CODEN_NODE",
    "js-debug-adapter": "CODEN_JS_DEBUG_ADAPTER",
    "go": "CODEN_GO",
    "kotlinc": "CODEN_KOTLINC",
    "dlv": "CODEN_GO_DEBUG_ADAPTER",
}


_TOOL_FILENAMES = {
    "lldb-dap": ("lldb-dap.exe", "lldb-dap"),
    "lldb-vscode": ("lldb-vscode.exe", "lldb-vscode"),
    "g++": ("g++.exe", "g++"),
    "clang++": ("clang++.exe", "clang++"),
    "javac": ("javac.exe", "javac"),
    "java": ("java.exe", "java"),
    "dotnet": ("dotnet.exe", "dotnet"),
    "netcoredbg": ("netcoredbg.exe", "netcoredbg"),
    "node": ("node.exe", "node"),
    "js-debug-adapter": (
        "js-debug-adapter.cmd",
        "js-debug-adapter.bat",
        "js-debug-adapter.exe",
        "js-debug-adapter",
        "js-debug-adapter.js",
        "dapDebugServer.js",
    ),
    "go": ("go.exe", "go"),
    "kotlinc": ("kotlinc.bat", "kotlinc.exe", "kotlinc"),
    "dlv": ("dlv.exe", "dlv"),
}

_DEBUG_TOOL_SUBDIRS = (
    "",
    "bin",
    "cpp",
    "cpp/bin",
    "java",
    "java/bin",
    "jdk/bin",
    "csharp",
    "csharp/bin",
    "dotnet",
    "dotnet/bin",
    "javascript",
    "javascript/bin",
    "js-debug",
    "js-debug/bin",
    "node",
    "node/bin",
    "go",
    "go/bin",
    "kotlin",
    "kotlin/bin",
)

_JAVA_DEBUG_ADAPTER_FILENAMES = (
    "java-debug-adapter.exe",
    "java-debug-adapter",
    "java-debug-adapter.jar",
    "java-debug.jar",
)

_JS_DEBUG_ADAPTER_FILENAMES = _TOOL_FILENAMES["js-debug-adapter"]


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


def _solution_path(challenge_id: str, language: str | None = "python") -> Path:
    return active_solution_path(challenge_id, normalize_language(language))


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


@router.get("/debug/capabilities")
def debug_capabilities() -> dict[str, Any]:
    """Return language debugger readiness for the in-app UI.

    The frontend should ask this endpoint instead of assuming Python-only
    debugging. A language can have a known DAP profile while still being
    unavailable on the current machine because its adapter or compiler/runtime
    is not installed.
    """
    languages = {
        language: _debug_capability(language)
        for language in SUPPORTED_LANGUAGES
    }
    return {"languages": languages}


def _debug_capability(language: str | None) -> dict[str, Any]:
    language_id = normalize_language(language)
    label = _DEBUG_LABELS[language_id]
    adapter_id = {
        "python": "debugpy",
        "cpp": "lldb-dap",
        "java": "java-debug",
        "csharp": "netcoredbg",
        "javascript": "js-debug",
        "go": "delve-dap",
        "kotlin": "java-debug",
        "sql": "sql-playground",
        "bash": "bash-playground",
    }[language_id]
    missing: list[str] = []
    adapter_command: str | None = None

    if language_id == "python":
        try:
            python_exe = _debug_python_exe()
            adapter_command = f"{python_exe} -m debugpy.adapter"
            if not _python_has_debugpy(python_exe):
                missing.append("debugpy")
        except DebugPythonUnavailable as exc:
            missing.append(str(exc))
    elif language_id == "cpp":
        adapter_command = _first_tool("lldb-dap", "lldb-vscode")
        if adapter_command is None:
            missing.append("lldb-dap or lldb-vscode")
        if _first_tool("g++", "clang++") is None:
            missing.append("g++ or clang++")
    elif language_id == "java":
        adapter_command = _java_debug_adapter_path()
        if adapter_command is None:
            missing.append("Java debug adapter")
        if _first_tool("javac") is None or _first_tool("java") is None:
            missing.append("javac and java")
    elif language_id == "csharp":
        adapter_command = _first_tool("netcoredbg")
        if adapter_command is None:
            missing.append("netcoredbg")
        if _first_tool("dotnet") is None:
            missing.append("dotnet SDK")
    elif language_id == "javascript":
        adapter_command = _js_debug_adapter_path()
        if adapter_command is None:
            missing.append("JavaScript debug adapter")
        if _first_tool("node") is None:
            missing.append("Node.js")
    elif language_id == "go":
        adapter_command = _first_tool("dlv")
        if adapter_command is None:
            missing.append("delve/dlv")
        if _first_tool("go") is None:
            missing.append("Go toolchain")
    elif language_id == "kotlin":
        adapter_command = _java_debug_adapter_path()
        if adapter_command is None:
            missing.append("Java/Kotlin debug adapter")
        if _first_tool("kotlinc") is None or _first_tool("java") is None:
            missing.append("kotlinc and java")

    launch_supported = language_id in {"python", "cpp", "java", "csharp", "javascript", "go", "kotlin"}
    if not launch_supported:
        missing.append("language launch wiring")

    available = not missing and launch_supported
    if available:
        message = f"{label} debugger is ready."
    else:
        missing_text = ", ".join(missing)
        message = f"{label} debugger is not ready: missing {missing_text}."

    return {
        "language": language_id,
        "label": label,
        "adapter_id": adapter_id,
        "adapter_command": adapter_command,
        "available": available,
        "launch_supported": launch_supported,
        "missing": missing,
        "message": message,
        "install_hint": _DEBUG_INSTALL_HINTS[language_id],
    }


def _first_tool(*names: str) -> str | None:
    for name in names:
        env_name = _TOOL_ENV_OVERRIDES.get(name)
        if env_name:
            configured = _configured_file(env_name, _TOOL_FILENAMES.get(name))
            if configured:
                return configured
    for root in _debug_tool_dirs():
        for name in names:
            bundled = _find_named_file(root, _TOOL_FILENAMES.get(name, (name,)))
            if bundled:
                return bundled
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    return None


def _configured_file(env_name: str, filenames: Iterable[str] | None = None) -> str | None:
    value = os.environ.get(env_name)
    if not value:
        return None
    path = Path(value)
    if path.is_file():
        return str(path)
    if path.is_dir() and filenames is not None:
        return _find_named_file(path, filenames)
    return None


def _java_debug_adapter_path() -> str | None:
    configured = _configured_file("CODEN_JAVA_DEBUG_ADAPTER", _JAVA_DEBUG_ADAPTER_FILENAMES)
    if configured:
        return configured
    for root in _debug_tool_dirs():
        adapter = _find_named_file(root, _JAVA_DEBUG_ADAPTER_FILENAMES)
        if adapter:
            return adapter
    return None


def _js_debug_adapter_path() -> str | None:
    configured = _configured_file("CODEN_JS_DEBUG_ADAPTER", _JS_DEBUG_ADAPTER_FILENAMES)
    if configured:
        return configured
    for root in _debug_tool_dirs():
        adapter = _find_named_file(root, _JS_DEBUG_ADAPTER_FILENAMES)
        if adapter:
            return adapter
    return None


def _debug_tool_dirs() -> list[Path]:
    dirs: list[Path] = []
    configured = os.environ.get("CODEN_DEBUG_TOOLS_DIR", "")
    for raw in configured.split(os.pathsep):
        raw = raw.strip()
        if raw:
            dirs.append(Path(raw))
    dirs.extend(
        [
            CODEN_HOME / "debug-tools",
            PROJECT_ROOT / "debug-tools",
            PROJECT_ROOT / "server" / "dist" / "debug-tools",
        ]
    )

    seen: set[str] = set()
    existing: list[Path] = []
    for directory in dirs:
        try:
            resolved = str(directory.resolve())
        except OSError:
            resolved = str(directory)
        if resolved in seen or not directory.is_dir():
            continue
        seen.add(resolved)
        existing.append(directory)
    return existing


def _find_named_file(root: Path, filenames: Iterable[str]) -> str | None:
    names = tuple(filenames)
    for subdir in _DEBUG_TOOL_SUBDIRS:
        base = root / Path(subdir) if subdir else root
        for name in names:
            candidate = base / name
            if candidate.is_file():
                return str(candidate)
    return None


def _python_has_debugpy(python_exe: str) -> bool:
    try:
        result = subprocess.run(
            [python_exe, "-c", "import debugpy"],
            text=True,
            capture_output=True,
            timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    return result.returncode == 0


@router.websocket("/debug/ws")
async def debug_ws(websocket: WebSocket) -> None:
    await websocket.accept()
    dap = DAPClient()
    send_lock = asyncio.Lock()
    relay_task: asyncio.Task[None] | None = None
    prepared_session: PreparedDebugSession | None = None

    async def send(payload: dict[str, Any]) -> None:
        async with send_lock:
            await websocket.send_json(payload)

    async def start_session(payload: dict[str, Any]) -> None:
        nonlocal relay_task, prepared_session
        challenge_id = str(payload.get("challengeId") or "")
        if challenge_id not in CHALLENGE_REGISTRY:
            await send({"type": "error", "message": f"Unknown challenge: {challenge_id}"})
            return

        try:
            language_id = normalize_language(str(payload.get("language") or "python"))
        except ValueError as exc:
            await send({"type": "error", "message": str(exc)})
            return

        capability = _debug_capability(language_id)
        if not capability["available"]:
            await send({
                "type": "error",
                "phase": "capability",
                "message": capability["message"],
                "detail": capability.get("install_hint", ""),
            })
            return

        try:
            prepared_session = _prepare_debug_session(payload, language_id)
        except (DebugPythonUnavailable, DebugPreparationError, ValueError) as exc:
            await send({
                "type": "error",
                "phase": "prepare",
                "message": str(exc),
                "detail": _exception_detail(exc),
            })
            return

        await send({"type": "context", **prepared_session.context})
        try:
            await dap.start(
                prepared_session.adapter_executable,
                prepared_session.adapter_args,
                cwd=prepared_session.cwd,
                env=prepared_session.env,
                connect_host=prepared_session.adapter_connect_host,
                connect_port=prepared_session.adapter_connect_port,
            )
            await dap.request(
                "initialize",
                {
                    "adapterID": prepared_session.adapter_id,
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
                    prepared_session.launch_config,
                )
            )
            await dap.wait_for_event("initialized")
            verified_breakpoints = await _set_breakpoints(
                dap, prepared_session.breakpoint_path, payload.get("breakpoints")
            )
            await send({"type": "breakpoints", "breakpoints": verified_breakpoints})
            await dap.request("configurationDone")
            await launch_task
        except Exception as exc:
            await send({
                "type": "error",
                "phase": "launch",
                "message": _debug_start_error(
                    exc,
                    language_id,
                    prepared_session.adapter_executable,
                ),
                "detail": _exception_detail(exc),
                "adapter": prepared_session.adapter_executable,
            })
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
                    verified_breakpoints = await _set_breakpoints(
                        dap,
                        prepared_session.breakpoint_path if prepared_session is not None else _solution_path(
                            str(payload.get("challengeId") or ""),
                            str(payload.get("language") or "python"),
                        ),
                        payload.get("breakpoints"),
                    )
                    await send({"type": "breakpoints", "breakpoints": verified_breakpoints})
                elif command == "selectFrame":
                    frame_id = _as_int(payload.get("frameId"), 0)
                    await send({"type": "frame", **await _frame_payload(dap, frame_id)})
                elif command == "variables":
                    variables_reference = _as_int(payload.get("variablesReference"), 0)
                    variables = await dap.request(
                        "variables", {"variablesReference": variables_reference}
                    )
                    await send({
                        "type": "variables",
                        "requestId": payload.get("requestId"),
                        "variablesReference": variables_reference,
                        "variables": [
                            _debug_variable_payload(variable)
                            for variable in variables.get("variables", [])
                            if isinstance(variable, dict)
                        ] if isinstance(variables.get("variables"), list) else [],
                    })
                elif command == "evaluate":
                    expression = str(payload.get("expression") or "").strip()
                    frame_id = _as_int(payload.get("frameId"), 0)
                    if expression:
                        try:
                            evaluated = await dap.request(
                                "evaluate",
                                {"expression": expression, "frameId": frame_id, "context": "watch"},
                            )
                            await send({
                                "type": "watchResult",
                                "requestId": payload.get("requestId"),
                                "expression": expression,
                                "result": evaluated.get("result", ""),
                                "typeName": evaluated.get("type", ""),
                                "variablesReference": evaluated.get("variablesReference", 0),
                            })
                        except DAPError as exc:
                            await send({
                                "type": "watchResult",
                                "requestId": payload.get("requestId"),
                                "expression": expression,
                                "error": str(exc),
                            })
                elif command == "stop":
                    await dap.request("disconnect", {"terminateDebuggee": True})
                    break
            except DAPError as exc:
                await send({
                    "type": "error",
                    "phase": str(command or "command"),
                    "message": "Debugger command failed.",
                    "detail": str(exc),
                })
    except WebSocketDisconnect:
        pass
    finally:
        if relay_task:
            relay_task.cancel()
        await dap.stop()
        if prepared_session is not None:
            prepared_session.cleanup()


def _prepare_debug_session(payload: dict[str, Any], language: SupportedLanguage) -> PreparedDebugSession:
    challenge_id = str(payload.get("challengeId") or "")
    solution_path = _solution_path(challenge_id, language)
    if not solution_path.is_file():
        raise DebugPreparationError(f"Solution file not found: {solution_path}")
    context = _debug_session_context(payload, language, solution_path)
    if language == "python":
        prepared = _prepare_python_debug_session(payload, solution_path)
    elif language == "cpp":
        prepared = _prepare_cpp_debug_session(payload, solution_path)
    elif language == "java":
        prepared = _prepare_java_debug_session(payload, solution_path)
    elif language == "csharp":
        prepared = _prepare_csharp_debug_session(payload, solution_path)
    elif language == "javascript":
        prepared = _prepare_javascript_debug_session(payload, solution_path)
    elif language == "go":
        prepared = _prepare_go_debug_session(payload, solution_path)
    elif language == "kotlin":
        prepared = _prepare_kotlin_debug_session(payload, solution_path)
    else:
        raise DebugPreparationError(f"{_DEBUG_LABELS[language]} debug launch is not wired yet.")
    prepared.context = context
    prepared.context["adapter"] = prepared.adapter_executable
    prepared.context["breakpointPath"] = str(prepared.breakpoint_path)
    return prepared


def _debug_session_context(
    payload: dict[str, Any],
    language: SupportedLanguage,
    solution_path: Path,
) -> dict[str, Any]:
    challenge_id = str(payload.get("challengeId") or "")
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise DebugPreparationError(f"Unknown challenge: {challenge_id}")

    mode = str(payload.get("mode") or "practice")
    challenge, setup_data, _expected_output, selected_case_ids = _debug_validated_setup(
        payload,
        challenge_id,
        mode=mode,
    )
    return {
        "challengeId": challenge_id,
        "challengeName": challenge.info.name,
        "language": language,
        "languageLabel": _DEBUG_LABELS[language],
        "mode": mode,
        "selectedCaseIds": selected_case_ids,
        "solutionPath": str(solution_path),
        "inputs": {
            key: _format_debug_value(value)
            for key, value in setup_data.items()
        },
    }


def _debug_case_ids(payload: dict[str, Any]) -> list[str]:
    raw = payload.get("caseIds") or payload.get("case_ids") or []
    if isinstance(raw, list):
        return [str(item) for item in raw if str(item)]
    if isinstance(raw, str) and raw:
        return [raw]
    return []


def _debug_custom_input(payload: dict[str, Any]) -> dict[str, Any] | None:
    raw = payload.get("customInput")
    if raw is None:
        raw = payload.get("custom_input")
    return raw if isinstance(raw, dict) else None


def _debug_validated_setup(
    payload: dict[str, Any],
    challenge_id: str,
    *,
    mode: str,
) -> tuple[Any, dict[str, Any], Any, list[str]]:
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise DebugPreparationError(f"Unknown challenge: {challenge_id}")
    if mode != "practice":
        raise DebugPreparationError(
            "Debug requires one visible or custom case; Run handles hidden real-test cases."
        )
    requested_case_ids = _debug_case_ids(payload)
    if len(requested_case_ids) > 1 or "__all_trial__" in requested_case_ids:
        raise DebugPreparationError("Debug accepts exactly one selected case, not Run All.")
    try:
        run_cases, _benchmark_cases = select_cases_for_run(
            challenge_id,
            mode=mode,
            selected_case_ids=requested_case_ids,
            custom_input=_debug_custom_input(payload),
        )
    except InvalidCustomCase as exc:
        raise DebugPreparationError(str(exc)) from exc
    except NoValidatedCases as exc:
        raise DebugPreparationError(str(exc)) from exc
    if not run_cases:
        raise DebugPreparationError(f"{challenge_id} has no authored validated case to debug.")
    selected_case = run_cases[0]
    return challenge_cls(), selected_case.input, selected_case.expected, [selected_case.id]


def _prepare_python_debug_session(payload: dict[str, Any], solution_path: Path) -> PreparedDebugSession:
    python_exe = _debug_python_exe()
    project_path = _project_path()
    runner = _runner_path()
    if not runner.is_file():
        raise DebugPreparationError(f"Debug runner not found: {runner}")

    env = _debug_env(project_path)
    challenge_id = str(payload.get("challengeId") or "")
    launch_args = [
        challenge_id,
        "--mode",
        str(payload.get("mode") or "practice"),
        "--no-hold",
    ]
    for case_id in _debug_case_ids(payload):
        launch_args.extend(["--case-id", case_id])
    custom_input = _debug_custom_input(payload)
    if custom_input is not None:
        launch_args.extend(["--custom-input-json", json.dumps(custom_input)])

    return PreparedDebugSession(
        adapter_executable=python_exe,
        adapter_args=["-m", "debugpy.adapter"],
        adapter_id="debugpy",
        cwd=str(project_path),
        env=env,
        launch_config={
            "name": "cOde(n) Python debug",
            "type": "python",
            "request": "launch",
            "program": str(runner),
            "python": [python_exe],
            "debugLauncherPython": python_exe,
            "cwd": str(project_path),
            "args": launch_args,
            "env": env,
            "console": "internalConsole",
            "justMyCode": False,
            "stopOnEntry": False,
        },
        breakpoint_path=solution_path,
    )


def _prepare_cpp_debug_session(payload: dict[str, Any], solution_path: Path) -> PreparedDebugSession:
    adapter = _first_tool("lldb-dap", "lldb-vscode")
    if adapter is None:
        raise DebugPreparationError("C++ debugger is not ready: missing lldb-dap or lldb-vscode.")
    compiler = _first_tool("g++", "clang++")
    if compiler is None:
        raise DebugPreparationError("C++ debugger is not ready: missing g++ or clang++.")

    tempdir = tempfile.TemporaryDirectory(prefix="coden-cpp-debug-")
    workdir = Path(tempdir.name)
    env = os.environ.copy()

    try:
        exe_path = _build_cpp_debug_target(
            compiler=compiler,
            workdir=workdir,
            solution_path=solution_path,
            payload=payload,
        )
    except Exception:
        tempdir.cleanup()
        raise

    return PreparedDebugSession(
        adapter_executable=adapter,
        adapter_args=[],
        adapter_id="lldb-dap",
        cwd=str(workdir),
        env=env,
        launch_config={
            "name": "cOde(n) C++ debug",
            "type": "lldb-dap",
            "request": "launch",
            "program": str(exe_path),
            "args": [],
            "cwd": str(workdir),
            "env": env,
            "stopOnEntry": False,
        },
        breakpoint_path=solution_path,
        tempdir=tempdir,
    )


def _prepare_java_debug_session(payload: dict[str, Any], solution_path: Path) -> PreparedDebugSession:
    javac = _first_tool("javac")
    java = _first_tool("java")
    if javac is None or java is None:
        raise DebugPreparationError("Java debugger is not ready: missing javac and java.")
    adapter_path = _java_debug_adapter_path()
    if adapter_path is None:
        raise DebugPreparationError("Java debugger is not ready: missing Java debug adapter.")
    adapter_executable, adapter_args = _java_debug_adapter_invocation(adapter_path, java)

    tempdir = tempfile.TemporaryDirectory(prefix="coden-java-debug-")
    workdir = Path(tempdir.name)
    env = os.environ.copy()

    try:
        target = _build_java_debug_target(
            javac=javac,
            workdir=workdir,
            solution_path=solution_path,
            payload=payload,
        )
    except Exception:
        tempdir.cleanup()
        raise

    return PreparedDebugSession(
        adapter_executable=adapter_executable,
        adapter_args=adapter_args,
        adapter_id="java-debug",
        cwd=str(workdir),
        env=env,
        launch_config={
            "name": "cOde(n) Java debug",
            "type": "java",
            "request": "launch",
            "mainClass": target.main_class,
            "classPaths": [str(target.classpath)],
            "modulePaths": [],
            "args": [],
            "cwd": str(workdir),
            "env": env,
            "console": "internalConsole",
            "stopOnEntry": False,
        },
        breakpoint_path=target.source_path,
        tempdir=tempdir,
    )


def _prepare_csharp_debug_session(payload: dict[str, Any], solution_path: Path) -> PreparedDebugSession:
    dotnet = _first_tool("dotnet")
    if dotnet is None:
        raise DebugPreparationError("C# debugger is not ready: missing dotnet SDK.")
    netcoredbg = _first_tool("netcoredbg")
    if netcoredbg is None:
        raise DebugPreparationError("C# debugger is not ready: missing netcoredbg.")

    tempdir = tempfile.TemporaryDirectory(prefix="coden-csharp-debug-")
    workdir = Path(tempdir.name)
    env = os.environ.copy()
    env["DOTNET_CLI_TELEMETRY_OPTOUT"] = "1"
    env["DOTNET_NOLOGO"] = "1"

    try:
        dll_path = _build_csharp_debug_target(
            dotnet=dotnet,
            workdir=workdir,
            solution_path=solution_path,
            payload=payload,
            env=env,
        )
    except Exception:
        tempdir.cleanup()
        raise

    return PreparedDebugSession(
        adapter_executable=netcoredbg,
        adapter_args=["--interpreter=vscode"],
        adapter_id="coreclr",
        cwd=str(workdir),
        env=env,
        launch_config={
            "name": "cOde(n) C# debug",
            "type": "coreclr",
            "request": "launch",
            "program": str(dll_path),
            "args": [],
            "cwd": str(workdir),
            "env": env,
            "console": "internalConsole",
            "stopAtEntry": False,
        },
        breakpoint_path=solution_path,
        tempdir=tempdir,
    )


def _prepare_go_debug_session(payload: dict[str, Any], solution_path: Path) -> PreparedDebugSession:
    dlv = _first_tool("dlv")
    if dlv is None:
        raise DebugPreparationError("Go debugger is not ready: missing delve/dlv.")
    go = _first_tool("go")
    if go is None:
        raise DebugPreparationError("Go debugger is not ready: missing Go toolchain.")

    tempdir = tempfile.TemporaryDirectory(prefix="coden-go-debug-")
    workdir = Path(tempdir.name)
    env = os.environ.copy()
    env["GOCACHE"] = str(workdir / "gocache")

    try:
        exe_path = _build_go_debug_target(
            go=go,
            workdir=workdir,
            solution_path=solution_path,
            payload=payload,
            env=env,
        )
        port = _free_tcp_port()
    except Exception:
        tempdir.cleanup()
        raise

    host = "127.0.0.1"
    return PreparedDebugSession(
        adapter_executable=dlv,
        adapter_args=["dap", "--listen", f"{host}:{port}"],
        adapter_id="delve-dap",
        cwd=str(workdir),
        env=env,
        launch_config={
            "name": "cOde(n) Go debug",
            "type": "go",
            "request": "launch",
            "mode": "exec",
            "program": str(exe_path),
            "args": [],
            "cwd": str(workdir),
            "env": env,
            "stopOnEntry": False,
        },
        breakpoint_path=solution_path,
        adapter_connect_host=host,
        adapter_connect_port=port,
        tempdir=tempdir,
    )


def _prepare_javascript_debug_session(payload: dict[str, Any], solution_path: Path) -> PreparedDebugSession:
    node = _first_tool("node")
    if node is None:
        raise DebugPreparationError("JavaScript debugger is not ready: missing Node.js.")
    adapter_path = _js_debug_adapter_path()
    if adapter_path is None:
        raise DebugPreparationError("JavaScript debugger is not ready: missing JavaScript debug adapter.")
    adapter_executable, adapter_args = _js_debug_adapter_invocation(adapter_path, node)

    tempdir = tempfile.TemporaryDirectory(prefix="coden-js-debug-")
    workdir = Path(tempdir.name)
    env = os.environ.copy()

    try:
        program_path = _build_javascript_debug_target(
            workdir=workdir,
            solution_path=solution_path,
            payload=payload,
        )
    except Exception:
        tempdir.cleanup()
        raise

    return PreparedDebugSession(
        adapter_executable=adapter_executable,
        adapter_args=adapter_args,
        adapter_id="js-debug",
        cwd=str(workdir),
        env=env,
        launch_config={
            "name": "cOde(n) JavaScript debug",
            "type": "pwa-node",
            "request": "launch",
            "runtimeExecutable": node,
            "program": str(program_path),
            "args": [],
            "cwd": str(workdir),
            "env": env,
            "console": "internalConsole",
            "stopOnEntry": False,
        },
        breakpoint_path=solution_path,
        tempdir=tempdir,
    )


def _prepare_kotlin_debug_session(payload: dict[str, Any], solution_path: Path) -> PreparedDebugSession:
    kotlinc = _first_tool("kotlinc")
    java = _first_tool("java")
    if kotlinc is None or java is None:
        raise DebugPreparationError("Kotlin debugger is not ready: missing kotlinc and java.")
    adapter_path = _java_debug_adapter_path()
    if adapter_path is None:
        raise DebugPreparationError("Kotlin debugger is not ready: missing Java/Kotlin debug adapter.")
    adapter_executable, adapter_args = _java_debug_adapter_invocation(adapter_path, java)

    tempdir = tempfile.TemporaryDirectory(prefix="coden-kotlin-debug-")
    workdir = Path(tempdir.name)
    env = os.environ.copy()

    try:
        target = _build_kotlin_debug_target(
            kotlinc=kotlinc,
            workdir=workdir,
            solution_path=solution_path,
            payload=payload,
        )
    except Exception:
        tempdir.cleanup()
        raise

    return PreparedDebugSession(
        adapter_executable=adapter_executable,
        adapter_args=adapter_args,
        adapter_id="java-debug",
        cwd=str(workdir),
        env=env,
        launch_config={
            "name": "cOde(n) Kotlin debug",
            "type": "java",
            "request": "launch",
            "mainClass": target.main_class,
            "classPaths": [str(target.classpath)],
            "modulePaths": [],
            "args": [],
            "cwd": str(workdir),
            "env": env,
            "console": "internalConsole",
            "stopOnEntry": False,
        },
        breakpoint_path=target.source_path,
        tempdir=tempdir,
    )


def _debug_env(project_path: Path) -> dict[str, str]:
    env = os.environ.copy()
    for key in list(env):
        if key.upper() == "PYTHONHOME":
            env.pop(key, None)
    env["CODEN_HOME"] = str(CODEN_HOME)
    existing_pythonpath = "" if _is_packaged_server() else env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = os.pathsep.join(
        p for p in [str(project_path), existing_pythonpath] if p
    )
    return env


def _build_cpp_debug_target(
    *,
    compiler: str,
    workdir: Path,
    solution_path: Path,
    payload: dict[str, Any],
) -> Path:
    challenge_id = str(payload.get("challengeId") or "")
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise DebugPreparationError(f"Unknown challenge: {challenge_id}")

    challenge, setup_data, _expected_output, _selected_case_ids = _debug_validated_setup(
        payload,
        challenge_id,
        mode=str(payload.get("mode") or "practice"),
    )

    user_source = solution_path.read_text(encoding="utf-8")
    spec = getattr(challenge, "_spec", None)
    param_names = list(getattr(spec, "params", []) or setup_data.keys())
    param_hints = dict(getattr(spec, "inputs", {}) or {})
    returns_hint = str(getattr(spec, "returns", "") or "")
    source = _cpp_function_debug_source(
        solution_path,
        user_source,
        param_names,
        param_hints,
        returns_hint,
        json.dumps(setup_data),
        setup_data,
    )

    source_path = workdir / "main.cpp"
    exe_path = workdir / ("main.exe" if os.name == "nt" else "main")
    source_path.write_text(source, encoding="utf-8")

    build_result = _run_process(
        [compiler, "-std=c++17", "-O0", "-g", str(source_path), "-o", str(exe_path)],
        cwd=workdir,
        timeout_seconds=60.0,
    )
    if build_result.returncode != 0:
        raise DebugPreparationError(
            _short_message("C++ debug build failed", build_result.stderr or build_result.stdout)
        )
    if not exe_path.is_file():
        raise DebugPreparationError(f"C++ debug build did not produce {exe_path}")
    return exe_path


def _cpp_function_debug_source(
    solution_path: Path,
    user_source: str,
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    input_json: str,
    param_values: dict[str, object] | None = None,
) -> str:
    return (
        "#include <bits/stdc++.h>\n"
        "using namespace std;\n\n"
        f"{_cpp_line_directive(solution_path)}"
        f"{user_source.rstrip()}\n\n"
        '#line 1 "CodenCppDebugHarness.cpp"\n'
        + _cpp_function_harness(
            param_names,
            param_hints,
            returns_hint,
            input_json=input_json,
            param_values=param_values,
        )
    )


def _cpp_line_directive(path: Path) -> str:
    source_path = str(path).replace("\\", "/")
    return f"#line 1 {json.dumps(source_path)}\n"


def _build_java_debug_target(
    *,
    javac: str,
    workdir: Path,
    solution_path: Path,
    payload: dict[str, Any],
) -> JavaDebugTarget:
    challenge_id = str(payload.get("challengeId") or "")
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise DebugPreparationError(f"Unknown challenge: {challenge_id}")

    challenge, setup_data, _expected_output, _selected_case_ids = _debug_validated_setup(
        payload,
        challenge_id,
        mode=str(payload.get("mode") or "practice"),
    )

    main_class = "Main"
    user_source_path = workdir / "Solution.java"
    user_source_path.write_text(solution_path.read_text(encoding="utf-8"), encoding="utf-8")
    spec = getattr(challenge, "_spec", None)
    param_names = list(getattr(spec, "params", []) or setup_data.keys())
    param_hints = dict(getattr(spec, "inputs", {}) or {})
    returns_hint = str(getattr(spec, "returns", "") or "")
    harness_path = workdir / "Main.java"
    harness_path.write_text(
        _java_function_harness(
            param_names,
            param_hints,
            returns_hint,
            input_json=json.dumps(setup_data),
            param_values=setup_data,
        ),
        encoding="utf-8",
    )

    build_result = _run_process(
        [javac, "-g", "-d", str(workdir), str(user_source_path), str(harness_path)],
        cwd=workdir,
        timeout_seconds=60.0,
    )
    if build_result.returncode != 0:
        raise DebugPreparationError(
            _short_message("Java debug build failed", build_result.stderr or build_result.stdout)
        )

    class_path = workdir / f"{main_class}.class"
    if not class_path.is_file():
        raise DebugPreparationError(f"Java debug build did not produce {class_path}")
    return JavaDebugTarget(main_class=main_class, classpath=workdir, source_path=user_source_path)


def _java_debug_adapter_invocation(adapter_path: str, java: str) -> tuple[str, list[str]]:
    adapter = Path(adapter_path)
    if adapter.suffix.lower() == ".jar":
        return java, ["-jar", str(adapter)]
    return str(adapter), []


def _js_debug_adapter_invocation(adapter_path: str, node: str) -> tuple[str, list[str]]:
    adapter = Path(adapter_path)
    if adapter.suffix.lower() == ".js":
        return node, [str(adapter)]
    return str(adapter), []


def _build_csharp_debug_target(
    *,
    dotnet: str,
    workdir: Path,
    solution_path: Path,
    payload: dict[str, Any],
    env: dict[str, str],
) -> Path:
    challenge_id = str(payload.get("challengeId") or "")
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise DebugPreparationError(f"Unknown challenge: {challenge_id}")

    project_path = workdir / "CodenDebug.csproj"
    startup_object = "Program"
    target_framework = _dotnet_target_framework(dotnet)
    project_path.write_text(
        _csharp_debug_project(target_framework, solution_path, startup_object),
        encoding="utf-8",
    )

    challenge, setup_data, _expected_output, _selected_case_ids = _debug_validated_setup(
        payload,
        challenge_id,
        mode=str(payload.get("mode") or "practice"),
    )

    spec = getattr(challenge, "_spec", None)
    param_names = list(getattr(spec, "params", []) or setup_data.keys())
    param_hints = dict(getattr(spec, "inputs", {}) or {})
    returns_hint = str(getattr(spec, "returns", "") or "")
    harness_source = _csharp_function_harness(
        param_names,
        param_hints,
        returns_hint,
        input_json=json.dumps(setup_data),
        param_values=setup_data,
    )

    (workdir / "Program.cs").write_text(
        harness_source,
        encoding="utf-8",
    )

    build_result = _run_process(
        [dotnet, "build", str(project_path), "-c", "Debug", "-nologo", "-v:q"],
        cwd=workdir,
        timeout_seconds=60.0,
        env=env,
    )
    if build_result.returncode != 0:
        raise DebugPreparationError(
            _short_message("C# debug build failed", build_result.stderr or build_result.stdout)
        )

    dll_path = workdir / "bin" / "Debug" / target_framework / "CodenDebug.dll"
    if not dll_path.is_file():
        raise DebugPreparationError(f"C# debug build did not produce {dll_path}")
    return dll_path


def _build_go_debug_target(
    *,
    go: str,
    workdir: Path,
    solution_path: Path,
    payload: dict[str, Any],
    env: dict[str, str],
) -> Path:
    challenge_id = str(payload.get("challengeId") or "")
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise DebugPreparationError(f"Unknown challenge: {challenge_id}")

    challenge, setup_data, _expected_output, _selected_case_ids = _debug_validated_setup(
        payload,
        challenge_id,
        mode=str(payload.get("mode") or "practice"),
    )

    user_source = solution_path.read_text(encoding="utf-8")
    solution_source_path = workdir / "solution.go"
    harness_path = workdir / "coden_harness.go"
    spec = getattr(challenge, "_spec", None)
    param_names = list(getattr(spec, "params", []) or setup_data.keys())
    param_hints = dict(getattr(spec, "inputs", {}) or {})
    returns_hint = str(getattr(spec, "returns", "") or "")
    solution_source_path.write_text(
        _go_user_source_with_line_directive(user_source, solution_path),
        encoding="utf-8",
    )
    harness_path.write_text(
        _go_function_harness(
            param_names,
            param_hints,
            returns_hint,
            input_json=json.dumps(setup_data),
            param_values=setup_data,
        ),
        encoding="utf-8",
    )

    exe_path = workdir / ("main.exe" if os.name == "nt" else "main")
    build_result = _run_process(
        [
            go,
            "build",
            "-gcflags=all=-N -l",
            "-o",
            str(exe_path),
            str(solution_source_path),
            str(harness_path),
        ],
        cwd=workdir,
        timeout_seconds=60.0,
        env=env,
    )
    if build_result.returncode != 0:
        raise DebugPreparationError(
            _short_message("Go debug build failed", build_result.stderr or build_result.stdout)
        )
    if not exe_path.is_file():
        raise DebugPreparationError(f"Go debug build did not produce {exe_path}")
    return exe_path


def _build_javascript_debug_target(
    *,
    workdir: Path,
    solution_path: Path,
    payload: dict[str, Any],
) -> Path:
    challenge_id = str(payload.get("challengeId") or "")
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise DebugPreparationError(f"Unknown challenge: {challenge_id}")

    challenge, setup_data, _expected_output, _selected_case_ids = _debug_validated_setup(
        payload,
        challenge_id,
        mode=str(payload.get("mode") or "practice"),
    )

    spec = getattr(challenge, "_spec", None)
    param_names = list(getattr(spec, "params", []) or setup_data.keys())
    param_hints = dict(getattr(spec, "inputs", {}) or {})
    returns_hint = str(getattr(spec, "returns", "") or "")
    source = _javascript_function_debug_launcher(
        solution_path,
        param_names,
        param_hints,
        returns_hint,
        json.dumps(setup_data),
        setup_data,
    )

    launcher_path = workdir / "coden_js_debug_launcher.js"
    launcher_path.write_text(source, encoding="utf-8")
    return launcher_path


def _javascript_function_debug_launcher(
    solution_path: Path,
    param_names: list[str],
    param_hints: dict[str, str],
    returns_hint: str,
    input_json: str,
    param_values: dict[str, object] | None = None,
) -> str:
    combined_source = (
        solution_path.read_text(encoding="utf-8").rstrip()
        + "\n\n"
        + _javascript_function_harness(
            param_names,
            param_hints,
            returns_hint,
            input_json=input_json,
            param_values=param_values,
        )
    )
    return _javascript_vm_launcher(solution_path, combined_source)


def _javascript_vm_launcher(solution_path: Path, source: str) -> str:
    return (
        "const __codenVm = require(\"vm\");\n"
        "global.require = require;\n"
        "global.process = process;\n"
        "global.console = console;\n"
        "global.Buffer = Buffer;\n"
        f"__codenVm.runInThisContext({json.dumps(source)}, {{ filename: {json.dumps(str(solution_path))}, displayErrors: true }});\n"
    )


def _go_user_source_with_line_directive(user_source: str, solution_path: Path) -> str:
    source_path = str(solution_path).replace("\\", "/")
    return f"//line {source_path}:1\n{user_source.rstrip()}\n"


def _free_tcp_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def _build_kotlin_debug_target(
    *,
    kotlinc: str,
    workdir: Path,
    solution_path: Path,
    payload: dict[str, Any],
) -> JavaDebugTarget:
    challenge_id = str(payload.get("challengeId") or "")
    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        raise DebugPreparationError(f"Unknown challenge: {challenge_id}")

    challenge, setup_data, _expected_output, _selected_case_ids = _debug_validated_setup(
        payload,
        challenge_id,
        mode=str(payload.get("mode") or "practice"),
    )

    user_source_path = solution_path
    spec = getattr(challenge, "_spec", None)
    param_names = list(getattr(spec, "params", []) or setup_data.keys())
    param_hints = dict(getattr(spec, "inputs", {}) or {})
    returns_hint = str(getattr(spec, "returns", "") or "")
    harness_path = workdir / "CodenHarness.kt"
    harness_path.write_text(
        _kotlin_function_harness(
            param_names,
            param_hints,
            returns_hint,
            input_json=json.dumps(setup_data),
            param_values=setup_data,
        ),
        encoding="utf-8",
    )
    main_class = "CodenHarnessKt"
    source_path = solution_path

    jar_path = workdir / "coden-kotlin-debug.jar"
    build_result = _run_process(
        [kotlinc, str(user_source_path), str(harness_path), "-include-runtime", "-d", str(jar_path)],
        cwd=workdir,
        timeout_seconds=60.0,
    )
    if build_result.returncode != 0:
        raise DebugPreparationError(
            _short_message("Kotlin debug build failed", build_result.stderr or build_result.stdout)
        )
    if not jar_path.is_file():
        raise DebugPreparationError(f"Kotlin debug build did not produce {jar_path}")
    return JavaDebugTarget(main_class=main_class, classpath=jar_path, source_path=source_path)


def _csharp_debug_project(target_framework: str, solution_path: Path, startup_object: str) -> str:
    return (
        '<Project Sdk="Microsoft.NET.Sdk">\n'
        "  <PropertyGroup>\n"
        "    <OutputType>Exe</OutputType>\n"
        f"    <TargetFramework>{xml_escape(target_framework)}</TargetFramework>\n"
        "    <ImplicitUsings>enable</ImplicitUsings>\n"
        "    <Nullable>disable</Nullable>\n"
        "    <DebugType>portable</DebugType>\n"
        "    <DebugSymbols>true</DebugSymbols>\n"
        f"    <StartupObject>{xml_escape(startup_object)}</StartupObject>\n"
        "  </PropertyGroup>\n"
        "  <ItemGroup>\n"
        f'    <Compile Include="{xml_escape(str(solution_path))}" Link="Solution.cs" />\n'
        "  </ItemGroup>\n"
        "</Project>\n"
    )


async def _set_breakpoints(dap: DAPClient, path: Path, raw_breakpoints: Any) -> list[dict[str, Any]]:
    breakpoints = raw_breakpoints if isinstance(raw_breakpoints, list) else []
    lines = sorted({int(line) for line in breakpoints if isinstance(line, int) and line > 0})
    response = await dap.request(
        "setBreakpoints",
        {
            "source": {"path": str(path)},
            "breakpoints": [{"line": line} for line in lines],
            "sourceModified": False,
        },
    )
    received = response.get("breakpoints") if isinstance(response.get("breakpoints"), list) else []
    result: list[dict[str, Any]] = []
    for index, line in enumerate(lines):
        breakpoint = received[index] if index < len(received) and isinstance(received[index], dict) else {}
        result.append({
            "line": breakpoint.get("line", line),
            "requestedLine": line,
            "verified": bool(breakpoint.get("verified", False)),
            "message": breakpoint.get("message", ""),
            "id": breakpoint.get("id"),
        })
    return result


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
            try:
                await send(await _paused_payload(dap, body))
            except Exception as exc:
                await send({
                    "type": "error",
                    "phase": "pause",
                    "message": "Debugger paused, but locals/stack could not be read.",
                    "detail": _exception_detail(exc),
                })
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
    frame_state = await _frame_payload(dap, _as_int(top.get("id"), 0)) if top.get("id") is not None else {
        "frameId": None, "locals": [], "scopes": []
    }
    exception_info: dict[str, Any] | None = None
    if str(body.get("reason", "")).lower() == "exception":
        try:
            info = await dap.request("exceptionInfo", {"threadId": thread_id})
            exception_info = {
                "exceptionId": info.get("exceptionId"),
                "description": info.get("description"),
                "breakMode": info.get("breakMode"),
                "details": info.get("details"),
            }
        except Exception:
            exception_info = None
    return {
        "type": "stopped",
        "reason": body.get("reason", "pause"),
        "description": body.get("description"),
        "text": body.get("text"),
        "threadId": thread_id,
        "line": top.get("line"),
        "column": top.get("column"),
        "path": (top.get("source") or {}).get("path") if isinstance(top.get("source"), dict) else None,
        "frameId": top.get("id"),
        "frames": [
            _stack_frame_payload(
                frame,
                (top.get("source") or {}).get("path") if isinstance(top.get("source"), dict) else None,
            )
            for frame in frames if isinstance(frame, dict)
        ],
        "locals": frame_state["locals"],
        "scopes": frame_state["scopes"],
        "exception": exception_info,
    }


async def _frame_payload(dap: DAPClient, frame_id: int) -> dict[str, Any]:
    scopes_body = await dap.request("scopes", {"frameId": frame_id})
    scopes = scopes_body.get("scopes") if isinstance(scopes_body.get("scopes"), list) else []
    locals_out: list[dict[str, Any]] = []
    scope_payloads: list[dict[str, Any]] = []
    for scope in scopes:
        if not isinstance(scope, dict):
            continue
        variables_reference = _as_int(scope.get("variablesReference"), 0)
        scope_payloads.append({
            "name": scope.get("name", ""),
            "variablesReference": variables_reference,
            "expensive": bool(scope.get("expensive", False)),
        })
        if str(scope.get("name", "")).lower() not in {"locals", "arguments"} or not variables_reference:
            continue
        variables = await dap.request("variables", {"variablesReference": variables_reference})
        for variable in variables.get("variables", []) if isinstance(variables.get("variables"), list) else []:
            if isinstance(variable, dict) and _is_user_relevant_debug_variable(variable):
                locals_out.append(_debug_variable_payload(variable))
    return {"frameId": frame_id, "locals": locals_out, "scopes": scope_payloads}


def _debug_variable_payload(variable: dict[str, Any]) -> dict[str, Any]:
    return {
        "name": variable.get("name", ""),
        "value": variable.get("value", ""),
        "type": variable.get("type", ""),
        "variablesReference": _as_int(variable.get("variablesReference"), 0),
        "evaluateName": variable.get("evaluateName", ""),
        "indexedVariables": variable.get("indexedVariables"),
        "namedVariables": variable.get("namedVariables"),
    }


def _stack_frame_payload(frame: dict[str, Any], user_path: Any = None) -> dict[str, Any]:
    source = frame.get("source") if isinstance(frame.get("source"), dict) else {}
    path = source.get("path")
    return {
        "id": frame.get("id"),
        "name": frame.get("name", ""),
        "line": frame.get("line"),
        "column": frame.get("column"),
        "path": path,
        "sourceName": source.get("name"),
        "userCode": bool(path and user_path and _same_debug_path(path, user_path)),
    }


def _same_debug_path(left: Any, right: Any) -> bool:
    try:
        return Path(str(left)).resolve() == Path(str(right)).resolve()
    except OSError:
        return os.path.normcase(str(left)) == os.path.normcase(str(right))


def _debug_start_error(exc: Exception, language: SupportedLanguage, adapter_executable: str) -> str:
    message = str(exc)
    if language == "python" and ("No module named debugpy" in message or "debug adapter exited" in message):
        if _is_packaged_server():
            return (
                f"Could not start the bundled debugger with {adapter_executable}. "
                "Rebuild the Windows app so resources/debug-python contains "
                "python.exe and debugpy."
            )
        return (
            f"Could not start debugpy with {adapter_executable}. Install debugpy in that Python "
            "environment (`python -m pip install debugpy`) and try again."
        )
    if "debug adapter exited" in message:
        label = _DEBUG_LABELS[language]
        return f"Could not start the {label} debugger with {adapter_executable}: {message}"
    return message


_DEBUG_LOCAL_NAME_BLOCKLIST = {
    "__builtins__",
    "__cached__",
    "__doc__",
    "__file__",
    "__loader__",
    "__name__",
    "__package__",
    "__spec__",
    "argparse",
    "asyncio",
    "challenge",
    "challenge_cls",
    "json",
    "namespace",
    "os",
    "parser",
    "project_path",
    "ref_result",
    "ref_setup_data",
    "run_player_code",
    "runpy",
    "setup_data",
    "source_path",
    "sys",
    "trace",
}


_DEBUG_LOCAL_VALUE_PREFIX_BLOCKLIST = (
    "<built-in function",
    "<bound method",
    "<class ",
    "<code object ",
    "<function ",
    "<module ",
    "<staticmethod",
    "<classmethod",
    "module ",
)


_DEBUG_LOCAL_TYPE_BLOCKLIST = {
    "ABCMeta",
    "ModuleSpec",
    "TextIOWrapper",
    "builtin_function_or_method",
    "classmethod",
    "code",
    "function",
    "frame",
    "module",
    "staticmethod",
    "traceback",
    "type",
}

_DEBUG_LOCAL_TYPE_BLOCKLIST_LOWER = {
    item.lower()
    for item in _DEBUG_LOCAL_TYPE_BLOCKLIST
}


def _is_user_relevant_debug_variable(variable: dict[str, Any]) -> bool:
    name = str(variable.get("name") or "")
    if not name or name in _DEBUG_LOCAL_NAME_BLOCKLIST:
        return False
    if name.startswith("__") or name.startswith("_"):
        return False

    value = str(variable.get("value") or "").strip()
    lowered_type = str(variable.get("type") or "").strip().lower()
    if lowered_type in _DEBUG_LOCAL_TYPE_BLOCKLIST_LOWER:
        return False
    if any(value.startswith(prefix) for prefix in _DEBUG_LOCAL_VALUE_PREFIX_BLOCKLIST):
        return False

    hint = variable.get("presentationHint")
    if isinstance(hint, dict):
        kind = str(hint.get("kind") or "").lower()
        if kind in {"method", "function", "class", "virtual"}:
            return False
        attributes = hint.get("attributes")
        if isinstance(attributes, list) and "readOnly" in attributes and value.startswith("<"):
            return False

    return True


def _short_message(prefix: str, detail: str) -> str:
    detail = detail.strip()
    if not detail:
        return prefix
    if len(detail) > 1200:
        detail = detail[:1200] + "..."
    return f"{prefix}: {detail}"


def _exception_detail(exc: BaseException) -> str:
    text = "".join(traceback.format_exception_only(type(exc), exc)).strip()
    if not text:
        text = str(exc)
    if len(text) > 2000:
        text = text[:2000] + "..."
    return text


def _format_debug_value(value: Any) -> str:
    try:
        from server.app.engine_runner import _format_return_value

        return _format_return_value(value)
    except Exception:
        text = repr(value)
        return text[:500] + "..." if len(text) > 500 else text
