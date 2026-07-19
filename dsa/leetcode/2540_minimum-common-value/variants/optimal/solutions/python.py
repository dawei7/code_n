from typing import List

def solve(nums1: List[int], nums2: List[int]) -> int:
    """
    Finds the minimum common value in two sorted arrays using the two-pointer technique.
    """
    i, j = 0, 0
    n, m = len(nums1), len(nums2)
    
    while i < n and j < m:
        if nums1[i] == nums2[j]:
            return nums1[i]
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
            
    return -1
