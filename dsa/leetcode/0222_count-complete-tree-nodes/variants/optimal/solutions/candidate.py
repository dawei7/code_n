from __future__ import annotations


class TreeNode:
    """Local equivalent of LeetCode's TreeNode for the standalone app template."""

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode | None) -> int:
    def left_height(node: TreeNode | None) -> int:
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    total = 0
    while root:
        left = left_height(root.left)
        right = left_height(root.right)
        if left == right:
            total += 1 << left
            root = root.right
        else:
            total += 1 << right
            root = root.left
    return total
