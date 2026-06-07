"""Convert engine objects to JSON-safe dicts.

The engine's :class:`code_n.execution_trace.TraceFrame` carries
``locals`` as a snapshot of the player's frame.f_locals at the time
of the line event. The engine's own ``_serialize_locals`` already
unwraps :class:`code_n.tracked.TrackedValue` and shallow-copies
mutable containers, but it still leaves ``set`` and ``tuple`` types
intact - both of which are not JSON-serialisable. The BFS challenges
have set-valued locals (``visited``) and tuple-valued ones
(``frontier`` cells are ``(x, y)`` tuples), so the codec finishes
the job.

:func:`to_json_safe` is a recursive conversion that turns any Python
object into a JSON-safe value. The fall-through ``str(value)`` is
deliberate: a string repr is always JSON-safe, and any object that
isn't a known structured type is probably engine internals leaking
through (e.g. a TrackedGrid that ``_serialize_locals`` already turned
into a list of lists).
"""
from __future__ import annotations

from typing import Any

from code_n.counter import OpRecord, OpType
from code_n.execution_trace import TraceFrame
from code_n.tracked import TrackedGrid, TrackedList, TrackedValue


# Order matters in to_json_safe: bool is a subclass of int, so check
# bool before int.
_PRIMITIVE_TYPES = (bool, int, float, str, type(None))


def to_json_safe(value: Any) -> Any:
    """Recursively convert any Python value to a JSON-safe form.

    * :class:`TrackedList` / :class:`TrackedGrid` / :class:`TrackedValue`
      are unwrapped to their underlying ``.raw`` data (the engine keeps
      them as-is in the trace; the codec finishes the job for the wire)
    * ``list`` and ``tuple`` become ``list``
    * ``set`` becomes ``list`` (insertion order)
    * ``dict`` keys are stringified (JSON requires string keys)
    * all primitive types pass through
    * everything else is ``str()``-ified
    """
    # Engine wrappers first — they're the most common non-primitive
    # in the trace.
    if isinstance(value, TrackedValue):
        return to_json_safe(value.raw)
    if isinstance(value, TrackedList):
        return to_json_safe(value._data)  # already a plain list
    if isinstance(value, TrackedGrid):
        return to_json_safe([row[:] for row in value._data])
    if isinstance(value, _PRIMITIVE_TYPES):
        return value
    if isinstance(value, (list, tuple)):
        return [to_json_safe(v) for v in value]
    if isinstance(value, set):
        return [to_json_safe(v) for v in value]
    if isinstance(value, dict):
        return {str(k): to_json_safe(v) for k, v in value.items()}
    # Fallback: stringify. Covers user-defined classes, repr-able oddities.
    try:
        return str(value)
    except Exception:
        return f"<{type(value).__name__}>"


def serialize_op(op: OpRecord) -> dict[str, str]:
    """Convert an :class:`OpRecord` to a JSON-safe ``{"op_type", "detail"}`` dict."""
    return {
        "op_type": op.op_type.value if isinstance(op.op_type, OpType) else str(op.op_type),
        "detail": op.detail or "",
    }


def serialize_frame(frame: TraceFrame) -> dict[str, Any]:
    """Convert a :class:`TraceFrame` to a JSON-safe dict.

    The ``locals`` dict is run through :func:`to_json_safe` so that
    sets, tuples, and any leaked engine objects become lists / strings.
    ``source_line`` is left empty here; the route layer (which has
    the player's source) can fill it in if it wants to.
    """
    return {
        "op_index": int(frame.op_index),
        "line_no": int(frame.line_no),
        "event": str(frame.event),
        "locals": to_json_safe(frame.locals),
        "return_value": str(frame.return_value or ""),
        "breakpoint": bool(frame.breakpoint),
        "source_file": str(frame.source_file or ""),
        "source_line": "",
    }
