from typing import List

def solve(cost: List[int], time: List[int]) -> int:
    n = len(cost)
    # dp[j] will store the minimum cost to paint at least j walls
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for c, t in zip(cost, time):
        # Iterate backwards to prevent using the same wall multiple times
        for j in range(n, 0, -1):
            dp[j] = min(dp[j], dp[max(0, j - (t + 1))] + c)
            
    return int(dp[n])
