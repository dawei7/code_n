from typing import List

def solve(nums: List[int]) -> int:
    """
    Calculates the minimum operations to make all elements divisible by 3.
    For any number x:
    - If x % 3 == 0, cost is 0.
    - If x % 3 == 1, we can subtract 1 to reach a multiple of 3 (cost 1).
    - If x % 3 == 2, we can add 1 to reach a multiple of 3 (cost 1).
    """
    operations = 0
    for num in nums:
        if num % 3 != 0:
            operations += 1
    return operations
