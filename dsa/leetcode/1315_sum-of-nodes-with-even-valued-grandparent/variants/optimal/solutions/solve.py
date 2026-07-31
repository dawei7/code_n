"""Optimal app-local solution for LeetCode 1315."""


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
    stack = [(root, None, None)]

    while stack:
        node, parent_value, grandparent_value = stack.pop()
        if grandparent_value is not None and grandparent_value % 2 == 0:
            total += node.val

        if node.left is not None:
            stack.append((node.left, node.val, parent_value))
        if node.right is not None:
            stack.append((node.right, node.val, parent_value))

    return total
