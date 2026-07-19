def solve(nums: list[int], k: int, m: int) -> int:
    n = len(nums)
    # prefix_sum[i] is sum of nums[0...i-1]
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    # dp[i][j] = max sum using i subarrays from first j elements
    # Initialize with a very small number
    inf = float('inf')
    dp = [[-inf] * (n + 1) for _ in range(k + 1)]
    
    # Base case: 0 subarrays have sum 0
    for j in range(n + 1):
        dp[0][j] = 0
        
    for i in range(1, k + 1):
        # max_prev stores the best value of (dp[i-1][p] - prefix_sum[p])
        # where p <= j - m
        max_prev = -inf
        for j in range(m * i, n + 1):
            # We can start the i-th subarray at index p, ending at j-1
            # The i-th subarray is nums[p...j-1], length is j-p >= m => p <= j-m
            p = j - m
            max_prev = max(max_prev, dp[i - 1][p] - prefix_sum[p])
            
            # Option 1: Don't include nums[j-1] in the i-th subarray
            # Option 2: Include nums[j-1] as the end of the i-th subarray
            dp[i][j] = max(dp[i][j - 1], max_prev + prefix_sum[j])
            
    return dp[k][n]
