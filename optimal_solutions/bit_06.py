"""Optimal solution for bit_06: Bit Flips to Convert.

Given two non-negative integers a and b, return
"""


def solve(a, b):
    """Return the number of bit flips to convert a to b (Hamming distance)."""
    return bin(a ^ b).count("1")
