from collections import deque
from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        modulus = 1_000_000_007
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        rows, columns = len(grid), len(grid[0])
        smaller_neighbors = [[0] * columns for _ in range(rows)]
        path_count = [[1] * columns for _ in range(rows)]

        for row in range(rows):
            for column in range(columns):
                for row_step, column_step in directions:
                    next_row = row + row_step
                    next_column = column + column_step
                    if (
                        0 <= next_row < rows
                        and 0 <= next_column < columns
                        and grid[next_row][next_column] < grid[row][column]
                    ):
                        smaller_neighbors[row][column] += 1

        queue = deque(
            (row, column)
            for row in range(rows)
            for column in range(columns)
            if smaller_neighbors[row][column] == 0
        )

        while queue:
            row, column = queue.popleft()
            for row_step, column_step in directions:
                next_row = row + row_step
                next_column = column + column_step
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and grid[next_row][next_column] > grid[row][column]
                ):
                    path_count[next_row][next_column] = (
                        path_count[next_row][next_column]
                        + path_count[row][column]
                    ) % modulus
                    smaller_neighbors[next_row][next_column] -= 1
                    if smaller_neighbors[next_row][next_column] == 0:
                        queue.append((next_row, next_column))

        return sum(map(sum, path_count)) % modulus
