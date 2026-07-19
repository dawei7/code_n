"""Optimal app-local solution for LeetCode 861."""


def solve(grid):
    row_count = len(grid)
    column_count = len(grid[0])
    score = 0

    for column in range(column_count):
        effective_ones = 0
        for row in range(row_count):
            effective_ones += grid[row][column] ^ (1 - grid[row][0])

        best_ones = max(effective_ones, row_count - effective_ones)
        score += best_ones << (column_count - 1 - column)

    return score
