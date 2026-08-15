"""Project Euler Problem 475: Music Festival.

Find f(600) mod 1_000_000_007, the number of ways to organize 4n trios
from 3n quartets of 12n musicians such that no two musicians from the same quartet
share a trio.
"""

from typing import List, Tuple

MOD = 1_000_000_007


def _prep_factorials(limit: int, mod: int = MOD) -> Tuple[List[int], List[int]]:
    fact = [1] * (limit + 1)
    for i in range(1, limit + 1):
        fact[i] = (fact[i - 1] * i) % mod

    invfact = [1] * (limit + 1)
    invfact[limit] = pow(fact[limit], mod - 2, mod)
    for i in range(limit, 0, -1):
        invfact[i - 1] = (invfact[i] * i) % mod

    return fact, invfact


def solve(total_musicians: int = 600, mod: int = MOD) -> int:
    """Compute f(12n) mod mod using exponential generating function closed reduction."""
    n = total_musicians // 12
    e_trios = 4 * n
    m_quartets = 3 * n

    limit = 16 * n + 10
    fact, invfact = _prep_factorials(limit, mod)

    pow2 = [1] * (e_trios + 1)
    for t in range(1, e_trios + 1):
        pow2[t] = (pow2[t - 1] * 2) % mod

    neg3 = mod - 3
    pow_neg3 = [1] * (e_trios + 1)
    for t in range(1, e_trios + 1):
        pow_neg3[t] = (pow_neg3[t - 1] * neg3) % mod

    inv2 = (mod + 1) // 2
    inv24 = pow(24, mod - 2, mod)

    inv24pow = [1] * (m_quartets + 1)
    for t in range(1, m_quartets + 1):
        inv24pow[t] = (inv24pow[t - 1] * inv24) % mod

    inv2pow = [1] * (e_trios + 1)
    for t in range(1, e_trios + 1):
        inv2pow[t] = (inv2pow[t - 1] * inv2) % mod

    sigma = 0
    for i in range(e_trios + 1):
        max_j = e_trios - i
        for j in range(max_j + 1):
            k = e_trios - i - j
            a_idx = 3 * i + j

            base = (fact[a_idx] * invfact[i]) % mod
            base = (base * pow_neg3[j]) % mod
            base = (base * pow2[k]) % mod

            dmin = 0 if i >= n else (n - i)
            dmax = j // 2
            if dmin > dmax:
                continue

            invfact_c = invfact[k]
            sumd = 0
            for d in range(dmin, dmax + 1):
                a = i - n + d
                b = j - 2 * d

                term = invfact[a]
                term = (term * invfact[b]) % mod
                term = (term * invfact_c) % mod
                term = (term * invfact[d]) % mod
                term = (term * inv24pow[a]) % mod
                term = (term * inv2pow[b + d]) % mod

                sumd = (sumd + term) % mod

            sigma = (sigma + base * sumd) % mod

    pow24m = pow(24, m_quartets, mod)
    inv6e = pow(pow(6, e_trios, mod), mod - 2, mod)
    return (
        pow24m * fact[m_quartets] % mod * sigma % mod * inv6e % mod
    )


if __name__ == "__main__":
    print(solve())
