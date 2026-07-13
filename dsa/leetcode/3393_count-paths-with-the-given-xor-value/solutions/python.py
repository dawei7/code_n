def solve(grid: list[list[int]], k: int) -> int:
    MOD = 10**9 + 7
    m = len(grid)
    n = len(grid[0])
    # The maximum XOR value is 16 (2^4) based on problem constraints
    MAX_XOR = 16
    
    # dp[r][c][xor_val] stores the number of paths to (r, c) with XOR sum xor_val
    dp = [[[0] * MAX_XOR for _ in range(n)] for _ in range(m)]
    
    # Initialize starting point
    dp[0][0][grid[0][0]] = 1
    
    for r in range(m):
        for c in range(n):
            for val in range(MAX_XOR):
                if dp[r][c][val] == 0:
                    continue
                
                # Move Right
                if c + 1 < n:
                    new_xor = val ^ grid[r][c + 1]
                    dp[r][c + 1][new_xor] = (dp[r][c + 1][new_xor] + dp[r][c][val]) % MOD
                
                # Move Down
                if r + 1 < m:
                    new_xor = val ^ grid[r + 1][c]
                    dp[r + 1][c][new_xor] = (dp[r + 1][c][new_xor] + dp[r][c][val]) % MOD
                    
    return dp[m - 1][n - 1][k]
