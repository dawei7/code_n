def solve(grid: list[list[int]], k: int) -> int:
    MOD = 10**9 + 7
    rows = len(grid)
    cols = len(grid[0])
    
    # dp[i][j][rem] stores the number of paths to (i, j) with sum % k == rem
    dp = [[[0] * k for _ in range(cols)] for _ in range(rows)]
    
    # Initialize starting cell
    dp[0][0][grid[0][0] % k] = 1
    
    for i in range(rows):
        for j in range(cols):
            for rem in range(k):
                if dp[i][j][rem] == 0:
                    continue
                
                # Move Down
                if i + 1 < rows:
                    new_rem = (rem + grid[i + 1][j]) % k
                    dp[i + 1][j][new_rem] = (dp[i + 1][j][new_rem] + dp[i][j][rem]) % MOD
                
                # Move Right
                if j + 1 < cols:
                    new_rem = (rem + grid[i][j + 1]) % k
                    dp[i][j + 1][new_rem] = (dp[i][j + 1][new_rem] + dp[i][j][rem]) % MOD
                    
    return dp[rows - 1][cols - 1][0]
