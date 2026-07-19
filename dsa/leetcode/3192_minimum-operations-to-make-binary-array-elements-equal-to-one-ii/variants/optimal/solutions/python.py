from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the minimum operations to make all elements 1.
    We track the number of flips performed. If the current element's 
    effective value (original value XORed with flip parity) is 0, 
    we must perform a flip.
    """
    flips = 0
    for num in nums:
        # If flips is even, the current element is unchanged.
        # If flips is odd, the current element is inverted.
        # We need the effective value to be 1.
        if (num + flips) % 2 == 0:
            flips += 1
            
    return flips
