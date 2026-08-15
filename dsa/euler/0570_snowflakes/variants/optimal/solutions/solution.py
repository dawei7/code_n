"""Project Euler Problem 570: Snowflakes.

Find sum_{n=3..10^7} G(n), where G(n) = gcd(A(n), B(n)), and A(n), B(n) are
the counts of 1-layer-thick and 3-layer-thick triangles in an order n snowflake.
"""

import math


def solve(limit_n: int = 10_000_000) -> int:
    """Compute sum_{n=3..limit_n} G(n) using algebraic polynomial GCD reduction."""
    if limit_n < 3:
        return 0

    gcd = math.gcd
    total_d = 0

    # Branch 1: n = 4, 7, 10, ... (n = 1 mod 3)
    for n in range(4, limit_n + 1, 3):
        m = 7 * n + 3
        inv3 = (2 * m + 1) // 3
        b = (4 * inv3) % m
        t = pow(b, n - 2, m)
        total_d += gcd((2 * t - 1) % m, m)

    # Branch 2: n = 5, 8, 11, ... (n = 2 mod 3)
    for n in range(5, limit_n + 1, 3):
        m = 7 * n + 3
        inv3 = (m + 1) // 3
        b = (4 * inv3) % m
        t = pow(b, n - 2, m)
        total_d += gcd((2 * t - 1) % m, m)

    # Branch 3: n = 3, 6, 9, ... (n = 0 mod 3)
    for n in range(3, limit_n + 1, 3):
        m = 7 * n + 3
        x = (2 * pow(4, n - 2, m) - pow(3, n - 2, m)) % m
        total_d += gcd(x, m)

    return 6 * total_d


if __name__ == "__main__":
    print(solve())
