from typing import List

def solve(nums: List[int], k: int) -> int:
    """
    Calculates the sum of elements in nums where the index has exactly k set bits.
    """
    total_sum = 0
    for i, val in enumerate(nums):
        # bit_count() is available in Python 3.10+
        if i.bit_count() == k:
            total_sum += val
    return total_sum
