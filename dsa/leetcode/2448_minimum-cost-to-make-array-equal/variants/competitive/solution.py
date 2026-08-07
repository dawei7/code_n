from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs = sorted(zip(nums, cost))
        total_weight = sum(cost)
        prefix_weight = 0
        target = pairs[0][0]

        for value, weight in pairs:
            prefix_weight += weight
            if prefix_weight * 2 >= total_weight:
                target = value
                break

        return sum(abs(value - target) * weight for value, weight in pairs)
