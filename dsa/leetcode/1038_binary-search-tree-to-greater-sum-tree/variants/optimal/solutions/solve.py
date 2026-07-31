"""Optimal app-local solution for LeetCode 1038."""


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
    running_sum = 0
    stack = []
    node = root

    while node is not None or stack:
        while node is not None:
            stack.append(node)
            node = node.right
        node = stack.pop()
        running_sum += node.val
        node.val = running_sum
        node = node.left

    return root
