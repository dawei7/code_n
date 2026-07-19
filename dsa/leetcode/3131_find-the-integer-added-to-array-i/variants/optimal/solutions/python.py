from typing import List

def solve(nums1: List[int], nums2: List[int]) -> int:
    """
    Calculates the integer x added to each element of nums1 to produce nums2.
    Since nums2[i] = nums1[i] + x, it follows that min(nums2) = min(nums1) + x.
    Therefore, x = min(nums2) - min(nums1).
    """
    return min(nums2) - min(nums1)
