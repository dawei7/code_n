from math import gcd


def solve(nums):
    current = 0
    for value in nums:
        current = gcd(current, value)
        if current == 1:
            return True
    return False
