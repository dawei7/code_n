"""Optimal app-local solution for LeetCode 1313."""


def solve(nums):
    result = []
    for index in range(0, len(nums), 2):
        frequency = nums[index]
        value = nums[index + 1]
        result.extend([value] * frequency)
    return result
