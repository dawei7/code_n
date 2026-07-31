import heapq
from typing import List


class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def non_decreasing_cost(values: List[int]) -> int:
            maximums = []
            cost = 0
            for value in values:
                heapq.heappush(maximums, -value)
                largest = -maximums[0]
                if largest > value:
                    cost += largest - value
                    heapq.heapreplace(maximums, -value)
            return cost

        return min(
            non_decreasing_cost(nums),
            non_decreasing_cost([-value for value in nums]),
        )
