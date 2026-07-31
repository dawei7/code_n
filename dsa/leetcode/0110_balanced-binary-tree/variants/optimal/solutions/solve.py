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


def solve(root: Any | None) -> bool:
    def height(node: Any | None) -> int:
        if node is None:
            return 0
        left_height = height(node.left)
        if left_height < 0:
            return -1
        right_height = height(node.right)
        if right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)

    return height(root) >= 0
