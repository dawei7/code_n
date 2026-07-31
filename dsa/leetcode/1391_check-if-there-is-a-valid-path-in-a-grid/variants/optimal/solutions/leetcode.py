from collections import deque
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        openings = (
            (),
            ((0, -1), (0, 1)),
            ((-1, 0), (1, 0)),
            ((0, -1), (1, 0)),
            ((0, 1), (1, 0)),
            ((0, -1), (-1, 0)),
            ((0, 1), (-1, 0)),
        )
        rows, columns = len(grid), len(grid[0])
        queue = deque([(0, 0)])
        seen = {(0, 0)}

        while queue:
            row, column = queue.popleft()
            if row == rows - 1 and column == columns - 1:
                return True
            for delta_row, delta_column in openings[grid[row][column]]:
                next_row = row + delta_row
                next_column = column + delta_column
                neighbor = (next_row, next_column)
                if not (0 <= next_row < rows and 0 <= next_column < columns):
                    continue
                if neighbor in seen:
                    continue
                if (-delta_row, -delta_column) not in openings[grid[next_row][next_column]]:
                    continue
                seen.add(neighbor)
                queue.append(neighbor)

        return False
