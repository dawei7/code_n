"""Project Euler Problem 432: Totient Sum.

Find S(510510, 10^11) mod 10^9, where S(n, m) = sum_{i=1..m} phi(n*i).
Return the last 9 digits as a string.
"""

from array import array
from math import isqrt
from typing import Dict, List, Tuple

MOD = 1_000_000_000
SIEVE_LIMIT = 5_000_000


def _build_totients(limit: int) -> Tuple[array, array, List[int]]:
    phi = array("I", [0]) * (limit + 1)
    phi[1] = 1
    primes: List[int] = []

    for i in range(2, limit + 1):
        if phi[i] == 0:
            phi[i] = i - 1
            primes.append(i)
        for p in primes:
            ip = i * p
            if ip > limit:
                break
            if i % p == 0:
                phi[ip] = phi[i] * p
                break
            phi[ip] = phi[i] * (p - 1)

    prefix_mod = array("I", [0]) * (limit + 1)
    acc = 0
    for i in range(1, limit + 1):
        acc += phi[i]
        acc %= MOD
        prefix_mod[i] = acc

    return phi, prefix_mod, primes


def _subset_products_with_sign(
    prime_factors: List[int],
) -> List[Tuple[int, int]]:
    k = len(prime_factors)
    out: List[Tuple[int, int]] = []
    for mask in range(1, 1 << k):
        prod = 1
        bits = 0
        mm = mask
        idx = 0
        while mm:
            if mm & 1:
                prod *= prime_factors[idx]
                bits += 1
            idx += 1
            mm >>= 1
        sign = 1 if (bits & 1) else -1
        out.append((prod, sign))
    out.sort(key=lambda t: t[0])
    return out


def solve(n_val: int = 510510, m_val: int = 10**11) -> str:
    """Compute S(n_val, m_val) mod MOD using Du Sieve and inclusion-exclusion over prime factors."""
    phi, phi_small_mod, _ = _build_totients(SIEVE_LIMIT)

    # Prime factors of 510510 = 2 * 3 * 5 * 7 * 11 * 13 * 17
    temp = n_val
    pf: List[int] = []
    for d in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if temp % d == 0:
            pf.append(d)
            while temp % d == 0:
                temp //= d
    if temp > 1:
        pf.append(temp)

    subset_list = _subset_products_with_sign(pf)
    phi_n_mod = int(phi[n_val]) % MOD

    phi_cache: Dict[int, int] = {}

    def phi_mod_sum(x: int) -> int:
        if x <= SIEVE_LIMIT:
            return phi_small_mod[x]
        got = phi_cache.get(x)
        if got is not None:
            return got

        ans = (x * (x + 1) // 2) % MOD
        r = isqrt(x)
        upper = x // r

        for t in range(1, upper):
            ans -= phi_small_mod[t] * (x // t - x // (t + 1))
            ans %= MOD

        for k in range(2, r + 1):
            ans -= phi_mod_sum(x // k)
            ans %= MOD

        ans %= MOD
        phi_cache[x] = ans
        return ans

    s_cache: Dict[int, int] = {}

    def s_mod_rec(mm: int) -> int:
        if mm <= 0:
            return 0
        if mm == 1:
            return phi_n_mod
        got = s_cache.get(mm)
        if got is not None:
            return got

        ans = (phi_n_mod * phi_mod_sum(mm)) % MOD

        for prod, sign in subset_list:
            if prod > mm:
                break
            q = mm // prod
            if q == 0:
                break
            if sign == 1:
                ans += s_mod_rec(q)
            else:
                ans -= s_mod_rec(q)
            ans %= MOD

        ans %= MOD
        s_cache[mm] = ans
        return ans

    last9 = s_mod_rec(m_val) % MOD
    return f"{last9:09d}"


if __name__ == "__main__":
    print(solve())
