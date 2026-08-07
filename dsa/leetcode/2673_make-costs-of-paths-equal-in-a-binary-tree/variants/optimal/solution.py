from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        increments = 0

        for parent in range(n // 2 - 1, -1, -1):
            left = 2 * parent + 1
            right = left + 1
            increments += abs(cost[left] - cost[right])
            cost[parent] += max(cost[left], cost[right])

        return increments
