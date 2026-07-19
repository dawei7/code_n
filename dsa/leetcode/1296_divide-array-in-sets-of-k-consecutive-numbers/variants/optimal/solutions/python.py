"""Optimal app-local solution for LeetCode 1296."""

from collections import Counter


def solve(nums, k):
    if len(nums) % k != 0:
        return False

    counts = Counter(nums)
    for start in sorted(counts):
        copies = counts[start]
        if copies == 0:
            continue
        for value in range(start, start + k):
            if counts[value] < copies:
                return False
            counts[value] -= copies

    return True
