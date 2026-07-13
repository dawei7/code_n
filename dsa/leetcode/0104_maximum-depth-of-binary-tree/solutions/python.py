from typing import Any


def solve(root: Any | None) -> int:
    if root is None:
        return 0

    maximum = 0
    stack = [(root, 1)]
    while stack:
        node, depth = stack.pop()
        maximum = max(maximum, depth)
        if node.right is not None:
            stack.append((node.right, depth + 1))
        if node.left is not None:
            stack.append((node.left, depth + 1))
    return maximum
