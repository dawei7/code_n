from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cost = [0] * len(grid[0])
        for row_index, row in enumerate(grid):
            for column, value in enumerate(row):
                if row_index == 0 and column == 0:
                    cost[column] = value
                elif row_index == 0:
                    cost[column] = cost[column - 1] + value
                elif column == 0:
                    cost[column] += value
                else:
                    cost[column] = min(cost[column], cost[column - 1]) + value
        return cost[-1]
