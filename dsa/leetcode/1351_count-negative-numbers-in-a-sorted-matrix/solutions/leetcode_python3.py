from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        row = rows - 1
        column = 0
        negatives = 0

        while row >= 0 and column < columns:
            if grid[row][column] < 0:
                negatives += columns - column
                row -= 1
            else:
                column += 1

        return negatives
