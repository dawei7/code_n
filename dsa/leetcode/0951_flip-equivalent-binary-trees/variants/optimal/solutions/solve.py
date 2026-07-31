"""Optimal app-local solution for LeetCode 951."""


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


def solve(root1, root2):
    if root1 is root2:
        return True
    if root1 is None or root2 is None or root1.val != root2.val:
        return False
    return (solve(root1.left, root2.left) and solve(root1.right, root2.right)) or (
        solve(root1.left, root2.right) and solve(root1.right, root2.left)
    )
