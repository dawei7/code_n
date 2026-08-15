"""Project Euler Problem 804: Counting Binary Quadratic Representations.

Find T(10^16), the total number of integer pairs (x, y) != (0, 0) such that x^2 + xy + 41y^2 <= 10^16.
"""

import math


def solve(N: int = 10**16) -> int:
    """Compute T(N) via completing the square: (2x + y)^2 + 163y^2 <= 4N with parity constraint."""
    ans = 2 * math.isqrt(N)
    max_y = math.isqrt(4 * N // 163)

    for y in range(1, max_y + 1):
        rem = 4 * N - 163 * y * y
        if rem < 0:
            break
        M = math.isqrt(rem)
        if (M & 1) == (y & 1):
            count = M + 1
        else:
            count = M
        ans += 2 * count

    return ans


if __name__ == "__main__":
    print(solve())
