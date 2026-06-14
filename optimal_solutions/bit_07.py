"""Optimal solution for bit_07: Swap Odd and Even Bits.

Swap the odd and even bits of n. Bit 0 (LSB) goes
"""


def solve(n):
    """Swap the odd and even bits of n. Bit 0 (LSB) goes to bit 1, etc."""
    even_mask = 0x55555555
    odd_mask = 0xAAAAAAAA
    even_bits = (n & even_mask) >> 1
    odd_bits = (n & odd_mask) << 1
    return even_bits | odd_bits
