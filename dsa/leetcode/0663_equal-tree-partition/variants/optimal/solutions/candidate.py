from __future__ import annotations


class TreeNode:
    """Local equivalent of LeetCode's TreeNode."""

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode) -> bool:
    subtree_sums = []

    def total(node: TreeNode | None) -> int:
        if node is None:
            return 0
        value = node.val + total(node.left) + total(node.right)
        subtree_sums.append(value)
        return value

    tree_sum = total(root)
    subtree_sums.pop()
    return tree_sum % 2 == 0 and tree_sum // 2 in subtree_sums
