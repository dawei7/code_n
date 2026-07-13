from typing import List

def solve(nums: List[int]) -> List[int]:
    """
    Transforms the array by mapping each index i to the value at (i + nums[i]) % n.
    Python's modulo operator handles negative numbers correctly for circular indexing.
    """
    n = len(nums)
    result = [0] * n
    
    for i in range(n):
        # Calculate the target index using modulo arithmetic
        # Python's % operator ensures the result is always in [0, n-1]
        target_index = (i + nums[i]) % n
        result[i] = nums[target_index]
        
    return result
