from functools import lru_cache


def solve(pizza, k):
    mod = 1_000_000_007
    grid = [list(row) if isinstance(row, str) else list(row) for row in pizza]
    rows = len(grid)
    cols = max((len(row) for row in grid), default=0)
    for row in grid:
        row.extend(["."] * (cols - len(row)))
    has_apple = [[0] * (cols + 1) for _ in range(rows + 1)]
    for row in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):
            cell = grid[row][col]
            apple = cell == "A" or (isinstance(cell, int) and cell != 0)
            has_apple[row][col] = (
                int(apple)
                + has_apple[row + 1][col]
                + has_apple[row][col + 1]
                - has_apple[row + 1][col + 1]
            )

    @lru_cache(None)
    def dp(row, col, pieces):
        if has_apple[row][col] == 0:
            return 0
        if pieces == 1:
            return 1
        ways = 0
        for next_row in range(row + 1, rows):
            if has_apple[row][col] - has_apple[next_row][col] > 0:
                ways += dp(next_row, col, pieces - 1)
        for next_col in range(col + 1, cols):
            if has_apple[row][col] - has_apple[row][next_col] > 0:
                ways += dp(row, next_col, pieces - 1)
        return ways % mod

    return dp(0, 0, max(1, min(k, rows + cols))) if rows and cols else 0
