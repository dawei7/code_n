from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the maximum length of a consecutive sequence after 
    incrementing each element by at most 1.
    """
    if not nums:
        return 0
    
    # Sort the numbers to process them in order
    nums.sort()
    
    # dp[v] stores the length of the longest consecutive sequence 
    # ending with the value v.
    dp = {}
    max_len = 0
    
    for x in nums:
        # For each number x, we have two choices:
        # 1. Use x as is: it extends a sequence ending at x-1.
        # 2. Use x+1: it extends a sequence ending at x.
        
        # We check the potential lengths for both options.
        # We update in reverse order of potential values to avoid 
        # using the same element twice for the same sequence.
        
        val_plus_one = dp.get(x, 0) + 1
        val_orig = dp.get(x - 1, 0) + 1
        
        # Update the DP table for x+1 and x
        # We take the max because we might have seen these values before
        dp[x + 1] = max(dp.get(x + 1, 0), val_plus_one)
        dp[x] = max(dp.get(x, 0), val_orig)
        
        max_len = max(max_len, dp[x + 1], dp[x])
        
    return max_len
