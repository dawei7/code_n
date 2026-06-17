"""Convert engine trace frames to JSON-safe dicts.

The engine's :class:`code_n.execution_trace.TraceFrame` carries
``locals`` as a snapshot of the player's frame.f_locals at the
time of the line event. The engine's own ``_serialize_locals``
already shallow-copies mutable containers, but it still leaves
``set`` and ``tuple`` types intact - both of which are not
JSON-serialisable. The BFS challenges have set-valued locals
(``visited``) and tuple-valued ones (``frontier`` cells are
``(x, y)`` tuples), so this module finishes the job.

:func:`to_json_safe` is a recursive conversion that turns any
Python object into a JSON-safe value. The fall-through
``str(value)`` is deliberate: a string repr is always JSON-safe,
and any object that isn't a known structured type is probably
engine internals leaking through.

Note: the old runtime counter's
``TrackedList`` / ``TrackedGrid`` / ``TrackedValue`` wrappers
were removed in v0.8.5. The branches in ``to_json_safe`` that
used to unwrap them are gone — the player's input is now a
plain list / dict / set, and the list / tuple / set / dict
paths handle them.
"""
from __future__ import annotations

from typing import Any

from code_n.execution_trace import TraceFrame


# Order matters in to_json_safe: bool is a subclass of int, so check
# bool before int.
_PRIMITIVE_TYPES = (bool, int, float, str, type(None))


def to_json_safe(value: Any) -> Any:
    """Recursively convert any Python value to a JSON-safe form.

    * ``list`` and ``tuple`` become ``list``
    * ``set`` becomes ``list`` (insertion order)
    * ``dict`` keys are stringified (JSON requires string keys)
    * all primitive types pass through
    * everything else is ``str()``-ified
    """
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


def serialize_frame(frame: TraceFrame) -> dict[str, Any]:
    """Convert a :class:`TraceFrame` to a JSON-safe dict.

    The ``locals`` dict is run through :func:`to_json_safe` so that
    every value is wire-safe (sets become arrays, tuples become
    arrays, dict keys are stringified, etc.). The ``frame_index``
    field is the frame's position in the trace's frame list —
    the visualizer's step player drives the slider off this
    index directly.
    """
    return {
        "frame_index": int(frame.frame_index),
        "line_no": int(frame.line_no),
        "event": frame.event,
        "locals": to_json_safe(frame.locals),
        "return_value": frame.return_value or "",
        "breakpoint": bool(frame.breakpoint),
        "source_file": frame.source_file or "",
        # source_line is filled in by the route layer; we don't
        # know the source text here.
        "source_line": "",
    }
