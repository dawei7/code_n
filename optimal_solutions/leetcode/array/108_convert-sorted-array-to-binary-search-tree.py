"""Optimal solution for LeetCode 108: Convert Sorted Array to Binary Search Tree."""

from __future__ import annotations


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def solve(nums: list[int]) -> TreeNode | None:
    def build(left: int, right: int) -> TreeNode | None:
        if left > right:
            return None
        mid = (left + right) // 2
        return TreeNode(nums[mid], build(left, mid - 1), build(mid + 1, right))

    return build(0, len(nums) - 1)
