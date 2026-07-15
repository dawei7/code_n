"""Reference solution for LeetCode 1362."""

from math import isqrt


def _closest_pair(value):
    divisor = isqrt(value)
    while value % divisor:
        divisor -= 1
    return [divisor, value // divisor]


def solve(num):
    first = _closest_pair(num + 1)
    second = _closest_pair(num + 2)
    if second[1] - second[0] < first[1] - first[0]:
        return second
    return first
