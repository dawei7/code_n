def solve(fruits: list[list[int]]) -> int:
    n = len(fruits)
    total_fruits = 0
    
    # Path 1: Down-Right diagonal (0,0) to (n-1, n-1)
    for i in range(n):
        total_fruits += fruits[i][i]
        
    # Path 2: Down-Left from (0, n-1) to (n-1, n-1)
    # We can only move to (r+1, c-1) or (r+1, c+1) - but here restricted to grid
    # DP state: dp[r][c] is max fruits to reach (r, c)
    dp2 = [[0] * n for _ in range(n)]
    dp2[0][n-1] = fruits[0][n-1]
    for r in range(1, n):
        for c in range(n - 1 - r, n):
            prev = dp2[r-1][c]
            if c + 1 < n: prev = max(prev, dp2[r-1][c+1])
            if c - 1 >= 0: prev = max(prev, dp2[r-1][c-1])
            dp2[r][c] = fruits[r][c] + prev
            
    # The path ends at the bottom row (n-1, c) where c < n-1
    # Actually, the problem defines specific paths:
    # Path 2 ends at (n-1, n-1) is not possible if we only move down-left.
    # The paths are: (0,0)->(n-1, n-1), (0, n-1)->(n-1, n-1), (n-1, 0)->(n-1, n-1)
    # Correcting logic:
    
    # Path 2: Start (0, n-1), end at row n-1, column > n-1-r
    # Path 3: Start (n-1, 0), end at col n-1, row > n-1-c
    
    def get_max_path(start_r, start_c, dr, dc_range):
        dp = [[-1] * n for _ in range(n)]
        dp[start_r][start_c] = fruits[start_r][start_c]
        for r in range(start_r + 1, n):
            for c in range(n):
                if not (0 <= c < n): continue
                best = -1
                for prev_c in [c-1, c, c+1]:
                    if 0 <= prev_c < n and dp[r-1][prev_c] != -1:
                        best = max(best, dp[r-1][prev_c])
                if best != -1:
                    dp[r][c] = fruits[r][c] + best
        return dp
    
    # Simplified approach for the specific constraints of the problem:
    # Path 1: (0,0) to (n-1, n-1)
    res = 0
    for i in range(n): res += fruits[i][i]
    
    # Path 2: (0, n-1) to (n-1, n-1)
    dp2 = [[0]*n for _ in range(n)]
    dp2[0][n-1] = fruits[0][n-1]
    for i in range(1, n):
        for j in range(n-1-i, n):
            vals = [dp2[i-1][j]]
            if j > 0: vals.append(dp2[i-1][j-1])
            if j < n-1: vals.append(dp2[i-1][j+1])
            dp2[i][j] = fruits[i][j] + max(vals)
    res += dp2[n-1][n-1]
    
    # Path 3: (n-1, 0) to (n-1, n-1)
    dp3 = [[0]*n for _ in range(n)]
    dp3[n-1][0] = fruits[n-1][0]
    for j in range(1, n):
        for i in range(n-1-j, n):
            vals = [dp3[i][j-1]]
            if i > 0: vals.append(dp3[i-1][j-1])
            if i < n-1: vals.append(dp3[i+1][j-1])
            dp3[i][j] = fruits[i][j] + max(vals)
    res += dp3[n-1][n-1]
    
    return res
