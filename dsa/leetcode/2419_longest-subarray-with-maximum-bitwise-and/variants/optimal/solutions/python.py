from typing import List

def solve(nums: List[int]) -> int:
    """
    Finds the length of the longest contiguous subarray whose bitwise AND
    is equal to the maximum value in the array.
    """
    if not nums:
        return 0
    
    # The maximum bitwise AND of any subarray is the maximum element in the array.
    # This is because x & y <= min(x, y) <= max(x, y).
    max_val = max(nums)
    
    max_len = 0
    current_len = 0
    
    for x in nums:
        if x == max_val:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 0
            
    return max_len
