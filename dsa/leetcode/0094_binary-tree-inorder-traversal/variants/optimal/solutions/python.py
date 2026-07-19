from typing import Any


def solve(root: Any | None) -> list[int]:
    result: list[int] = []
    stack: list[Any] = []
    node = root

    while node is not None or stack:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.val)
        node = node.right

    return result
