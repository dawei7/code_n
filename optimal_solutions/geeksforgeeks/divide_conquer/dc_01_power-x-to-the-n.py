"""Optimal solution for dc_01: Power(x, n).

Recursive halving: x^n = (x^(n//2))^2, with an extra x when
n is odd. Handle negative n by computing the reciprocal. O(log n).
"""


def solve(x, n):
    if n == 0:
        return 1
    # Use absolute exponent, then take reciprocal at the end if needed.
    abs_n = -n if n < 0 else n
    result = 1.0
    base = float(x)
    while abs_n > 0:
        if abs_n & 1:
            result *= base
        abs_n >>= 1
        if abs_n:
            base *= base
    if n < 0:
        return 1.0 / result
    return result
