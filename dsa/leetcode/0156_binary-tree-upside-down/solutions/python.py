from typing import Any


def solve(root: Any | None) -> Any | None:
    current = root
    parent = None
    parent_right = None
    while current is not None:
        following = current.left
        current.left = parent_right
        parent_right = current.right
        current.right = parent
        parent = current
        current = following
    return parent
