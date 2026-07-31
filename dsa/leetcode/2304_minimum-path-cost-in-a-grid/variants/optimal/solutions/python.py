from typing import List


def solve(grid: List[List[int]], moveCost: List[List[int]]) -> int:
    costs = grid[0][:]

    for row_index in range(1, len(grid)):
        row = grid[row_index]
        next_costs = [float("inf")] * len(row)
        for previous_column, previous_cost in enumerate(costs):
            previous_value = grid[row_index - 1][previous_column]
            for column, value in enumerate(row):
                candidate = previous_cost + moveCost[previous_value][column] + value
                next_costs[column] = min(next_costs[column], candidate)
        costs = next_costs

    return int(min(costs))
