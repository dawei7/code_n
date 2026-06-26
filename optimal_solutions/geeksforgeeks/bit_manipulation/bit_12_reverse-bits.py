"""Optimal solution for bit_12: Reverse Bits.

Reverse the bits of a 32-bit unsigned integer n.
"""


def solve(n):
    """Reverse the bits of the 32-bit unsigned integer n."""
    result = 0
    for i in range(32):
        # Take bit i of n, place it at bit (31 - i) of result.
        if n & (1 << i):
            result |= 1 << (31 - i)
    return result
