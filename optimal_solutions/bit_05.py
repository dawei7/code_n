"""Optimal solution for bit_05: Single Number III.

Every element in the input array appears exactly
"""


def solve(arr):
    """Return the two elements that appear exactly once (sorted)."""
    xor_all = 0
    for v in arr:
        xor_all ^= v
    diff_bit = xor_all & -xor_all
    a, b = 0, 0
    for v in arr:
        if v & diff_bit:
            a ^= v
        else:
            b ^= v
    return sorted([a, b])
