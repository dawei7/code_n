"""App-local reference solution for LeetCode 2831."""

from collections import defaultdict
from typing import List


def solve(nums: List[int], k: int) -> int:
    """Return the longest equal subarray obtainable with at most k deletions."""
    positions_by_value = defaultdict(list)
    for index, value in enumerate(nums):
        positions_by_value[value].append(index)

    best = 0
    for positions in positions_by_value.values():
        left = 0
        for right in range(len(positions)):
            while positions[right] - positions[left] - (right - left) > k:
                left += 1
            best = max(best, right - left + 1)

    return best
