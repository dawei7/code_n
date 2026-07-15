"""Optimal solution for LeetCode 1060: Missing Element in Sorted Array."""


def solve(nums: list[int], k: int) -> int:
    def missing(index: int) -> int:
        return nums[index] - nums[0] - index

    missing_before_end = missing(len(nums) - 1)
    if k > missing_before_end:
        return nums[-1] + k - missing_before_end

    left = 0
    right = len(nums) - 1
    while left < right:
        middle = (left + right) // 2
        if missing(middle) < k:
            left = middle + 1
        else:
            right = middle

    previous = left - 1
    return nums[previous] + k - missing(previous)
