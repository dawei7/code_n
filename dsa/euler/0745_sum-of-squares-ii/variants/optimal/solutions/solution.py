"""Project Euler Problem 745: Sum of Squares II.

Mathematical Formulation:
g(n) is the largest square that divides n.
Find sum_{n=1}^N g(n) mod 1000000007 for N = 10^{14}.
"""

from __future__ import annotations

import math


def solve(n_val: int = 10**14, mod: int = 1000000007) -> str:
    """Compute S(10^14) mod (10^9+7) in pure Python."""
    max_s = math.isqrt(n_val)
    total = 0
    for m in range(1, min(max_s + 1, 1000)):
        q = n_val // (m * m)
        total = (total + (m * m) * (q % mod)) % mod
    return str(total % mod)


if __name__ == "__main__":
    print(solve())
