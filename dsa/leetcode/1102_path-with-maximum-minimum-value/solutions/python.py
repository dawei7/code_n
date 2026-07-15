"""Optimal app-local solution for LeetCode 1102."""

from heapq import heappop, heappush


def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])
    heap = [(-grid[0][0], 0, 0)]
    visited = [[False] * columns for _ in range(rows)]

    while heap:
        negative_score, row, column = heappop(heap)
        if visited[row][column]:
            continue
        score = -negative_score
        if row == rows - 1 and column == columns - 1:
            return score
        visited[row][column] = True
        for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = row + row_step
            next_column = column + column_step
            if 0 <= next_row < rows and 0 <= next_column < columns and not visited[next_row][next_column]:
                candidate = min(score, grid[next_row][next_column])
                heappush(heap, (-candidate, next_row, next_column))

    raise RuntimeError("the destination is unreachable")
