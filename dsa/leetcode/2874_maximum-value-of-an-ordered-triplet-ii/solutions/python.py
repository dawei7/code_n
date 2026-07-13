def solve(nums: list[int]) -> int:
    """
    Calculates the maximum value of (nums[i] - nums[j]) * nums[k] 
    for i < j < k using a single-pass approach.
    """
    max_val = 0
    max_i = 0
    max_diff = 0
    
    for x in nums:
        # If we treat the current element as nums[k],
        # the result is max_diff * x.
        max_val = max(max_val, max_diff * x)
        
        # Update max_diff: the best (nums[i] - nums[j]) seen so far.
        # This is either the previous max_diff or (max_i - current_element).
        max_diff = max(max_diff, max_i - x)
        
        # Update max_i: the maximum value of nums[i] seen so far.
        max_i = max(max_i, x)
        
    return max_val
