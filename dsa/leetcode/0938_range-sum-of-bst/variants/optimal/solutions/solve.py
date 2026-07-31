"""Optimal app-local solution for LeetCode 938."""


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


def solve(root, low, high):
    total = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if node.val < low:
            stack.append(node.right)
        elif node.val > high:
            stack.append(node.left)
        else:
            total += node.val
            stack.append(node.left)
            stack.append(node.right)
    return total
