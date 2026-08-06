"""Inert solution-quality candidate for LeetCode 448."""


def solve(nums: list[int]) -> list[int]:
    for number in nums:
        marker = abs(number) - 1
        nums[marker] = -abs(nums[marker])
    return [i + 1 for i, marker in enumerate(nums) if marker > 0]
