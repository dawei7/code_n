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


def solve(root: Any) -> bool:
    if root.left is None:
        return bool(root.val)

    left_value = solve(root.left)
    right_value = solve(root.right)
    if root.val == 2:
        return left_value or right_value
    return left_value and right_value
