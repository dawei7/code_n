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
