from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        queue = []
        fresh = 0

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2:
                    queue.append((row, column, 0))
                elif grid[row][column] == 1:
                    fresh += 1

        head = 0
        minutes = 0
        while head < len(queue):
            row, column, minute = queue[head]
            head += 1
            minutes = max(minutes, minute)
            for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + row_step
                next_column = column + column_step
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and grid[next_row][next_column] == 1
                ):
                    grid[next_row][next_column] = 2
                    fresh -= 1
                    queue.append((next_row, next_column, minute + 1))

        return minutes if fresh == 0 else -1
