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
    def mirror(left: Any | None, right: Any | None) -> bool:
        if left is None or right is None:
            return left is right
        return left.val == right.val and mirror(left.left, right.right) and mirror(left.right, right.left)

    return root is None or mirror(root.left, root.right)
