"""Optimal app-local solution for LeetCode 437."""

from collections import defaultdict


class TreeNode:
    """Local equivalent of the binary-tree node supplied by LeetCode's judge."""

    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode | None, targetSum: int) -> int:
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1

    def count_paths(node: TreeNode | None, current_sum: int) -> int:
        if node is None:
            return 0
        current_sum += node.val
        total = prefix_counts[current_sum - targetSum]
        prefix_counts[current_sum] += 1
        total += count_paths(node.left, current_sum)
        total += count_paths(node.right, current_sum)
        prefix_counts[current_sum] -= 1
        return total

    return count_paths(root, 0)
