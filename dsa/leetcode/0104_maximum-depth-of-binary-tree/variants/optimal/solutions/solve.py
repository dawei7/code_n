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


def solve(root: Any | None) -> int:
    if root is None:
        return 0

    maximum = 0
    stack = [(root, 1)]
    while stack:
        node, depth = stack.pop()
        maximum = max(maximum, depth)
        if node.right is not None:
            stack.append((node.right, depth + 1))
        if node.left is not None:
            stack.append((node.left, depth + 1))
    return maximum
