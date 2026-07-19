"""Optimal app-local solution for LeetCode 1437."""


def solve(nums: list[int], k: int) -> bool:
    previous = None
    for index, value in enumerate(nums):
        if value == 1:
            if previous is not None and index - previous <= k:
                return False
            previous = index
    return True
