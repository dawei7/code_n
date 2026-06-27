from typing import List

def solve(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Finds the intersection of two arrays using a hash set for O(n+m) performance.
    """
    # Convert the first list to a set for O(1) lookups
    set1 = set(nums1)
    # Use a set for the result to automatically handle uniqueness
    result_set = set()
    
    for num in nums2:
        if num in set1:
            result_set.add(num)
            
    return list(result_set)
