from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        operations = 0
        rows, columns = len(grid), len(grid[0])

        for column in range(columns):
            previous = grid[0][column]
            for row in range(1, rows):
                current = grid[row][column]
                required = max(current, previous + 1)
                operations += required - current
                previous = required

        return operations
