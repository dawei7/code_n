from bisect import bisect_left
from typing import List


class Solution:
    def minAbsoluteSumDiff(
        self, nums1: List[int], nums2: List[int]
    ) -> int:
        ordered = sorted(nums1)
        total = 0
        best_reduction = 0

        for first, second in zip(nums1, nums2):
            difference = abs(first - second)
            total += difference

            position = bisect_left(ordered, second)
            if position < len(ordered):
                best_reduction = max(
                    best_reduction,
                    difference - abs(ordered[position] - second),
                )
            if position > 0:
                best_reduction = max(
                    best_reduction,
                    difference - abs(ordered[position - 1] - second),
                )

        return (total - best_reduction) % 1_000_000_007
