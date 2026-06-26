"""Optimal solution for LeetCode 1390: Four Divisors."""

from math import isqrt


def solve(nums: list[int]) -> int:
    total = 0
    for value in nums:
        divisor_count = 0
        divisor_sum = 0
        for d in range(1, isqrt(value) + 1):
            if value % d != 0:
                continue
            other = value // d
            if other == d:
                divisor_count += 1
                divisor_sum += d
            else:
                divisor_count += 2
                divisor_sum += d + other
            if divisor_count > 4:
                break
        if divisor_count == 4:
            total += divisor_sum
    return total
