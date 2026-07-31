from __future__ import annotations


def solve(grid: list[list[int]]) -> list[list[int]]:
    rows = len(grid)
    cols = len(grid[0])
    cells = sorted(
        (grid[row][col], row, col)
        for row in range(rows)
        for col in range(cols)
    )
    row_max = [0] * rows
    col_max = [0] * cols
    answer = [[0] * cols for _ in range(rows)]

    for _, row, col in cells:
        score = max(row_max[row], col_max[col]) + 1
        answer[row][col] = score
        row_max[row] = score
        col_max[col] = score

    return answer
