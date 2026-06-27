def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    # dp[i][j] is the min cost to partition nums[0...i-1] into j subarrays
    # Initialize with infinity
    inf = float('inf')
    dp = [[inf] * (k + 1) for _ in range(n + 1)]
    
    # Base case: 0 elements, 0 subarrays cost 0
    dp[0][0] = 0
    
    # Fill DP table
    # i is the number of elements used
    # j is the number of subarrays formed
    for j in range(1, k + 1):
        for i in range(1, n + 1):
            # We want to form the j-th subarray ending at i-1
            # The j-th subarray starts at index 'p' and ends at 'i-1'
            # Cost of this subarray is nums[p] + nums[i-1]
            # We need at least j-1 elements to form j-1 subarrays
            for p in range(j - 1, i):
                if dp[p][j - 1] != inf:
                    cost = nums[p] + nums[i - 1]
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost)
                    
    return dp[n][k]
