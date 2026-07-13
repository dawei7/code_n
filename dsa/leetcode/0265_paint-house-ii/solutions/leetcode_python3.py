from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        previous = [0] * len(costs[0])
        for row in costs:
            minimum = min(previous)
            minimum_color = previous.index(minimum)
            second_minimum = min(
                value for color, value in enumerate(previous) if color != minimum_color
            ) if len(previous) > 1 else float("inf")
            previous = [
                cost + (second_minimum if color == minimum_color else minimum)
                for color, cost in enumerate(row)
            ]
        return int(min(previous))
