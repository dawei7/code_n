from typing import List


class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        best = [10**30] * n
        best[0] = 0
        nonincreasing = []
        increasing = []

        for index, value in enumerate(nums):
            while nonincreasing and nums[nonincreasing[-1]] <= value:
                source = nonincreasing.pop()
                best[index] = min(
                    best[index], best[source] + costs[index]
                )

            while increasing and nums[increasing[-1]] > value:
                source = increasing.pop()
                best[index] = min(
                    best[index], best[source] + costs[index]
                )

            nonincreasing.append(index)
            increasing.append(index)

        return best[-1]
