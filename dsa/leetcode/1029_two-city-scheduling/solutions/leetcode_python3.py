from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ordered = sorted(costs, key=lambda cost: cost[0] - cost[1])
        half = len(ordered) // 2
        return sum(cost[0] for cost in ordered[:half]) + sum(
            cost[1] for cost in ordered[half:]
        )

