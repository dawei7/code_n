"""Optimal app-local solution for LeetCode 906."""

from bisect import bisect_left, bisect_right
from math import isqrt


def _generate_super_palindromes():
    upper = 10**18 - 1
    root_limit = isqrt(upper)
    values = []
    for odd_length in (True, False):
        seed = 1
        while True:
            digits = str(seed)
            mirrored = digits[-2::-1] if odd_length else digits[::-1]
            root = int(digits + mirrored)
            if root > root_limit:
                break

            square = root * root
            square_digits = str(square)
            if square_digits == square_digits[::-1]:
                values.append(square)
            seed += 1

    return tuple(sorted(values))


_SUPER_PALINDROMES = _generate_super_palindromes()


def solve(left, right):
    lower = int(left)
    upper = int(right)
    return bisect_right(_SUPER_PALINDROMES, upper) - bisect_left(_SUPER_PALINDROMES, lower)
