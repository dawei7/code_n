from math import gcd
from typing import List


def solve(nums: List[int]) -> bool:
    current = 0
    for value in nums:
        current = gcd(current, value)
        if current == 1:
            return True
    return False
