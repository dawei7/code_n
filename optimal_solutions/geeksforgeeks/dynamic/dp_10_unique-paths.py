"""Optimal solution for dp_10: Unique Paths.

Count paths from (0,0) to (m-1, n-1) moving only right/down.
1 = obstacle, 0 = free.
"""


def solve(grid, m, n):
    if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
        return 0
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[m - 1][n - 1]
