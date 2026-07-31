from math import gcd, lcm


def solve(nums: list[int]) -> int:
    length = len(nums)
    prefix_gcd = [0] * (length + 1)
    prefix_lcm = [1] * (length + 1)

    for index, value in enumerate(nums):
        prefix_gcd[index + 1] = gcd(prefix_gcd[index], value)
        prefix_lcm[index + 1] = lcm(prefix_lcm[index], value)

    suffix_gcd = [0] * (length + 1)
    suffix_lcm = [1] * (length + 1)

    for index in range(length - 1, -1, -1):
        suffix_gcd[index] = gcd(nums[index], suffix_gcd[index + 1])
        suffix_lcm[index] = lcm(nums[index], suffix_lcm[index + 1])

    best = prefix_gcd[length] * prefix_lcm[length]
    for removed in range(length):
        remaining_gcd = gcd(prefix_gcd[removed], suffix_gcd[removed + 1])
        remaining_lcm = lcm(prefix_lcm[removed], suffix_lcm[removed + 1])
        best = max(best, remaining_gcd * remaining_lcm)

    return best
