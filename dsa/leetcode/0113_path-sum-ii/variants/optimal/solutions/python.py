from typing import Any


def solve(root: Any | None, targetSum: int) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def search(node: Any | None, remaining: int) -> None:
        if node is None:
            return
        path.append(node.val)
        remaining -= node.val
        if node.left is None and node.right is None:
            if remaining == 0:
                result.append(path.copy())
        else:
            search(node.left, remaining)
            search(node.right, remaining)
        path.pop()

    search(root, targetSum)
    return result
