"""Optimal solution for LeetCode 108: Convert Sorted Array to Binary Search Tree."""


class TreeNode:
    """Local equivalent of the binary-tree node supplied by LeetCode's judge."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(nums: list[int]):
    def build(left: int, right: int):
        if left > right:
            return None
        middle = (left + right) // 2
        return TreeNode(
            nums[middle],
            build(left, middle - 1),
            build(middle + 1, right),
        )

    return build(0, len(nums) - 1)
