from typing import List
from functools import reduce
from operator import xor

def solve(nums: List[int]) -> int:
    """
    Calculates the Xor-beauty of the array.
    The expression ((nums[i] | nums[j]) & nums[k]) XORed over all i, j, k
    simplifies to the XOR sum of all elements in the array.
    """
    return reduce(xor, nums)
