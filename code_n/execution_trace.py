"""Execution tracing for player solutions.

Captures local variable snapshots from the player's solve function so the
Pygame renderer can behave like a lightweight algorithm debugger.
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

from .counter import OperationCounter


@dataclass
class TraceFrame:
    op_index: int
    line_no: int
    event: str
    locals: dict[str, str] = field(default_factory=dict)
    return_value: str = ""
    breakpoint: bool = False


@dataclass
class ExecutionTrace:
    frames: list[TraceFrame] = field(default_factory=list)
    return_value: str = ""

    def latest_at(self, op_index: int) -> TraceFrame | None:
        latest: TraceFrame | None = None
        for frame in self.frames:
            if frame.op_index <= op_index:
                latest = frame
            else:
                break
        return latest


class ExecutionStepLimitExceeded(RuntimeError):
    """Raised when player code runs too many Python steps without finishing."""

    def __init__(self, steps: int, limit: int):
        self.steps = steps
        self.limit = limit
        super().__init__(
            f"Stopped: ran {steps} Python steps without finishing. Check for an accidental infinite loop or an algorithm that is far too slow."
        )


def run_with_trace(func: Callable, kwargs: dict[str, Any], counter: OperationCounter,
                   count_lines: bool = False,
                   step_limit: Optional[int] = None,
                   step_callback: Optional[Callable[[int], None]] = None,
                   step_interval: int = 1000) -> tuple[Any, ExecutionTrace]:
    """Run a player's function and capture local variables from their script file."""
    trace = ExecutionTrace()
    target_file = os.path.normcase(os.path.abspath(func.__code__.co_filename))
    breakpoint_lines = _load_inline_breakpoints(target_file)
    previous_tracer = sys.gettrace()
    step_count = 0
    last_step_update = 0

    def tracer(frame, event, arg):
        nonlocal step_count, last_step_update
        frame_file = os.path.normcase(os.path.abspath(frame.f_code.co_filename))
        if frame_file == target_file and event in {"line", "return"}:
            if count_lines and event == "line":
                counter.call(f"line {frame.f_lineno}")
            if event == "line":
                step_count += 1
                if step_callback and step_count - last_step_update >= max(1, step_interval):
                    last_step_update = step_count
                    step_callback(step_count)
                if step_limit is not None and step_count > step_limit:
                    raise ExecutionStepLimitExceeded(step_count, step_limit)
            return_value = _safe_repr(arg) if event == "return" else ""
            trace.frames.append(
                TraceFrame(
                    op_index=counter.total_ops,
                    line_no=frame.f_lineno,
                    event=event,
                    locals=_serialize_locals(frame.f_locals),
                    return_value=return_value,
                    breakpoint=frame.f_lineno in breakpoint_lines,
                )
            )
            if event == "return":
                trace.return_value = return_value
        return tracer

    sys.settrace(tracer)
    try:
        result = func(**kwargs)
        if not trace.return_value:
            trace.return_value = _safe_repr(result)
        return result, trace
    finally:
        sys.settrace(previous_tracer)


def _serialize_locals(locals_map: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for key, value in locals_map.items():
        if key.startswith("__"):
            continue
        result[key] = _safe_repr(value)
    return result


def _load_inline_breakpoints(path: str) -> set[int]:
    markers = ("code_n: breakpoint", "code_n breakpoint")
    breakpoints: set[int] = set()
    try:
        with open(path, "r", encoding="utf-8") as source_file:
            for line_no, line in enumerate(source_file, start=1):
                lowered = line.lower()
                if any(marker in lowered for marker in markers):
                    breakpoints.add(line_no)
    except OSError:
        pass
    return breakpoints


def _safe_repr(value: Any, max_len: int = 80) -> str:
    try:
        if hasattr(value, "raw"):
            text = repr(value.raw)
        elif isinstance(value, list):
            text = _repr_sequence(value, "[", "]")
        elif isinstance(value, tuple):
            text = _repr_sequence(list(value), "(", ")")
        elif isinstance(value, set):
            text = _repr_sequence(list(value), "{", "}")
        elif isinstance(value, dict):
            items = list(value.items())[:8]
            body = ", ".join(f"{_safe_repr(k, 20)}: {_safe_repr(v, 20)}" for k, v in items)
            suffix = ", ..." if len(value) > 8 else ""
            text = "{" + body + suffix + "}"
        else:
            text = repr(value)
    except Exception:
        text = f"<{type(value).__name__}>"

    if len(text) > max_len:
        return text[: max_len - 3] + "..."
    return text


def _repr_sequence(values: list[Any], start: str, end: str) -> str:
    visible = values[:10]
    body = ", ".join(_safe_repr(item, 20) for item in visible)
    if len(values) > len(visible):
        body += ", ..."
    return f"{start}{body}{end}"
