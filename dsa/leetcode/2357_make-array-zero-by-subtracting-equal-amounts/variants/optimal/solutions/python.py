from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the minimum number of operations to make all elements in the array zero.
    Each operation subtracts the minimum positive element from all positive elements.
    This is equivalent to finding the number of unique positive integers in the array.
    """
    return len({x for x in nums if x > 0})
