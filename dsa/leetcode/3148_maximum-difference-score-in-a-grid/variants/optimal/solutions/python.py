def solve(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    
    # dp[i][j] will store the minimum value in the region 
    # that can reach cell (i, j) from the top or left.
    dp = [[0] * n for _ in range(m)]
    max_score = float('-inf')
    
    for i in range(m):
        for j in range(n):
            min_prev = float('inf')
            
            # Check cell above
            if i > 0:
                min_prev = min(min_prev, dp[i-1][j], grid[i-1][j])
            
            # Check cell to the left
            if j > 0:
                min_prev = min(min_prev, dp[i][j-1], grid[i][j-1])
            
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            else:
                max_score = max(max_score, grid[i][j] - min_prev)
                dp[i][j] = min(grid[i][j], min_prev)
                
    return int(max_score)
