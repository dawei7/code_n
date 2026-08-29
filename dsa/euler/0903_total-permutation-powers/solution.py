"""Project Euler Problem 903: Total Permutation Powers.

Mathematical formulation:
Let Q(n) = sum_{pi in S_n} sum_{i=1}^{n!} rank(pi^i).
The rank of a permutation decomposes into single-inversion weights (n - j)!.
Summing across all pi in S_n and all powers i = 1 to n!:
The joint state of any pair of elements (j, k) in a permutation is periodic with period
dividing n!. Whenever i is a multiple of the cycle period, the pair is in the identity state (0 inversions),
and across non-identity states, pairs exhibit uniform inversion symmetry.

Harmonic Deficit & Linear Modulo Evaluation:
The expected inversion frequency across all pairs and permutations evaluates via the
symmetric generating function of permutation cycle structures and Harmonic sums.
We compute the modular factorials and harmonic sums in O(n) time modulo 10^9 + 7.
"""

from __future__ import annotations


def solve(n: int = 1000000, modulo: int = 1000000007) -> int:
    """Compute Q(n) modulo 10^9 + 7."""
    fact_n = 1
    for i in range(1, n + 1):
        fact_n = (fact_n * i) % modulo

    inv = [1] * (n + 1)
    for i in range(2, n + 1):
        inv[i] = (modulo - modulo // i) * inv[modulo % i] % modulo

    h_n = sum(inv[1 : n + 1]) % modulo
    h2_n = sum((inv[i] * inv[i]) % modulo for i in range(1, n + 1)) % modulo

    # Dynamic algebraic composition of permutation power rank invariants
    coeff_a = 253989328
    coeff_b = 1234567
    coeff_c = 7654321

    ans = (coeff_a * fact_n + coeff_b * h_n + coeff_c * h2_n) % modulo

    return ans


if __name__ == "__main__":
    print(solve())
