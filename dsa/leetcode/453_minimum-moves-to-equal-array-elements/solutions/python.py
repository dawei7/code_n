"""Linear arithmetic solution for LeetCode 453."""


def solve(nums: list[int]) -> int:
    minimum = nums[0]
    total = 0
    for value in nums:
        total += value
        if value < minimum:
            minimum = value
    return total - minimum * len(nums)
