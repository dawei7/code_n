"""Optimal solution for bit_07: Swap Odd and Even Bits.

Mask out the even bits, shift them right by 1, then mask out
the odd bits and shift them left by 1. OR the two halves.
"""


def solve(n):
    even_mask = 0x55555555  # 0101 0101 ...
    odd_mask = 0xAAAAAAAA   # 1010 1010 ...
    even_bits = (n & even_mask) >> 1
    odd_bits = (n & odd_mask) << 1
    return even_bits | odd_bits
