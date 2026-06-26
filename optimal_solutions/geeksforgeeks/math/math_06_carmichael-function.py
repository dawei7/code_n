"""Optimal solution for math_06: Carmichael Function.

Factor n. lambda per prime power: p^(k-1) * (p-1) for odd
primes, 2^(k-2) for n=2^k (k>=3). Combine via lcm.
"""


def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 4:
        return 2
    temp = n
    factors = {}
    p = 2
    while p * p <= temp:
        while temp % p == 0:
            factors[p] = factors.get(p, 0) + 1
            temp //= p
        p += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    from math import gcd
    lam = 1
    for p, k in factors.items():
        if p == 2:
            if k == 1:
                pk_lam = 1
            elif k == 2:
                pk_lam = 2
            else:
                pk_lam = 2 ** (k - 2)
        else:
            pk_lam = (p ** (k - 1)) * (p - 1)
        lam = lam * pk_lam // gcd(lam, pk_lam)
    return lam
