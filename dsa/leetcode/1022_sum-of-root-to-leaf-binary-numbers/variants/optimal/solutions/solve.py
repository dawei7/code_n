"""Optimal app-local solution for LeetCode 1022."""


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


def solve(root):
    def visit(node, prefix):
        if node is None:
            return 0

        current = prefix * 2 + node.val
        if node.left is None and node.right is None:
            return current

        return visit(node.left, current) + visit(node.right, current)

    return visit(root, 0)
