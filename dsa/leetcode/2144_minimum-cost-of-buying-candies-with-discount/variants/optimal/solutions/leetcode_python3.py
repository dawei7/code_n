from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ordered = sorted(cost, reverse=True)
        return sum(
            price for index, price in enumerate(ordered) if index % 3 != 2
        )
