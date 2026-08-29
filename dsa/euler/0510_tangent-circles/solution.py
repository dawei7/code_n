"""Project Euler Problem 510: Tangent Circles.

Find S(10^9), where S(n) is the sum of (r_A + r_B + r_C) for all mutually tangent
circles A, B, C resting on a common tangent line with integer radii 0 < r_A <= r_B <= n.
"""

import math


def solve(n: int = 10**9) -> int:
    """Compute S(n) using Descartes tangent circle parameterization and coprimality iteration."""
    total = 0
    sqrt_n = math.isqrt(n)

    for v in range(1, sqrt_n + 1):
        if v * (v + 1) > sqrt_n:
            break
        for u in range(1, v + 1):
            if math.gcd(u, v) != 1:
                continue
            m = (v * (u + v)) ** 2
            if m > n:
                continue
            k = n // m
            base_sum = (u**2 + v**2) * (u + v) ** 2 + (u * v) ** 2
            total += base_sum * (k * (k + 1) // 2)

    return total


if __name__ == "__main__":
    print(solve())
