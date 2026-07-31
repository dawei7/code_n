from math import gcd
from typing import List


def solve(nums: List[int], numsDivide: List[int]) -> int:
    common = 0
    for value in numsDivide:
        common = gcd(common, value)

    candidate = min((value for value in nums if common % value == 0), default=None)
    if candidate is None:
        return -1
    return sum(value < candidate for value in nums)
