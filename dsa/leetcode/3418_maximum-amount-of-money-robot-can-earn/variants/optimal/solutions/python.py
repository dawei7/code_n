def solve(coins: list[list[int]]) -> int:
    rows = len(coins)
    cols = len(coins[0])
    
    # dp[i][j][k] = max money at (i, j) having neutralized k negative values
    # Initialize with negative infinity to represent unreachable states
    inf = float('inf')
    dp = [[[ -inf for _ in range(3)] for _ in range(cols)] for _ in range(rows)]
    
    # Base case: starting cell
    val = coins[0][0]
    if val < 0:
        dp[0][0][0] = val
        dp[0][0][1] = 0
    else:
        dp[0][0][0] = val
        
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                continue
            
            # Possible previous cells
            prevs = []
            if i > 0: prevs.append(dp[i-1][j])
            if j > 0: prevs.append(dp[i][j-1])
            
            curr_val = coins[i][j]
            
            for prev_dp in prevs:
                for k in range(3):
                    if prev_dp[k] == -inf:
                        continue
                    
                    # Option 1: Don't neutralize current cell
                    dp[i][j][k] = max(dp[i][j][k], prev_dp[k] + curr_val)
                    
                    # Option 2: Neutralize current cell if it's negative and we have charges left
                    if curr_val < 0 and k < 2:
                        dp[i][j][k+1] = max(dp[i][j][k+1], prev_dp[k])
                        
    return max(dp[rows-1][cols-1])
