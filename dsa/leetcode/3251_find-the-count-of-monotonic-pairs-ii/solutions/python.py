def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    max_val = max(nums)
    
    # dp[j] stores the number of ways to have arr1[i] = j
    # Initially for i = 0, arr1[0] can be any value from 0 to nums[0]
    dp = [1] * (max_val + 1)
    
    for i in range(1, n):
        new_dp = [0] * (max_val + 1)
        prefix_sum = [0] * (max_val + 2)
        
        # Build prefix sum of the previous dp state
        for j in range(max_val + 1):
            prefix_sum[j + 1] = (prefix_sum[j] + dp[j]) % MOD
            
        for j in range(nums[i] + 1):
            # arr1[i-1] <= j
            # arr2[i] <= arr2[i-1] => nums[i]-j <= nums[i-1]-arr1[i-1]
            # => arr1[i-1] <= nums[i-1] - nums[i] + j
            upper = min(j, nums[i-1] - nums[i] + j)
            
            if upper >= 0:
                # Sum of dp[0...upper]
                limit = min(upper, nums[i-1])
                new_dp[j] = prefix_sum[limit + 1]
        
        dp = new_dp
        
    return sum(dp) % MOD
