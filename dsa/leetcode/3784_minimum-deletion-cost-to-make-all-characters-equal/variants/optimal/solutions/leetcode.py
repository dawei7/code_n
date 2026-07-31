from typing import List


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        kept_cost = [0] * 26
        total_cost = 0

        for char, deletion_cost in zip(s, cost):
            total_cost += deletion_cost
            kept_cost[ord(char) - ord("a")] += deletion_cost

        return total_cost - max(kept_cost)
