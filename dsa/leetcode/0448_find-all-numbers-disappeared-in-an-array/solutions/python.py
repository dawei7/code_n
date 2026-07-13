"""Optimal app-local solution for LeetCode 448."""


def solve(nums: list[int]) -> list[int]:
    for number in nums:
        marker = abs(number) - 1
        nums[marker] = -abs(nums[marker])
    return [index + 1 for index, marker in enumerate(nums) if marker > 0]
