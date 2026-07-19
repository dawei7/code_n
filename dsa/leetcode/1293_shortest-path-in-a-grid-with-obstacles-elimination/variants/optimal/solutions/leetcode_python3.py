from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        columns = len(grid[0])
        if rows == 1 and columns == 1:
            return 0
        if k >= rows + columns - 3:
            return rows + columns - 2

        queue = deque([(0, 0, k, 0)])
        best_remaining = [[-1] * columns for _ in range(rows)]
        best_remaining[0][0] = k

        while queue:
            row, column, remaining, steps = queue.popleft()
            for row_delta, column_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + row_delta
                next_column = column + column_delta
                if not (0 <= next_row < rows and 0 <= next_column < columns):
                    continue
                next_remaining = remaining - grid[next_row][next_column]
                if next_remaining < 0 or best_remaining[next_row][next_column] >= next_remaining:
                    continue
                if next_row == rows - 1 and next_column == columns - 1:
                    return steps + 1
                best_remaining[next_row][next_column] = next_remaining
                queue.append((next_row, next_column, next_remaining, steps + 1))

        return -1
