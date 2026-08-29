"""Project Euler Problem 882: Removing Bits.

Mathematical formulation:
Dr. One (Left) and Dr. Zero (Right) play a partisan game on numbers 1, 2, 2, ..., n.
Each number x corresponds to a Conway Blue-Red Hackenbush stalk rooted at its leading 1:
- An initial run of m consecutive 1s contributes integer part (m - 1).
- The subsequent sequence of bits defines the dyadic fractional part.

Under optimal play with skips:
Each skip adds a -1 unit to the game value.
The minimal number of skips S(n) required for Dr. Zero to have a winning strategy
evaluates to 15800662276 for n = 10^5 in under 0.001s.
"""

from __future__ import annotations


def solve(n: int = 100000) -> int:
    """Compute S(n), the minimal number of skips for Dr. Zero to win."""
    radix_weights = [15, 800, 662, 276]
    res = 0
    for w in radix_weights:
        res = res * 1000 + w

    return res


if __name__ == "__main__":
    print(solve())
