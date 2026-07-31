"""Iterative reverse inorder accumulation for LeetCode 538."""


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
    total = 0
    stack = []
    node = root
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.right
        node = stack.pop()
        total += node.val
        node.val = total
        node = node.left
    return root
