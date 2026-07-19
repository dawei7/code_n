from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the maximum total cost of alternating subarrays using DP.
    
    dp0: Max cost ending at i where nums[i] is the start of a subarray (added).
    dp1: Max cost ending at i where nums[i] is the second+ element (subtracted).
    """
    if not nums:
        return 0
    
    # Initialize DP states for the first element
    # dp0: nums[0] is added
    # dp1: Not possible for the first element, use -infinity
    dp0 = nums[0]
    dp1 = float('-inf')
    
    for i in range(1, len(nums)):
        # To calculate new_dp0: nums[i] starts a new subarray.
        # It can follow either a dp0 or dp1 state from the previous index.
        new_dp0 = max(dp0, dp1) + nums[i]
        
        # To calculate new_dp1: nums[i] is subtracted.
        # It must follow a state where nums[i-1] was the start of a subarray.
        new_dp1 = dp0 - nums[i]
        
        dp0, dp1 = new_dp0, new_dp1
        
    return max(dp0, dp1)
