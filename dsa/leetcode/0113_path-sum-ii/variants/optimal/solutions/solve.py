from typing import Any


class TreeNode:
    """Local equivalent of LeetCode's TreeNode for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


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
