"""Project Euler 302: Strong Achilles Numbers

Find the number of Strong Achilles numbers below 10^18.
An integer S is an Achilles number if S is powerful (p^2 | S for all p | S) but not a perfect power (gcd(exponents) == 1).
S is a Strong Achilles number if both S and phi(S) are Achilles numbers.
"""

from __future__ import annotations

import math


def solve(limit_s: int = 10**18) -> str:
    """Calculates the number of Strong Achilles numbers below limit_s using Top-Down Prime Factor Branching

    with Unreparable Odd Prime Pruning.
    """
    max_p = int(limit_s ** (1 / 3)) + 10  # 10^6

    # Sieve primes up to max_p
    sieve = [True] * (max_p + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(max_p)) + 1):
        if sieve[i]:
            sieve[i * i : max_p + 1 : i] = [False] * len(sieve[i * i : max_p + 1 : i])
    primes = [i for i, is_p in enumerate(sieve) if is_p]

    # Smallest prime factor (SPF) sieve for fast prime factorization of p - 1
    spf = list(range(max_p + 1))
    for i in range(2, int(math.isqrt(max_p)) + 1):
        if spf[i] == i:
            for j in range(i * i, max_p + 1, i):
                if spf[j] == j:
                    spf[j] = i

    factors_p_minus_1: list[list[tuple[int, int]]] = [[] for _ in range(len(primes))]
    for idx, p in enumerate(primes):
        m = p - 1
        f: list[tuple[int, int]] = []
        while m > 1:
            prime_factor = spf[m]
            cnt = 0
            while m % prime_factor == 0:
                cnt += 1
                m //= prime_factor
            f.append((prime_factor, cnt))
        factors_p_minus_1[idx] = f

    count = 0

    def dfs(
        p_idx: int,
        current_s: int,
        phi_factors: dict[int, int],
        s_exponents: list[int],
    ) -> None:
        nonlocal count

        if len(s_exponents) >= 2:
            if math.gcd(*s_exponents) == 1:
                phi_exps = list(phi_factors.values())
                if all(e >= 2 for e in phi_exps) and math.gcd(*phi_exps) == 1:
                    count += 1

        # Prune if any prime q > current_max_p has exponent 1 in phi(S)
        current_max_p = primes[p_idx] if p_idx >= 0 else 0
        for q, exp in phi_factors.items():
            if q > current_max_p and exp == 1:
                return

        for idx in range(p_idx, -1, -1):
            p = primes[idx]
            if current_s * p * p >= limit_s:
                continue

            p_pow = p * p
            e = 2
            f_p = factors_p_minus_1[idx]
            while current_s * p_pow < limit_s:
                new_phi = dict(phi_factors)
                new_phi[p] = new_phi.get(p, 0) + (e - 1)
                for q, cnt in f_p:
                    new_phi[q] = new_phi.get(q, 0) + cnt

                dfs(idx - 1, current_s * p_pow, new_phi, s_exponents + [e])
                e += 1
                p_pow *= p

    for idx in range(len(primes) - 1, -1, -1):
        p = primes[idx]
        if p**3 >= limit_s:
            continue
        e = 3
        p_pow = p**3
        f_p = factors_p_minus_1[idx]
        while p_pow < limit_s:
            phi_f = {p: e - 1}
            for q, cnt in f_p:
                phi_f[q] = phi_f.get(q, 0) + cnt
            dfs(idx - 1, p_pow, phi_f, [e])
            e += 1
            p_pow *= p

    return str(count)


if __name__ == "__main__":
    print(solve())
