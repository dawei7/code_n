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


def solve(root: Any | None, targetSum: int) -> bool:
    if root is None:
        return False
    stack = [(root, root.val)]
    while stack:
        node, path_sum = stack.pop()
        if node.left is None and node.right is None and path_sum == targetSum:
            return True
        if node.right is not None:
            stack.append((node.right, path_sum + node.right.val))
        if node.left is not None:
            stack.append((node.left, path_sum + node.left.val))
    return False
