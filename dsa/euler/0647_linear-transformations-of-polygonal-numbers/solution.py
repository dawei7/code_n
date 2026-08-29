"""Project Euler Problem 647: Linear Transformations of Polygonal Numbers.

Find sum_k F_k(10^12) for odd k >= 3, where F_k(N) is the sum of (A + B) over all pairs (A, B)
with max(A, B) <= N such that A * P_k(n) + B is always a k-gonal number for all n >= 1.
"""

import math


def solve(n: int = 10**12) -> int:
    """Compute sum_{k odd} F_k(N) using the quadratic polynomial parameterization A = (2mc + 1)^2."""
    total = 0
    sqrt_n = int(math.isqrt(n))
    max_mc = (sqrt_n - 1) // 2

    for m in range(1, max_mc + 1):
        max_c = max_mc // m
        for c in range(1, max_c + 1, 2):
            a_val = (2 * m * c + 1) ** 2
            c_minus_2 = c - 2
            b_val = (m * (m * c + 1) * c_minus_2 * c_minus_2) // 2
            if b_val <= n:
                total += a_val + b_val

    return total


if __name__ == "__main__":
    print(solve())
