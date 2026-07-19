"""Optimal solution for LeetCode 371: Sum of Two Integers."""


def solve(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    maximum_positive = 0x7FFFFFFF
    left = a & mask
    right = b & mask

    while right:
        left, right = (left ^ right) & mask, ((left & right) << 1) & mask

    return left if left <= maximum_positive else ~(left ^ mask)

