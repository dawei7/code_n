from typing import List

def solve(nums1: List[int], nums2: List[int], k: int) -> int:
    """
    Calculates the number of good pairs (i, j) such that 
    nums1[i] is divisible by (nums2[j] * k).
    """
    count = 0
    # Pre-calculate the modified values of nums2 to avoid redundant multiplication
    multipliers = [x * k for x in nums2]
    
    for val1 in nums1:
        for val2_mod in multipliers:
            if val1 % val2_mod == 0:
                count += 1
                
    return count
