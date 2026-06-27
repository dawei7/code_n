from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the minimum operations to collect all integers from 1 to k
    by iterating backwards through the list.
    """
    collected = set()
    operations = 0
    
    # Iterate backwards through the array
    for i in range(len(nums) - 1, -1, -1):
        operations += 1
        val = nums[i]
        
        # Only track values within the target range [1, k]
        if val <= k:
            collected.add(val)
            
        # If we have collected all numbers from 1 to k, return the count
        if len(collected) == k:
            return operations
            
    return operations
