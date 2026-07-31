from math import isqrt


def solve(k: int) -> int:
    value = isqrt(k)
    copies = (k + value - 1) // value
    return value + copies - 2
