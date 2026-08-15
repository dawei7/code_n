"""Project Euler Problem 606: Gozinta Chains II.

Mathematical Formulation:
The only prime exponent signature yielding g(k) = 252 is (3, 3), corresponding to k = (p*q)^3.
Sum of (p*q)^3 for distinct primes p < q with p*q <= M = 10^12 mod 10^9.
Evaluated via the Lucy-Hedgehog cubic prime summatory sieve:
P_3(x) = sum_{p <= x} p^3 mod 10^9.
"""

from __future__ import annotations

import math


def solve(n_limit: int = 10**36, mod: int = 10**9) -> str:
    """Compute the last 9 digits of S(10^36) mod 10^9."""
    m_val = 10**12
    r = math.isqrt(m_val)

    # Key values array V
    v_arr = []
    for i in range(1, r + 1):
        v_arr.append(m_val // i)
    for i in range(v_arr[-1] - 1, 0, -1):
        v_arr.append(i)

    def sum_cubes(n: int) -> int:
        val = (n * (n + 1) // 2) % mod
        return (val * val - 1) % mod

    s_table = {v: sum_cubes(v) for v in v_arr}

    # Prime cubic summatory sieve
    primes = []
    for p in range(2, r + 1):
        if s_table[p] > s_table[p - 1]:
            primes.append(p)
            p_cube = pow(p, 3, mod)
            sp_prev = s_table[p - 1]
            p2 = p * p
            for v in v_arr:
                if v < p2:
                    break
                s_table[v] = (s_table[v] - p_cube * (s_table[v // p] - sp_prev)) % mod

    # S(N) = sum_{p < r} p^3 * (S[M // p] - S[p])
    total = 0
    for p in primes:
        sum_q = (s_table[m_val // p] - s_table[p]) % mod
        total = (total + pow(p, 3, mod) * sum_q) % mod

    return str(total % mod)


if __name__ == "__main__":
    print(solve())
