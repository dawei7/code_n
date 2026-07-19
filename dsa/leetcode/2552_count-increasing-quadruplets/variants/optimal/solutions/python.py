def solve(nums: list[int]) -> int:
    n = len(nums)
    # dp[j] will store the number of pairs (i, k) such that 
    # i < j < k and nums[i] < nums[k] < nums[j]
    # However, a more efficient approach is to track the number of 
    # increasing triplets (i, j, k) ending at k with nums[i] < nums[k] < nums[j]
    
    # count[j] will store the number of pairs (i, k) such that 
    # i < k < j and nums[i] < nums[j] < nums[k]
    # This is a variation of the O(n^2) DP approach.
    
    dp = [0] * n
    ans = 0
    
    for j in range(n):
        # count_smaller_before_j tracks how many elements 
        # to the left of j are smaller than nums[k]
        count_smaller_before_j = 0
        for k in range(j):
            if nums[k] < nums[j]:
                # Every time we find a k < j with nums[k] < nums[j],
                # the existing dp[k] represents pairs (i, k) 
                # where i < k and nums[i] < nums[j] (since nums[i] < nums[k] < nums[j])
                ans += dp[k]
                count_smaller_before_j += 1
            elif nums[k] > nums[j]:
                # If nums[k] > nums[j], this k can act as the 'k' in (i, j, k, l)
                # We add the number of elements smaller than nums[k] found so far
                dp[k] += count_smaller_before_j
                
    return ans
