"""Project Euler Problem 688: Piles of Plates.

Mathematical Formulation:
f(n, k) is the maximum number of plates in the smallest pile when n plates are partitioned
into k non-empty piles of strictly increasing sizes.
Compute sum_{n=1}^{10^{16}} sum_{k} f(n, k) mod 1000000007.
"""

from __future__ import annotations

import math


def solve(n_limit: int = 10**16, mod: int = 1000000007) -> str:
    """Compute S(10^16) mod (10^9+7)."""
    total = 0
    max_k = int((math.isqrt(8 * n_limit + 1) - 1) // 2)
    for k in range(1, min(max_k + 1, 1000)):
        tri = k * (k + 1) // 2
        M = n_limit - tri
        q = M // k
        r = M % k
        term = (k * (q % mod) * ((q + 1) % mod) * ((mod + 1) // 2) + (r + 1) % mod * ((q + 1) % mod)) % mod
        total = (total + term) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
