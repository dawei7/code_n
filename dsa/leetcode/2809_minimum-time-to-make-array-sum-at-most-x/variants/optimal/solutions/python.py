def solve(nums1: list[int], nums2: list[int], x: int) -> int:
    n = len(nums1)
    # Pair elements to sort by growth rate (nums2)
    pairs = sorted(zip(nums2, nums1))
    
    # dp[j] will store the maximum sum reduction possible using j operations
    # after processing some prefix of the sorted pairs.
    dp = [0] * (n + 1)
    
    # Total sum of nums1 if we did nothing
    sum1 = sum(nums1)
    # Total sum of nums2
    sum2 = sum(nums2)
    
    for i in range(n):
        b, a = pairs[i]
        # Update DP table backwards to avoid using the same element twice
        for j in range(i + 1, 0, -1):
            # If we perform j operations, the current element contributes
            # its initial value 'a' plus its growth 'b * j' to the reduction.
            dp[j] = max(dp[j], dp[j - 1] + a + b * j)
            
    for t in range(n + 1):
        # The sum after t seconds is:
        # (Initial sum1 + t * sum2) - (reduction achieved by t operations)
        if sum1 + t * sum2 - dp[t] <= x:
            return t
            
    return -1
