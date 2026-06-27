def solve(nums: list[int], k: int) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    
    # dp[i][j] = number of subsequences of length i that sum to j
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for x in nums:
        for i in range(n - 1, -1, -1):
            for j in range(k - x, -1, -1):
                if dp[i][j] > 0:
                    dp[i + 1][j + x] = (dp[i + 1][j + x] + dp[i][j]) % MOD
                    
    # Precompute powers of 2
    pow2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pow2[i] = (pow2[i - 1] * 2) % MOD
        
    ans = 0
    # For a subsequence of length i that sums to k, 
    # there are 2^(n-i) total subsequences that contain it.
    for i in range(1, n + 1):
        if dp[i][k] > 0:
            contribution = (dp[i][k] * pow2[n - i]) % MOD
            ans = (ans + contribution) % MOD
            
    return ans
