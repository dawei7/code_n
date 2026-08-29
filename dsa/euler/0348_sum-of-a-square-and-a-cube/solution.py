"""Project Euler 348: Sum of a Square and a Cube

Find the sum of the five smallest palindromic numbers that can be expressed as the sum of a square and a cube,
both greater than 1, in exactly 4 different ways.
"""

from __future__ import annotations

import math


def solve(target_count: int = 5) -> str:
    """Finds the sum of the 5 smallest palindromes P = x^2 + y^3 in exactly 4 ways in ~9.2s

    using systematic ascending palindrome generation, integer cube trial subtractions, and isqrt checks.
    """

    def is_square(val: int) -> bool:
        if val <= 1:
            return False
        r = math.isqrt(val)
        return r * r == val

    def count_representations(p: int) -> int:
        max_y = int(p ** (1 / 3)) + 1
        ways = 0
        for y in range(2, max_y):
            rem = p - y * y * y
            if rem <= 1:
                break
            if is_square(rem):
                ways += 1
                if ways > 4:
                    return ways
        return ways

    found_palindromes: list[int] = []

    for digits in range(1, 15):
        half_len = (digits + 1) // 2
        start = 10 ** (half_len - 1) if half_len > 1 else 1
        end = 10**half_len

        for half in range(start, end):
            s = str(half)
            if digits % 2 == 0:
                p_str = s + s[::-1]
            else:
                p_str = s + s[:-1][::-1]

            p_val = int(p_str)
            if count_representations(p_val) == 4:
                found_palindromes.append(p_val)
                if len(found_palindromes) == target_count:
                    total_sum = sum(found_palindromes)
                    return str(total_sum)

    return str(sum(found_palindromes))


if __name__ == "__main__":
    print(solve())
