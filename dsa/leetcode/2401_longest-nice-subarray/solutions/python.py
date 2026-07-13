from typing import List

def solve(nums: List[int]) -> int:
    """
    Finds the length of the longest contiguous subarray where every pair
    of elements has a bitwise AND result of zero.
    """
    max_len = 0
    left = 0
    used_bits = 0
    
    for right in range(len(nums)):
        # While the current number shares bits with the existing window,
        # shrink the window from the left.
        while (used_bits & nums[right]) != 0:
            used_bits ^= nums[left]
            left += 1
        
        # Add the current number's bits to the window
        used_bits |= nums[right]
        
        # Update the maximum length found so far
        max_len = max(max_len, right - left + 1)
        
    return max_len
