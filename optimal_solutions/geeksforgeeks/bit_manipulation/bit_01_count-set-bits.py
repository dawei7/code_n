"""Optimal solution for bit_01: Count Set Bits.

Count the number of 1-bits in the binary
"""


def solve(n):
    """Count the 1-bits in n (Hamming weight)."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
