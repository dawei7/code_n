"""Optimal solution for LeetCode 1060: Missing Element in Sorted Array."""


def solve(nums: list[int], k: int) -> int:
    def missing_count_at(array_position: int) -> int:
        return nums[array_position] - nums[0] - array_position

    missing_before_end = missing_count_at(len(nums) - 1)
    if k > missing_before_end:
        return nums[-1] + k - missing_before_end

    left = 0
    right = len(nums) - 1
    while left < right:
        middle = (left + right) // 2
        if missing_count_at(middle) < k:
            left = middle + 1
        else:
            right = middle

    gap_left_position = left - 1
    return nums[gap_left_position] + k - missing_count_at(gap_left_position)
