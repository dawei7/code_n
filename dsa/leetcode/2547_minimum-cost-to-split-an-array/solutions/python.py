def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    # dp[i] will store the minimum cost to partition nums[0...i-1]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # Precompute trimming costs for all subarrays [j, i-1]
    # cost[j][i] = number of elements that appear more than once in nums[j...i]
    # Since we need this for DP, we can compute it on the fly.
    
    for i in range(1, n + 1):
        freq = {}
        trimming_cost = 0
        # Iterate backwards to build the subarray nums[j...i-1]
        for j in range(i - 1, -1, -1):
            val = nums[j]
            freq[val] = freq.get(val, 0) + 1
            
            if freq[val] == 2:
                # This element now contributes to the trimming cost
                trimming_cost += 2
            elif freq[val] > 2:
                # This element was already contributing, now it adds 1 more
                trimming_cost += 1
            
            current_subarray_cost = k + trimming_cost
            if dp[j] + current_subarray_cost < dp[i]:
                dp[i] = dp[j] + current_subarray_cost
                
    return int(dp[n])
