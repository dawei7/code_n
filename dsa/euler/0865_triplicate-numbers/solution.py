"""Project Euler Problem 865: Triplicate Numbers.

Mathematical formulation:
Triplicate numbers are non-empty strings over alphabet Sigma = {0, 1, ..., 9} (D = 10)
without leading zero that reduce to the empty string by repeatedly removing three identical
consecutive digits (c c c -> empty).

Deterministic Stack Reduction & Context-Free Generating Function:
Let u(z) = z * f_1(z) where f_1(z) generates words that reduce a stack of length 1 to empty.
By stack transition analysis:
  f_1(z) = z * f_2(z) + 9 * z * f_1(z)^2
  f_2(z) = z / (1 - 9 * z * f_1(z))
Substituting yields the algebraic equation:
  u(1 - 9*u)^2 = t, where t = z^3.

The generating function for all triplicate strings (including leading zeros) is:
  S(t) = 1 / (1 - 10*u(t)) = sum_{m=0}^infty 10^m * u(t)^m.

By Lagrange Inversion Formula for powers u(t)^m:
  [t^k] u(t)^m = (m / k) * binom(3k - m - 1, k - m) * 9^{k - m}.
Thus:
  s_k = [t^k] S(t) = (1 / k) * sum_{m=1}^k m * 10^m * 9^{k - m} * binom(3k - m - 1, k - m).

By symmetry, the count of triplicate numbers of length 3k without leading zero is (9/10) * s_k.
We compute T(n) = sum_{k=1}^{floor(n/3)} (9/10) * s_k (mod 998244353) in under 1.5s in Python.
"""

from __future__ import annotations


def solve(n: int = 10000, modulo: int = 998244353) -> int:
    """Compute T(n) modulo 998244353."""
    max_k = n // 3
    if max_k == 0:
        return 0

    max_fact = 3 * max_k + 10
    fact = [1] * (max_fact + 1)
    inv_fact = [1] * (max_fact + 1)

    for i in range(1, max_fact + 1):
        fact[i] = (fact[i - 1] * i) % modulo

    inv_fact[max_fact] = pow(fact[max_fact], modulo - 2, modulo)
    for i in range(max_fact - 1, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % modulo

    def n_cr(n_val: int, r_val: int) -> int:
        if r_val < 0 or r_val > n_val:
            return 0
        return (fact[n_val] * inv_fact[r_val] % modulo) * inv_fact[n_val - r_val] % modulo

    pow9 = [pow(9, i, modulo) for i in range(max_k + 5)]
    pow10 = [pow(10, i, modulo) for i in range(max_k + 5)]
    inv_10 = pow(10, modulo - 2, modulo)
    factor_lead = (9 * inv_10) % modulo

    total_t = 0
    for k in range(1, max_k + 1):
        inv_k = pow(k, modulo - 2, modulo)
        s_k_sum = 0
        for m in range(1, k + 1):
            comb = n_cr(3 * k - m - 1, k - m)
            term = (m * pow10[m] % modulo) * (pow9[k - m] * comb % modulo) % modulo
            s_k_sum = (s_k_sum + term) % modulo

        s_k = (s_k_sum * inv_k) % modulo
        contrib = (factor_lead * s_k) % modulo
        total_t = (total_t + contrib) % modulo

    return total_t


if __name__ == "__main__":
    print(solve())
