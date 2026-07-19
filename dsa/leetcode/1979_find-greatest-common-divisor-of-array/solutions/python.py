from math import gcd


def solve(nums: list[int]) -> int:
    return gcd(min(nums), max(nums))
