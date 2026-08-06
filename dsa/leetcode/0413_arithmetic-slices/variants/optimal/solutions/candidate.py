"""Inert review candidate for LeetCode 413: Arithmetic Slices."""


def solve(nums: list[int]) -> int:
    ending = 0
    total = 0

    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            ending += 1
            total += ending
        else:
            ending = 0

    return total
