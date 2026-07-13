from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    """
    dp[val][i] stores the maximum length of a subsequence ending with 'val'
    having exactly 'i' adjacent unequal pairs.
    """
    # dp[val][i]
    dp = defaultdict(lambda: [0] * (k + 1))
    
    # max_len_with_i[i] stores the maximum length of any subsequence 
    # ending with any value having exactly 'i' unequal pairs.
    max_len_with_i = [0] * (k + 1)
    
    for x in nums:
        new_dp_x = [0] * (k + 1)
        for i in range(k + 1):
            # Option 1: Extend a subsequence ending in x (no new unequal pair)
            new_dp_x[i] = dp[x][i] + 1
            
            # Option 2: Extend a subsequence ending in a different value (new unequal pair)
            if i > 0:
                new_dp_x[i] = max(new_dp_x[i], max_len_with_i[i - 1] + 1)
        
        # Update the DP table for value x
        for i in range(k + 1):
            dp[x][i] = max(dp[x][i], new_dp_x[i])
            max_len_with_i[i] = max(max_len_with_i[i], dp[x][i])
            
    return max(max_len_with_i)
