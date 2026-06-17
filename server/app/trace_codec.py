"""JSON-safe conversion for ``solve()`` return values.

The per-step trace was removed from the API in the v0.9.0 pivot
(player edits + debugs in VSCode). What's left is :func:`to_json_safe`,
which the engine runner uses to render the return value of
``solve()`` as a compact string for the ``RunResponse.return_value_repr``
field. The recursion handles the common structured types
(list, tuple, set, dict) and stringifies anything else.

Order matters in :func:`to_json_safe`: ``bool`` is a subclass
of ``int``, so we check ``bool`` before ``int``.
"""
from __future__ import annotations

from typing import Any


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
