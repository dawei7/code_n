def solve(target: int, types: list[list[int]]) -> int:
    MOD = 10**9 + 7
    
    # dp[i] stores the number of ways to get a total score of i
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for count, marks in types:
        new_dp = [0] * (target + 1)
        # We use a prefix sum approach to update the DP table efficiently.
        # For a specific question type with 'count' items of 'marks' value:
        # new_dp[j] = sum(dp[j - k * marks]) for 0 <= k <= count
        # This is equivalent to:
        # new_dp[j] = new_dp[j - marks] + dp[j] - dp[j - (count + 1) * marks]
        
        for j in range(target + 1):
            # Current ways to reach j using previous types
            new_dp[j] = dp[j]
            
            # Add ways by taking 1 to 'count' items of current type
            if j >= marks:
                new_dp[j] = (new_dp[j] + new_dp[j - marks]) % MOD
            
            # Subtract ways that exceed the 'count' limit
            if j >= (count + 1) * marks:
                new_dp[j] = (new_dp[j] - dp[j - (count + 1) * marks] + MOD) % MOD
        
        dp = new_dp
        
    return dp[target]
