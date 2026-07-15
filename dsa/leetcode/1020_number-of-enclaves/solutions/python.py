"""Optimal app-local solution for LeetCode 1020."""

from collections import deque


def solve(grid):
    rows = len(grid)
    columns = len(grid[0])
    queue = deque()

    def add(row, column):
        if grid[row][column] == 1:
            grid[row][column] = 0
            queue.append((row, column))

    for row in range(rows):
        add(row, 0)
        add(row, columns - 1)
    for column in range(columns):
        add(0, column)
        add(rows - 1, column)

    while queue:
        row, column = queue.popleft()
        for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = row + row_step
            next_column = column + column_step
            if (
                0 <= next_row < rows
                and 0 <= next_column < columns
                and grid[next_row][next_column] == 1
            ):
                grid[next_row][next_column] = 0
                queue.append((next_row, next_column))

    return sum(sum(row) for row in grid)
