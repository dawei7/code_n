from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        side = len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1
        while queue:
            row, column, distance = queue.popleft()
            if row == side - 1 and column == side - 1:
                return distance
            for row_step in (-1, 0, 1):
                for column_step in (-1, 0, 1):
                    if row_step == 0 and column_step == 0:
                        continue
                    next_row = row + row_step
                    next_column = column + column_step
                    if (
                        0 <= next_row < side
                        and 0 <= next_column < side
                        and grid[next_row][next_column] == 0
                    ):
                        grid[next_row][next_column] = 1
                        queue.append((next_row, next_column, distance + 1))
        return -1
