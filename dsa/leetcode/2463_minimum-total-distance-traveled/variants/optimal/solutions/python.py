def solve(robot: list[int], factory: list[list[int]]) -> int:
    robot.sort()
    factory.sort()
    
    n = len(robot)
    m = len(factory)
    
    # dp[i][j] is the min cost to repair first i robots using first j factories
    # Initialize with infinity
    inf = float('inf')
    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    
    # Base case: 0 robots cost 0 to repair
    for j in range(m + 1):
        dp[0][j] = 0
        
    for j in range(1, m + 1):
        f_pos, f_limit = factory[j-1]
        for i in range(n + 1):
            # Option 1: Don't use this factory at all
            dp[i][j] = dp[i][j-1]
            
            # Option 2: Use this factory to repair k robots (1 <= k <= f_limit)
            cost = 0
            for k in range(1, min(i, f_limit) + 1):
                cost += abs(robot[i - k] - f_pos)
                if dp[i - k][j - 1] != inf:
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + cost)
                    
    return dp[n][m]
