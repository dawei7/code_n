from typing import List

def solve(nums: List[int], n: int) -> int:
    """
    Calculates the minimum number of patches required to cover the range [1, n].
    """
    patches = 0
    miss = 1
    i = 0
    m = len(nums)
    
    while miss <= n:
        if i < m and nums[i] <= miss:
            # We can extend the range [1, miss - 1] to [1, miss + nums[i] - 1]
            miss += nums[i]
            i += 1
        else:
            # We must add 'miss' to the array to cover the current gap
            # This extends the range [1, miss - 1] to [1, 2 * miss - 1]
            miss += miss
            patches += 1
            
    return patches
