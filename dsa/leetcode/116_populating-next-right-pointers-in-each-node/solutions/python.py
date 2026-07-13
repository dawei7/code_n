from typing import Any


def solve(root: Any | None) -> Any | None:
    leftmost = root
    while leftmost is not None and leftmost.left is not None:
        node = leftmost
        while node is not None:
            node.left.next = node.right
            neighbor = getattr(node, "next", None)
            node.right.next = neighbor.left if neighbor is not None else None
            node = neighbor
        leftmost = leftmost.left
    return root
