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


def solve(root: Any | None) -> None:
    current = root
    while current is not None:
        if current.left is not None:
            predecessor = current.left
            while predecessor.right is not None:
                predecessor = predecessor.right
            predecessor.right = current.right
            current.right = current.left
            current.left = None
        current = current.right
