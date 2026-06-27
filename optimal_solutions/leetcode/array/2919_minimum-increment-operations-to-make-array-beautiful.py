def solve(nums: list[int], k: int) -> int:
    # dp[i] stores the minimum increments to make the subarray ending at i valid,
    # where nums[i] is the element that was increased to be >= k.
    # We only need the last 3 states to calculate the next state.
    
    n = len(nums)
    # dp[i] = max(0, k - nums[i]) + min(dp[i-1], dp[i-2], dp[i-3])
    # Initialize with the first three elements
    dp = [0] * n
    
    for i in range(n):
        cost = max(0, k - nums[i])
        if i < 3:
            dp[i] = cost
        else:
            dp[i] = cost + min(dp[i-1], dp[i-2], dp[i-3])
            
    # The answer is the minimum of the last three positions, 
    # because the last window of 3 must contain at least one element >= k.
    return min(dp[n-1], dp[n-2], dp[n-3])
