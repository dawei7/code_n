"""Optimal app-local solution for LeetCode 3603."""


def solve(m, n, waitCost):
    transposed = n > m
    height, width = (n, m) if transposed else (m, n)
    infinity = float("inf")
    dp = [infinity] * width
    dp[0] = 1

    for row in range(height):
        for column in range(width):
            if row == 0 and column == 0:
                continue
            from_above = dp[column]
            from_left = dp[column - 1] if column else infinity
            original_row, original_column = (
                (column, row) if transposed else (row, column)
            )
            dp[column] = (
                min(from_above, from_left)
                + (original_row + 1) * (original_column + 1)
                + waitCost[original_row][original_column]
            )

    return dp[-1] - waitCost[-1][-1]
