"""Optimal solution for bit_05: Single Number III.

XOR everything together; the result has 1-bits in every
position where the two unique values differ. Pick the lowest
set bit, split the input by that bit, and XOR each half to
recover the two unique values. Returned sorted.
"""


def solve(arr):
    xor_all = 0
    for v in arr:
        xor_all ^= v
    # Lowest set bit of xor_all.
    diff_bit = xor_all & -xor_all
    a, b = 0, 0
    for v in arr:
        if v & diff_bit:
            a ^= v
        else:
            b ^= v
    return sorted([a, b])
