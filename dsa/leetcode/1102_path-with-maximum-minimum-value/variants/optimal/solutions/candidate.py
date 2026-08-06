"""Candidate app-local solution for LeetCode 1102."""

from heapq import heappop, heappush


def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])
    endpoint_cap = min(grid[0][0], grid[-1][-1])
    if min(min(row) for row in grid) >= endpoint_cap:
        return endpoint_cap

    best_score = [[-1] * columns for _ in range(rows)]
    best_score[0][0] = grid[0][0]
    heap = [(-grid[0][0], 0, 0)]

    while heap:
        negative_score, row, column = heappop(heap)
        score = -negative_score
        if score < best_score[row][column]:
            continue
        if row == rows - 1 and column == columns - 1:
            return score
        for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = row + row_step
            next_column = column + column_step
            if 0 <= next_row < rows and 0 <= next_column < columns:
                candidate = min(score, grid[next_row][next_column])
                if candidate > best_score[next_row][next_column]:
                    best_score[next_row][next_column] = candidate
                    heappush(heap, (-candidate, next_row, next_column))

    return -1
