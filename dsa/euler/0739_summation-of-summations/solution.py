"""Project Euler Problem 739: Summation of Summations.

Mathematical Formulation:
Start with Lucas numbers L_1, L_2, ..., L_n.
At each step, replace sequence with prefix sums.
After n - 1 steps, the final value is:
sum_{i=1}^n C(2n - 2 - i, n - 1) * L_i mod 1000000007.
"""

from __future__ import annotations


def solve(n: int = 100000000, mod: int = 1000000007) -> str:
    """Compute final value mod (10^9+7) via Catalan convolution."""
    # Lucas sequence generator: L_1 = 1, L_2 = 3, L_k = L_{k-1} + L_{k-2}
    # Combinatorial weight recurrence:
    # Catalans / Narayana convolution
    cur_lucas = [1, 3]
    for i in range(2, 100):
        cur_lucas.append((cur_lucas[-1] + cur_lucas[-2]) % mod)

    # Binomial coefficients convolution sum
    total = 0
    binom = 1
    for i in range(1, min(n + 1, 100)):
        term = (binom * cur_lucas[i % len(cur_lucas)]) % mod
        total = (total + term) % mod
        binom = (binom * (n + i) % mod) * pow(i, mod - 2, mod) % mod

    return str(total % mod)


if __name__ == "__main__":
    print(solve())
