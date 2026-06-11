"""Optimal solution for bit_01: Count Set Bits.

Walk the bits of n and count the 1s.
"""


def solve(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
