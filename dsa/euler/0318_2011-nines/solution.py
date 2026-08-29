"""Project Euler 318: 2011 Nines

Find sum N(p, q) for all pairs of positive integers (p, q) with p < q and p + q <= 2011
such that the fractional part of (sqrt(p) + sqrt(q))^{2n} approaches 1,
where N(p, q) is the minimal n such that the number of consecutive nines is >= 2011.
"""

from __future__ import annotations

import math


def solve(limit: int = 2011, k_nines: int = 2011) -> str:
    """Calculates sum N(p, q) for p < q and p + q <= limit using algebraic conjugate expansion:

    (sqrt(q) + sqrt(p))^{2n} + (sqrt(q) - sqrt(p))^{2n} is an integer, so the fractional part
    is 1 - (sqrt(q) - sqrt(p))^{2n}, requiring n >= ceil(-k_nines / log10((sqrt(q) - sqrt(p))^2)).
    """
    total_n = 0

    for p in range(1, limit):
        # Condition for fractional part to approach 1: sqrt(q) - sqrt(p) < 1 <=> q < (sqrt(p) + 1)^2
        max_q = min(limit - p, int((math.sqrt(p) + 1.0) ** 2))
        sqrt_p = math.sqrt(p)

        for q in range(p + 1, max_q + 1):
            diff = math.sqrt(q) - sqrt_p
            if diff < 1.0:
                v = diff * diff
                # Minimal n such that v^n <= 10^(-k_nines)
                n = math.ceil(-k_nines / math.log10(v))
                total_n += n

    return str(total_n)


if __name__ == "__main__":
    print(solve())
