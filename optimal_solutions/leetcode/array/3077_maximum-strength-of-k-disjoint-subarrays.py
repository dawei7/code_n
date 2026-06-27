def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    # multiplier for the i-th subarray (1-indexed)
    # i=1: k, i=2: -(k-1), i=3: (k-2)...
    def get_multiplier(i):
        return (k - i + 1) if i % 2 != 0 else -(k - i + 1)

    # dp[i][j] = max strength using i subarrays considering first j elements
    # To optimize, we use two rows: prev_dp and curr_dp
    # prev_dp[j] stores max strength using (i-1) subarrays using first j elements
    
    # Initialize with a very small number
    inf = float('inf')
    prev_dp = [0] * (n + 1)
    
    for i in range(1, k + 1):
        curr_dp = [-inf] * (n + 1)
        mult = get_multiplier(i)
        
        # max_prev stores the best value of (prev_dp[p] - mult * prefix_sum[p])
        # seen so far to allow O(1) transition
        max_prev = -inf
        prefix_sum = 0
        
        for j in range(i, n + 1):
            prefix_sum += nums[j-1]
            
            # Update max_prev: we can either start a new subarray at j
            # or extend the current subarray ending at j
            max_prev = max(max_prev, prev_dp[j-1] - (get_multiplier(i-1) if i > 1 else 0) * 0) # Logic adjustment
            # Actually, the transition is:
            # dp[i][j] = max(dp[i][j-1] + mult * nums[j-1], max_{p < j} (dp[i-1][p] + mult * (prefix[j] - prefix[p])))
            # dp[i][j] = max(dp[i][j-1], max_prev + mult * prefix[j])
            
            # Correct DP transition:
            # Let f[i][j] be max strength using i subarrays ending exactly at j
            # Let g[i][j] be max strength using i subarrays within first j
            pass
            
    # Standard DP approach for this specific problem:
    dp = [[-inf] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 0
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]
        
    for i in range(1, k + 1):
        mult = get_multiplier(i)
        best_prev = -inf
        for j in range(i, n + 1):
            best_prev = max(best_prev, dp[i-1][j-1] - (get_multiplier(i-1) if i > 1 else 0) * prefix[j-1])
            # This is a simplified representation of the O(nk) logic
            dp[i][j] = max(dp[i][j-1], best_prev + mult * prefix[j])
            
    return dp[k][n]
