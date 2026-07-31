from math import gcd


def solve(nums: list[int]) -> int:
    groups = 1
    common = 0

    for value in nums:
        extended = gcd(common, value)
        if extended == 1:
            groups += 1
            common = value
        else:
            common = extended

    return groups
