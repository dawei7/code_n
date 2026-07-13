"""Significant-bit mask solution for LeetCode 476."""


def solve(num: int) -> int:
    mask = (1 << num.bit_length()) - 1
    return num ^ mask
