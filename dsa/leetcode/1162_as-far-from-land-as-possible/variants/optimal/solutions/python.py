"""Optimal app-local solution for LeetCode 1162."""

from collections import deque


def solve(grid: list[list[int]]) -> int:
    size = len(grid)
    queue = deque()
    seen = [[False] * size for _ in range(size)]
    for row in range(size):
        for column in range(size):
            if grid[row][column] == 1:
                queue.append((row, column))
                seen[row][column] = True

    if not queue or len(queue) == size * size:
        return -1

    distance = -1
    while queue:
        for _ in range(len(queue)):
            row, column = queue.popleft()
            for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + row_step
                next_column = column + column_step
                if (
                    0 <= next_row < size
                    and 0 <= next_column < size
                    and not seen[next_row][next_column]
                ):
                    seen[next_row][next_column] = True
                    queue.append((next_row, next_column))
        distance += 1
    return distance
