"""Project Euler Problem 417: Reciprocal Cycles II.

Find sum_{n=3..10^8} L(n), where L(n) is the recurring cycle length of 1/n.
"""

from array import array
from bisect import bisect_right
from math import gcd, isqrt
from typing import Dict, List


def _gen_two_five_products(limit: int) -> List[int]:
    res: List[int] = []
    p2 = 1
    while p2 <= limit:
        p5 = 1
        while p2 * p5 <= limit:
            res.append(p2 * p5)
            p5 *= 5
        p2 *= 2
    return sorted(set(res))


def _build_spf_odd(limit: int) -> array:
    spf = array("I", [0]) * (limit // 2 + 1)
    root = isqrt(limit)
    for p in range(3, root + 1, 2):
        if spf[p // 2] == 0:
            step = p * 2
            start = p * p
            for x in range(start, limit + 1, step):
                idx = x // 2
                if spf[idx] == 0:
                    spf[idx] = p
    return spf


def _multiplicative_order_prime(p: int, spf: array) -> int:
    n = p - 1
    factors = [2]
    while (n & 1) == 0:
        n //= 2
    while n > 1:
        q = spf[n // 2]
        if q == 0:
            q = n
        factors.append(q)
        while n % q == 0:
            n //= q

    order = p - 1
    for q in factors:
        while order % q == 0 and pow(10, order // q, p) == 1:
            order //= q
    return order


def solve(max_n: int = 100_000_000) -> int:
    """Compute sum_{3<=n<=max_n} L(n) using odd SPF order propagation and 2^a*5^b multiplicity counting."""
    products_big = _gen_two_five_products(max_n)
    cache_big: Dict[int, int] = {}

    def g_big(x: int) -> int:
        v = cache_big.get(x)
        if v is None:
            v = bisect_right(products_big, x)
            cache_big[x] = v
        return v

    spf = _build_spf_odd(max_n)
    order = array("I", [0]) * (max_n // 2 + 1)
    order[0] = 1

    ppow_cache: Dict[int, List[int]] = {}
    s_big = 0

    for n in range(3, max_n + 1, 2):
        if n % 5 == 0:
            continue
        idx = n // 2
        p = spf[idx]

        if p == 0:
            # n is prime
            o = _multiplicative_order_prime(n, spf)
        else:
            # n is composite
            m = n
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            rest = m

            a = order[rest // 2] if rest > 1 else 1

            if e == 1:
                b = order[p // 2]
            else:
                lst = ppow_cache.get(p)
                if lst is None:
                    t = p
                    maxe = 0
                    while t <= max_n:
                        maxe += 1
                        t *= p

                    lst = [0] * (maxe + 1)
                    ord_p = order[p // 2]
                    lst[1] = ord_p
                    ordk = ord_p
                    mod_p = p
                    for k in range(2, maxe + 1):
                        mod_p *= p
                        if pow(10, ordk, mod_p) != 1:
                            ordk *= p
                        lst[k] = ordk
                    ppow_cache[p] = lst

                b = ppow_cache[p][e]

            o = a // gcd(a, b) * b

        order[idx] = o
        s_big += o * g_big(max_n // n)

    return s_big


if __name__ == "__main__":
    print(solve())
