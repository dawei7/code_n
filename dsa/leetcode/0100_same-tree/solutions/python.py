from typing import Any


def solve(p: Any | None, q: Any | None) -> bool:
    if p is None or q is None:
        return p is q
    return p.val == q.val and solve(p.left, q.left) and solve(p.right, q.right)
