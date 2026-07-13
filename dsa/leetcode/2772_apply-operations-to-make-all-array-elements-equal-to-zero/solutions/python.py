def solve(nums: list[int], k: int) -> bool:
    n = len(nums)
    # diff[i] will store the value subtracted starting at index i
    diff = [0] * (n + 1)
    current_subtraction = 0
    
    for i in range(n):
        current_subtraction += diff[i]
        
        # The effective value of nums[i] after previous operations
        val = nums[i] - current_subtraction
        
        if val == 0:
            continue
        elif val < 0 or i + k > n:
            # Cannot reduce further or not enough elements left for a window of size k
            return False
        else:
            # Apply operation: subtract 'val' from [i, i + k - 1]
            current_subtraction += val
            # Mark the end of the effect of this operation
            if i + k < n:
                diff[i + k] -= val
                
    return True
