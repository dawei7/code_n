def solve(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    
    # Precompute cost to make each column 'j' consist entirely of digit 'v'
    # cost[j][v] = m - (count of v in column j)
    costs = [[m for _ in range(10)] for _ in range(n)]
    for j in range(n):
        counts = [0] * 10
        for i in range(m):
            counts[grid[i][j]] += 1
        for v in range(10):
            costs[j][v] = m - counts[v]
            
    # dp[v] stores the min cost to satisfy columns up to current, 
    # ending with the current column having value 'v'
    dp = [costs[0][v] for v in range(10)]
    
    for j in range(1, n):
        new_dp = [float('inf')] * 10
        # To optimize finding the min of previous dp excluding current v:
        # Find the two smallest values in the previous dp table
        first_min = float('inf')
        second_min = float('inf')
        first_idx = -1
        
        for v in range(10):
            if dp[v] < first_min:
                second_min = first_min
                first_min = dp[v]
                first_idx = v
            elif dp[v] < second_min:
                second_min = dp[v]
        
        for v in range(10):
            prev_min = second_min if v == first_idx else first_min
            new_dp[v] = costs[j][v] + prev_min
        dp = new_dp
        
    return min(dp)
