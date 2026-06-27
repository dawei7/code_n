import math

def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    max_val = max(nums)
    
    # dp[g1][g2] stores the number of ways to have two disjoint subsequences
    # with GCDs g1 and g2.
    # We use a dictionary or a 2D array. Given max_val is 200, 201x201 is fine.
    dp = [[0] * (max_val + 1) for _ in range(max_val + 1)]
    
    for x in nums:
        new_dp = [row[:] for row in dp]
        
        # Case 1: x starts a new subsequence
        new_dp[x][0] = (new_dp[x][0] + 1) % MOD
        new_dp[0][x] = (new_dp[0][x] + 1) % MOD
        
        # Case 2: x is added to existing subsequences
        for g1 in range(1, max_val + 1):
            if dp[g1][0] > 0:
                new_g1 = math.gcd(g1, x)
                new_dp[new_g1][0] = (new_dp[new_g1][0] + dp[g1][0]) % MOD
            
            if dp[0][g1] > 0:
                new_g2 = math.gcd(g1, x)
                new_dp[0][new_g2] = (new_dp[0][new_g2] + dp[0][g1]) % MOD
                
            for g2 in range(1, max_val + 1):
                if dp[g1][g2] > 0:
                    # Add to first
                    ng1 = math.gcd(g1, x)
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + dp[g1][g2]) % MOD
                    # Add to second
                    ng2 = math.gcd(g2, x)
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + dp[g1][g2]) % MOD
        
        dp = new_dp
        
    ans = 0
    for i in range(1, max_val + 1):
        ans = (ans + dp[i][i]) % MOD
        
    return ans
