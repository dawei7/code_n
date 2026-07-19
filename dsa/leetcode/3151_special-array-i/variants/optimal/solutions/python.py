from typing import List

def solve(nums: List[int]) -> bool:
    """
    Determines if an array is 'special' by checking if all adjacent 
    elements have different parity.
    """
    if len(nums) <= 1:
        return True
    
    for i in range(len(nums) - 1):
        # Check if both numbers have the same parity
        # If (a % 2) == (b % 2), they are both even or both odd
        if nums[i] % 2 == nums[i + 1] % 2:
            return False
            
    return True
