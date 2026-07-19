from typing import List

def solve(nums: List[int]) -> int:
    """
    To make the array non-decreasing, we want to keep the longest subsequence 
    that is already in the form 1...1, 2...2, 3...3.
    
    Let dp[i] be the minimum operations to make the prefix of the array 
    sorted such that the last element is of type i (where i is 1, 2, or 3).
    
    - If current is 1:
        dp[1] = dp[1]
        dp[2] = dp[2] + 1
        dp[3] = dp[3] + 1
    - If current is 2:
        dp[1] = dp[1] + 1
        dp[2] = min(dp[1], dp[2])
        dp[3] = dp[3] + 1
    - If current is 3:
        dp[1] = dp[1] + 1
        dp[2] = dp[2] + 1
        dp[3] = min(dp[1], dp[2], dp[3])
    """
    # dp[i] stores the min operations to have a sorted sequence ending in value (i+1)
    dp = [0, 0, 0]
    
    for x in nums:
        if x == 1:
            # To end in 1: no change needed
            # To end in 2: must change 1 to 2
            # To end in 3: must change 1 to 3
            dp[0] = dp[0]
            dp[1] = dp[1] + 1
            dp[2] = dp[2] + 1
        elif x == 2:
            # To end in 1: must change 2 to 1
            # To end in 2: min of ending in 1 or 2
            # To end in 3: must change 2 to 3
            dp[0] = dp[0] + 1
            dp[1] = min(dp[0] - 1, dp[1])
            dp[2] = dp[2] + 1
        else: # x == 3
            # To end in 1: must change 3 to 1
            # To end in 2: must change 3 to 2
            # To end in 3: min of ending in 1, 2, or 3
            dp[0] = dp[0] + 1
            dp[1] = dp[1] + 1
            dp[2] = min(dp[0] - 1, dp[1] - 1, dp[2])
            
    return min(dp)
