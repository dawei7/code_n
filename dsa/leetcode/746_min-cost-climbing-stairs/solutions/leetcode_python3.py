from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_before = 0
        one_before = 0

        for step_cost in cost:
            current = step_cost + min(two_before, one_before)
            two_before, one_before = one_before, current

        return min(two_before, one_before)
