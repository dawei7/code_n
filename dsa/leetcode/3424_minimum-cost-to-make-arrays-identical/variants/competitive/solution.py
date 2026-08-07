from typing import List


class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        direct_cost = sum(abs(a - b) for a, b in zip(arr, brr))
        rearranged_cost = k + sum(abs(a - b) for a, b in zip(sorted(arr), sorted(brr)))
        return min(direct_cost, rearranged_cost)
