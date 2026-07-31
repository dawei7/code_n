from typing import List


class Solution:
    def minPathCost(
        self,
        grid: List[List[int]],
        moveCost: List[List[int]],
    ) -> int:
        costs = grid[0][:]

        for row_index in range(1, len(grid)):
            next_costs = [float("inf")] * len(grid[0])
            for previous_column, previous_cost in enumerate(costs):
                previous_value = grid[row_index - 1][previous_column]
                for column, value in enumerate(grid[row_index]):
                    candidate = (
                        previous_cost
                        + moveCost[previous_value][column]
                        + value
                    )
                    next_costs[column] = min(next_costs[column], candidate)
            costs = next_costs

        return int(min(costs))
