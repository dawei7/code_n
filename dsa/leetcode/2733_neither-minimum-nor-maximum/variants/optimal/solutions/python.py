from typing import List

def solve(nums: List[int]) -> int:
    """
    Returns any number from the array that is neither the minimum nor the maximum.
    Returns -1 if no such number exists.
    """
    if len(nums) < 3:
        return -1
    
    # Take the first 3 elements, sort them, and return the middle one.
    first_three = nums[:3]
    first_three.sort()
    return first_three[1]
