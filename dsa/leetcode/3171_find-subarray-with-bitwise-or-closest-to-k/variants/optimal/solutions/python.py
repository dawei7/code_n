def solve(nums: list[int], k: int) -> int:
    """
    Finds the minimum absolute difference between k and the bitwise OR 
    of any contiguous subarray.
    """
    ans = float('inf')
    # active_ors stores the set of bitwise OR values of all subarrays 
    # ending at the previous index, mapped to their last seen index 
    # (though here we just need the values).
    # Because OR is monotonic, there are at most 30 distinct values.
    active_ors = set()
    
    for x in nums:
        # New set of OR values ending at current index
        new_ors = {x}
        for val in active_ors:
            new_ors.add(val | x)
        
        # Update the global minimum difference
        for val in new_ors:
            diff = abs(val - k)
            if diff < ans:
                ans = diff
        
        active_ors = new_ors
        
        # Optimization: if we found 0, we can't do better
        if ans == 0:
            return 0
            
    return int(ans)
