"""Optimal solution for bit_09: Multiply Without *.

Bit-by-bit multiplication: for each set bit of b, add (a << k)
to the result. O(log b) additions.
"""


def solve(a, b):
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
