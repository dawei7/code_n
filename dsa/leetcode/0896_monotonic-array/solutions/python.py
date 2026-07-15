"""Optimal app-local solution for LeetCode 896."""


def solve(nums):
    increasing = True
    decreasing = True

    for previous, current in zip(nums, nums[1:]):
        if previous < current:
            decreasing = False
        elif previous > current:
            increasing = False

        if not increasing and not decreasing:
            return False

    return True
