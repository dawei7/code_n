"""Optimal solution for LeetCode 1004: Max Consecutive Ones III."""


def solve(nums: list[int], k: int) -> int:
    left = 0
    zeroes = 0
    best = 0
    for right, value in enumerate(nums):
        if value == 0:
            zeroes += 1
        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
