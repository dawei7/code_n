"""Pair-sum frequency solution for LeetCode 454."""

from collections import Counter


def solve(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    first_sums = Counter(a + b for a in nums1 for b in nums2)
    total = 0
    for c in nums3:
        for d in nums4:
            total += first_sums.get(-(c + d), 0)
    return total
