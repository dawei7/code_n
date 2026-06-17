"""Execution tracing for player solutions.

Captures local variable snapshots from the player's solve function so
the visualizer (the React/Electron frontend) can replay the
algorithm step by step.

The tracer uses Python's :func:`sys.settrace` to fire on every line
event in the player's file. Each event becomes one
:class:`TraceFrame`. The frame's ``frame_index`` is its position in
the trace's frame list — the visualizer slider drives off this
index directly.

The runtime op counter was removed in v0.8.5; this module no
longer needs it. ``frame_index`` replaces the old ``op_index``,
and the per-step "is this a real op?" question is no longer
asked — every line event is one step.
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from typing import Any, Callable, Optional


@dataclass
class TraceFrame:
    # The frame's own position in the trace's frame list. The
    # tracer sets it at capture time (``frame_index =
    # len(trace.frames)``) so the trace is already sorted by
    # this field and ``trace[frame_index]`` is O(1) for the
    # visualizer slider.
    frame_index: int
    line_no: int
    event: str
    # The actual Python locals from the player's frame, NOT
    # their repr. Storing the objects lets the renderer build a
    # fully-fleshed visual (one cell per list element, one row
    # per dict pair) rather than dumping a truncated string.
    locals: dict[str, Any] = field(default_factory=dict)
    return_value: str = ""
    breakpoint: bool = False
    # Path of the player's source file the frame was captured in.
    # Lets the renderer look up the matching source line so the
    # "Current op" panel can show the actual Python statement
    # (e.g. ``candies[i] = max(candies[i], candies[i+1] + 1)``)
    # alongside the op-level detail.
    source_file: str = ""


@dataclass
class ExecutionTrace:
    frames: list[TraceFrame] = field(default_factory=list)
    return_value: str = ""

    def latest_at(self, frame_index: int) -> TraceFrame | None:
        """Return the latest frame at or before ``frame_index``.

        Used by the visualizer when the slider is dragged: we
        want the snapshot of the locals at the latest step ≤
        the slider position. With ``frame_index`` being the
        frame's own list position, this is just
        ``trace.frames[min(frame_index, len(trace.frames) - 1)]``
        for any monotonic slider position.
        """
        if not self.frames:
            return None
        if frame_index >= self.frames[-1].frame_index:
            return self.frames[-1]
        for frame in self.frames:
            if frame.frame_index > frame_index:
                return self.frames[max(0, self.frames.index(frame) - 1)]
        return self.frames[-1]


class ExecutionStepLimitExceeded(RuntimeError):
    """Raised when player code runs too many Python steps without finishing."""

    def __init__(self, steps: int, limit: int):
        self.steps = steps
        self.limit = limit
        super().__init__(
            f"Stopped: ran {steps} Python steps without finishing. Check for an accidental infinite loop or an algorithm that is far too slow."
        )


def run_with_trace(func: Callable, kwargs: dict[str, Any],
                   step_limit: Optional[int] = None,
                   step_callback: Optional[Callable[[int], None]] = None,
                   step_interval: int = 1000) -> tuple[Any, ExecutionTrace]:
    """Run a player's function and capture local variables from their script file.

    Each Python line event in the player's file becomes one
    :class:`TraceFrame`. ``step_limit`` is a safety cap to
    catch infinite loops; it is independent of the
    complexity budget (the AST op counter handles the
    budget — see :mod:`server.app.ast_ops`).
    """
    trace = ExecutionTrace()
    target_file = os.path.normcase(os.path.abspath(func.__code__.co_filename))
    breakpoint_lines = _load_inline_breakpoints(target_file)
    previous_tracer = sys.gettrace()
    step_count = 0
    last_step_update = 0

    def tracer(frame, event, arg):
        nonlocal step_count, last_step_update
        frame_file = os.path.normcase(os.path.abspath(frame.f_code.co_filename))
        if frame_file == target_file and event in {"call", "line", "return"}:
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
                    frame_index=len(trace.frames),
                    line_no=frame.f_lineno,
                    event=event,
                    locals=_serialize_locals(frame.f_locals),
                    return_value=return_value,
                    breakpoint=frame.f_lineno in breakpoint_lines,
                    source_file=frame.f_code.co_filename,
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


def _serialize_locals(locals_map: dict[str, Any]) -> dict[str, Any]:
    """Return the locals as actual Python objects (not repr strings).

    The renderer can then build a fully-fleshed visual for each
    one: one cell per list element, one row per dict pair, etc.
    Previously the locals were pre-rendered to ``repr()`` strings
    which forced the renderer to dump truncated text.

    Mutable containers (list, set, dict) are shallow-copied so the
    snapshot is independent of the player's later mutations. The
    BFS Grid challenge is the canonical example: the BFS mutates
    ``frontier`` (plain list) and ``visited`` (plain set) in place
    across every iteration, and the tracer fires one line event
    per iteration. Without the copy, every captured frame shares
    the same list/set references as the live ones, and by the time
    the renderer reads the stored locals they all show the FINAL
    state of the BFS - the variable panel at step 0 would show
    ``frontier`` with the post-goal layer and ``visited`` with
    every cell the BFS touched, instead of the start state. The
    shallow copy freezes each container's contents at the moment
    of the line event so a frame captured at line 20 (just after
    ``frontier = []``) keeps ``frontier == []`` even after the
    rest of the BFS has run.
    """
    result: dict[str, Any] = {}
    for key, value in locals_map.items():
        if key.startswith("__"):
            continue
        # Snapshot mutable containers. Tuples and scalars are
        # immutable from the player's perspective and don't
        # need a copy. A shallow copy is enough: the elements
        # inside the player's frontier (3-tuples) and visited
        # (2-tuples) are themselves immutable, so freezing the
        # outer container is sufficient.
        if isinstance(value, list):
            value = list(value)
        elif isinstance(value, set):
            value = set(value)
        elif isinstance(value, dict):
            value = dict(value)
        result[key] = value
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
        if isinstance(value, list):
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
