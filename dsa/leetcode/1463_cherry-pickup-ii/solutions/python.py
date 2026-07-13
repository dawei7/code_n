def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    if not rows or not cols:
        return 0
    dp = {(0, cols - 1): grid[0][0] + (grid[0][cols - 1] if cols > 1 else 0)}
    for row in range(1, rows):
        next_dp = {}
        for (c1, c2), value in dp.items():
            for nc1 in (c1 - 1, c1, c1 + 1):
                for nc2 in (c2 - 1, c2, c2 + 1):
                    if 0 <= nc1 < cols and 0 <= nc2 < cols:
                        gain = grid[row][nc1] + (grid[row][nc2] if nc1 != nc2 else 0)
                        key = (nc1, nc2)
                        next_dp[key] = max(next_dp.get(key, -1), value + gain)
        dp = next_dp
    return max(dp[key] for key in dp)
