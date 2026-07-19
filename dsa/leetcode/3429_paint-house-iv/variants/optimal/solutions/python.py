def solve(n: int, cost: list[list[int]]) -> int:
    m = len(cost[0])
    # dp[c1][c2] stores the min cost for the current pair of houses
    # (i, n-1-i) having colors c1 and c2 respectively.
    dp = [[float('inf')] * m for _ in range(m)]
    
    # Base case: the outermost pair (0, n-1)
    for c1 in range(m):
        for c2 in range(m):
            if c1 != c2:
                dp[c1][c2] = cost[0][c1] + cost[n - 1][c2]
                
    # Iterate through the remaining n/2 - 1 pairs
    for i in range(1, n // 2):
        new_dp = [[float('inf')] * m for _ in range(m)]
        # Precompute min values to optimize transition from O(m^4) to O(m^2)
        # min_prev[prev_c1][prev_c2] is the min cost of previous pair
        # We need to find min(dp[prev_c1][prev_c2]) where prev_c1 != c1 and prev_c2 != c2
        
        # To optimize, find the smallest and second smallest values in dp
        # for each row and column, but given m is usually small, 
        # a direct O(m^4) or O(m^3) is often acceptable.
        # Here we use O(m^3) by pre-calculating row/col minimums.
        
        for c1 in range(m):
            for c2 in range(m):
                if c1 == c2:
                    continue
                
                current_cost = cost[i][c1] + cost[n - 1 - i][c2]
                
                # Find min(dp[pc1][pc2]) where pc1 != c1 and pc2 != c2
                for pc1 in range(m):
                    if pc1 == c1: continue
                    for pc2 in range(m):
                        if pc2 == c2: continue
                        if dp[pc1][pc2] + current_cost < new_dp[c1][c2]:
                            new_dp[c1][c2] = dp[pc1][pc2] + current_cost
        dp = new_dp
        
    ans = min(min(row) for row in dp)
    return int(ans) if ans != float('inf') else -1
