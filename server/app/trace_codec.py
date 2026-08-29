"""JSON-safe conversion for ``solve()`` return values.

The per-step trace is no longer serialized into the REST API; the
in-app debugger streams live state through DAP. What's left here is
:func:`to_json_safe`,
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


def _tree_node_to_list(root: Any) -> list[Any]:
    if root is None:
        return []
    res: list[Any] = []
    seen: set[int] = set()
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is not None:
            if id(node) in seen:
                break
            seen.add(id(node))
            res.append(getattr(node, "val", None))
            queue.append(getattr(node, "left", None))
            queue.append(getattr(node, "right", None))
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res


def _list_node_to_list(head: Any) -> list[Any]:
    res = []
    seen = set()
    node = head
    while node is not None:
        if id(node) in seen:
            break
        seen.add(id(node))
        res.append(getattr(node, "val", None))
        node = getattr(node, "next", None)
    return res


def to_json_safe(value: Any) -> Any:
    """Recursively convert any Python value to a JSON-safe form."""
    if isinstance(value, _PRIMITIVE_TYPES):
        return value
    if hasattr(value, "val") and (hasattr(value, "left") or hasattr(value, "right")):
        return [to_json_safe(v) for v in _tree_node_to_list(value)]
    if hasattr(value, "val") and hasattr(value, "next"):
        return [to_json_safe(v) for v in _list_node_to_list(value)]
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
