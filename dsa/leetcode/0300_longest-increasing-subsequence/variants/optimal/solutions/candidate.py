"""Naming-only candidate for LeetCode 300: Longest Increasing Subsequence."""

from bisect import bisect_left


def solve(nums: list[int]) -> int:
    tails = []
    for value in nums:
        i = bisect_left(tails, value)
        if i == len(tails):
            tails.append(value)
        else:
            tails[i] = value
    return len(tails)
