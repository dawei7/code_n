"""Project Euler Problem 447: Retractions C.

Find F(10^14) mod 1000000007, where F(N) = sum_{n=2..N} R(n)
and R(n) is the number of retractions modulo n.
"""

from array import array
from math import isqrt
from typing import List

MOD = 1_000_000_007


def solve(n_limit: int = 10**14, mod: int = MOD) -> int:
    """Compute F(n_limit) mod mod using square-free Möbius convolution and divisor hyperbola sums."""
    sqrt_n = isqrt(n_limit)

    mu = array("b", [0]) * (sqrt_n + 1)
    mu[1] = 1
    is_comp = bytearray(sqrt_n + 1)
    primes: List[int] = []

    for i in range(2, sqrt_n + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > sqrt_n:
                break
            is_comp[ip] = 1
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]

    h_limit = min(5_000_000, sqrt_n)
    sigma = array("i", [0]) * (h_limit + 1)
    for d in range(1, h_limit + 1):
        for m in range(d, h_limit + 1, d):
            sigma[m] += d
    h_small = array("i", [0]) * (h_limit + 1)
    acc = 0
    for i in range(1, h_limit + 1):
        acc = (acc + sigma[i]) % mod
        h_small[i] = acc

    def h_func(x: int) -> int:
        if x <= h_limit:
            return h_small[x]
        res = 0
        r = isqrt(x)
        for t in range(1, r + 1):
            res = (res + t * (x // t)) % mod
        for v in range(1, x // (r + 1) + 1):
            lo = x // (v + 1) + 1
            hi = x // v
            if lo <= hi:
                cnt = hi - lo + 1
                sum_t = (lo + hi) * cnt // 2
                res = (res + (sum_t % mod) * v) % mod
        return res

    total_u = 0
    for k in range(1, sqrt_n + 1):
        mk = mu[k]
        if mk == 0:
            continue
        v = n_limit // (k * k)
        term = (k * h_func(v)) % mod
        if mk == 1:
            total_u = (total_u + term) % mod
        else:
            total_u = (total_u - term) % mod

    sum_n = (n_limit % mod) * ((n_limit + 1) % mod) % mod
    sum_n = (sum_n * ((mod + 1) // 2)) % mod
    return (total_u - sum_n) % mod


if __name__ == "__main__":
    print(solve())
