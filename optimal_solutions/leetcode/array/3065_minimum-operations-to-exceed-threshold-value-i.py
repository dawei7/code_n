from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the number of elements in nums that are strictly less than k.
    Removing these elements is the minimum operation to satisfy the threshold.
    """
    count = 0
    for num in nums:
        if num < k:
            count += 1
    return count
