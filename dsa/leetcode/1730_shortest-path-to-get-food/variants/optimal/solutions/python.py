
from collections import deque
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        start = (-1, -1)

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "*":
                    start = (row, column)
                    break
            if start[0] != -1:
                break

        queue = deque([(start[0], start[1], 0)])
        visited = {start}

        while queue:
            row, column, distance = queue.popleft()
            for row_step, column_step in (
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1),
            ):
                next_row = row + row_step
                next_column = column + column_step
                position = (next_row, next_column)
                if (
                    next_row < 0
                    or next_row >= rows
                    or next_column < 0
                    or next_column >= columns
                    or grid[next_row][next_column] == "X"
                    or position in visited
                ):
                    continue
                if grid[next_row][next_column] == "#":
                    return distance + 1
                visited.add(position)
                queue.append((next_row, next_column, distance + 1))

        return -1


def solve(grid: list[list[str]]) -> int:
    return Solution().getFood(grid)

