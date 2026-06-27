def solve(n: int, requirements: list[list[int]]) -> int:
    MOD = 10**9 + 7
    
    # Map requirements for quick lookup
    req_map = {}
    max_inv = 0
    for end, cnt in requirements:
        req_map[end] = cnt
        max_inv = max(max_inv, cnt)
    
    # dp[j] stores the number of permutations of current length with j inversions
    dp = [0] * (max_inv + 1)
    dp[0] = 1
    
    for i in range(n):
        new_dp = [0] * (max_inv + 1)
        
        # Prefix sum array to optimize the transition:
        # dp[i][j] = sum(dp[i-1][j-k]) for 0 <= k < i
        prefix_sum = [0] * (max_inv + 2)
        for j in range(max_inv + 1):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MOD
            
        for j in range(max_inv + 1):
            # The number of inversions we can add by placing the current element
            # at position i is between 0 and i.
            # So we sum dp[i-1] from j-i to j.
            lower = max(0, j - i)
            new_dp[j] = (prefix_sum[j + 1] - prefix_sum[lower]) % MOD
            
        # Apply constraints if they exist for the current index i
        if i in req_map:
            target = req_map[i]
            for j in range(max_inv + 1):
                if j != target:
                    new_dp[j] = 0
        
        dp = new_dp
        
    return dp[req_map.get(n - 1, 0)] % MOD
