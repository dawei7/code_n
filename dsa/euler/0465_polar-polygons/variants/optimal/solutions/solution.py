"""Project Euler Problem 465: Polar Polygons.

Find P(7^13) mod 1_000_000_007, the number of polar polygons with vertices
having integer coordinates in [-n, n].
"""

from array import array
from typing import Dict, List

MOD = 1_000_000_007


def _build_totient_prefix(limit: int) -> array:
    if limit < 1:
        return array("Q", [0])

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

    pref = array("Q", [0]) * (limit + 1)
    s = 0
    for i in range(1, limit + 1):
        s += phi[i]
        pref[i] = s
    return pref


def solve(n: int = 7**13, mod: int = MOD) -> int:
    """Compute P(n) mod mod using Du Sieve totient summation and quotient grouping."""
    limit = int(n ** (2 / 3))
    pref = _build_totient_prefix(limit)
    cache: Dict[int, int] = {}

    def tot_sum(x: int) -> int:
        if x <= limit:
            return int(pref[x])
        v = cache.get(x)
        if v is not None:
            return v
        res = x * (x + 1) // 2
        l = 2
        while l <= x:
            q = x // l
            r = x // q
            res -= (r - l + 1) * tot_sum(q)
            l = r + 1
        cache[x] = res
        return res

    b_prod = 1
    s1 = 0
    s2 = 0

    l = 1
    while l <= n:
        q = n // l
        r = n // q

        phi_sum = (tot_sum(r) - tot_sum(l - 1)) % (mod - 1)
        c_count = (4 * phi_sum) % (mod - 1)

        b_prod = (b_prod * pow(q + 1, c_count, mod)) % mod
        c_mod = (4 * (tot_sum(r) - tot_sum(l - 1))) % mod

        s1 = (s1 + c_mod * q) % mod
        s2 = (s2 + c_mod * ((q * q) % mod)) % mod

        l = r + 1

    ans = (b_prod * b_prod - 2 * b_prod * s1 + s2 - 1) % mod
    return ans


if __name__ == "__main__":
    print(solve())
