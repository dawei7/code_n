"""Optimal solution for bit_09: Multiply Without *.

Compute a * b using only addition and shifts. For
"""


def solve(a, b):
    """Return a * b without using *."""
    negative = (a < 0) != (b < 0)
    x = abs(a)
    y = abs(b)
    result = 0
    while y > 0:
        if y & 1:
            result += x
        x <<= 1
        y >>= 1
    if negative:
        result = -result
    return result
