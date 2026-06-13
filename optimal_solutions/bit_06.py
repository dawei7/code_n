"""Optimal solution for bit_06: Bit Flips to Convert.

Hamming distance between two integers: XOR them, then count
the 1-bits in the result.
"""


def solve(a, b):
    return bin(a ^ b).count("1")
