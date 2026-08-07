from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        ordered = sorted(nums)
        pair_sums = set()
        n = len(ordered)

        for left in range(n // 2):
            pair_sums.add(ordered[left] + ordered[n - 1 - left])

        return len(pair_sums)
