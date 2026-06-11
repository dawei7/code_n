"""Optimal solution for bit_02: Power of Two Check.

Powers of two have exactly one bit set, so n & (n-1) clears it.
"""


def solve(n):
    return n > 0 and (n & (n - 1)) == 0
