from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the minimum number of bit flips to make the XOR sum of nums equal to k.
    """
    # Calculate the XOR sum of all elements in the array
    current_xor = 0
    for num in nums:
        current_xor ^= num
    
    # The bits that need to be flipped are exactly the bits that differ
    # between the current_xor and the target k.
    # XORing current_xor and k gives a number where each set bit 
    # represents a difference at that position.
    diff = current_xor ^ k
    
    # The number of operations is the count of set bits (population count)
    return bin(diff).count('1')
