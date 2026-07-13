def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    max_val = max(nums)
    
    # dp[v] stores the number of ways to have arr1[i] = v
    # Initialize for i = 0: arr1[0] can be any value from 0 to nums[0]
    dp = [1] * (max_val + 1)
    for v in range(max_val + 1):
        if v > nums[0]:
            dp[v] = 0
            
    for i in range(1, n):
        new_dp = [0] * (max_val + 1)
        # Prefix sums of the previous dp state to optimize transition
        prefix_sum = [0] * (max_val + 2)
        for v in range(max_val + 1):
            prefix_sum[v + 1] = (prefix_sum[v] + dp[v]) % MOD
            
        for v in range(nums[i] + 1):
            # Conditions:
            # 1. arr1[i-1] <= v
            # 2. arr2[i-1] >= arr2[i] => nums[i-1] - arr1[i-1] >= nums[i] - v
            #    => arr1[i-1] <= v - (nums[i] - nums[i-1])
            # So, arr1[i-1] <= min(v, v - nums[i] + nums[i-1])
            
            upper = min(v, v - nums[i] + nums[i-1])
            if upper >= 0:
                # Sum of dp[0...upper]
                limit = min(upper, nums[i-1])
                new_dp[v] = prefix_sum[limit + 1]
        dp = new_dp
        
    return sum(dp) % MOD
