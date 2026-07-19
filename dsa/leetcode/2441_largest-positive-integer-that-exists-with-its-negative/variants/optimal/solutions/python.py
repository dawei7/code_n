from typing import List

def solve(nums: List[int]) -> int:
    """
    Finds the largest positive integer k such that -k exists in the list.
    Uses a set for O(1) lookups.
    """
    num_set = set(nums)
    max_k = -1
    
    for x in nums:
        if x > 0 and -x in num_set:
            if x > max_k:
                max_k = x
                
    return max_k
