from typing import List

def solve(nums: List[int]) -> List[int]:
    """
    For each index i, the maximum possible bitwise OR of a subarray starting at i
    is determined by the bits available from i to the end of the array.
    To minimize the length, we need the smallest index j >= i such that the 
    bitwise OR of nums[i...j] includes all bits that are set in the 
    bitwise OR of nums[i...n-1].
    """
    n = len(nums)
    # last_seen[b] stores the index of the most recent occurrence of bit b
    last_seen = [-1] * 30
    res = [0] * n
    
    # Iterate backwards to keep track of the nearest index for each bit
    for i in range(n - 1, -1, -1):
        for b in range(30):
            if (nums[i] >> b) & 1:
                last_seen[b] = i
        
        # The shortest subarray starting at i must extend to the furthest
        # index required to capture all bits that can be set.
        # If no bits are set (nums[i] is 0), the shortest subarray is length 1.
        furthest_idx = i
        for b in range(30):
            if last_seen[b] != -1:
                furthest_idx = max(furthest_idx, last_seen[b])
        
        res[i] = furthest_idx - i + 1
        
    return res
