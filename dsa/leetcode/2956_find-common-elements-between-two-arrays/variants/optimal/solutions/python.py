from typing import List

def solve(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Calculates the number of common elements between two arrays from the 
    perspective of each array.
    """
    set1 = set(nums1)
    set2 = set(nums2)
    
    count1 = sum(1 for x in nums1 if x in set2)
    count2 = sum(1 for x in nums2 if x in set1)
    
    return [count1, count2]
