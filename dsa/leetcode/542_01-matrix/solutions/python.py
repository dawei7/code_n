"""Multi-source breadth-first search for LeetCode 542."""

from collections import deque


def solve(mat: list[list[int]]) -> list[list[int]]:
    rows, cols = len(mat), len(mat[0])
    distances = [[-1] * cols for _ in range(rows)]
    queue = deque()
    for row in range(rows):
        for col in range(cols):
            if mat[row][col] == 0:
                distances[row][col] = 0
                queue.append((row, col))

    while queue:
        row, col = queue.popleft()
        for next_row, next_col in (
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ):
            if (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and distances[next_row][next_col] == -1
            ):
                distances[next_row][next_col] = distances[row][col] + 1
                queue.append((next_row, next_col))
    return distances
