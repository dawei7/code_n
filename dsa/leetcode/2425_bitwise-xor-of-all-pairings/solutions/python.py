from typing import List

def solve(nums1: List[int], nums2: List[int]) -> int:
    """
    Calculates the XOR sum of all pairs (x, y) where x in nums1 and y in nums2.
    If len(nums2) is odd, all elements in nums1 contribute to the result.
    If len(nums1) is odd, all elements in nums2 contribute to the result.
    """
    xor1 = 0
    xor2 = 0
    
    if len(nums2) % 2 == 1:
        for num in nums1:
            xor1 ^= num
            
    if len(nums1) % 2 == 1:
        for num in nums2:
            xor2 ^= num
            
    return xor1 ^ xor2
