from math import isqrt


def solve(n):
    total = n * (n + 1) // 2
    pivot = isqrt(total)
    return pivot if pivot * pivot == total else -1
