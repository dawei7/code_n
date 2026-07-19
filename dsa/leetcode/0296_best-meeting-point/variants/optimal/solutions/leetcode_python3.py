from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows = [
            row
            for row in range(len(grid))
            for column in range(len(grid[0]))
            if grid[row][column] == 1
        ]
        columns = [
            column
            for column in range(len(grid[0]))
            for row in range(len(grid))
            if grid[row][column] == 1
        ]
        meeting_row = rows[len(rows) // 2]
        meeting_column = columns[len(columns) // 2]
        return sum(abs(row - meeting_row) for row in rows) + sum(
            abs(column - meeting_column) for column in columns
        )
