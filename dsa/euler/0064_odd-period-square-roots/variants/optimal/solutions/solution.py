import math


def period_length(n: int) -> int:
    """Find period length of the continued fraction expansion of sqrt(n)."""
    a0 = math.isqrt(n)
    if a0 * a0 == n:
        return 0

    m = 0
    d = 1
    a = a0
    length = 0

    while a != 2 * a0:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        length += 1

    return length


def solve(limit: int = 10000) -> int:
    """How many continued fractions for N <= limit have an odd period length?
    
    Time Complexity: O(limit * P)
    Space Complexity: O(1)
    """
    return sum(1 for n in range(1, limit + 1) if period_length(n) % 2 == 1)
