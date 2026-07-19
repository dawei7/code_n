from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the K-or of an array by checking the frequency of set bits
    at each position from 0 to 31.
    """
    k_or_result = 0
    
    # Iterate through each bit position (assuming 32-bit integers)
    for i in range(32):
        count = 0
        mask = 1 << i
        
        # Count how many numbers have the i-th bit set
        for num in nums:
            if num & mask:
                count += 1
        
        # If the count meets the threshold k, set the i-th bit in the result
        if count >= k:
            k_or_result |= mask
            
    return k_or_result
