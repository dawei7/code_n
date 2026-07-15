"""Optimal app-local solution for LeetCode 1318."""


def solve(a, b, c):
    flips = 0
    while a or b or c:
        a_bit = a & 1
        b_bit = b & 1
        c_bit = c & 1
        if c_bit:
            if not (a_bit or b_bit):
                flips += 1
        else:
            flips += a_bit + b_bit
        a >>= 1
        b >>= 1
        c >>= 1
    return flips
