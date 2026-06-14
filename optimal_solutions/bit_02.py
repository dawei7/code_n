"""Optimal solution for bit_02: Power of Two Check.

Return True iff the input n is a power of two.
"""


def solve(n):
    """True iff n is a power of two (n >= 1)."""
    return n > 0 and (n & (n - 1)) == 0
