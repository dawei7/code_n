"""Project Euler Problem 439: Sum of Sum of Divisors.

Find S(10^11) mod 10^9, where S(N) = sum_{i=1..N} sum_{j=1..N} d(i*j) and d(k) = sum_{t|k} t.
"""

from array import array
from math import isqrt
from typing import Dict, List

MOD = 1_000_000_000


def solve(n_limit: int = 10**11, mod: int = MOD) -> int:
    """Compute S(n_limit) mod MOD using Du Sieve and hyperbola quotient grouping."""
    sqrt_n = isqrt(n_limit)
    sieve_limit = max(sqrt_n, min(int(n_limit ** (2 / 3)), 6_000_000))

    # Linear sieve for mu and pre_imu
    mu = array("b", [0]) * (sieve_limit + 1)
    is_comp = bytearray(sieve_limit + 1)
    primes: List[int] = []
    mu[1] = 1

    for i in range(2, sieve_limit + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            ip = i * p
            if ip > sieve_limit:
                break
            is_comp[ip] = 1
            if i % p == 0:
                mu[ip] = 0
                break
            mu[ip] = -mu[i]

    pre_imu = array("i", [0]) * (sieve_limit + 1)
    acc = 0
    for i in range(1, sieve_limit + 1):
        acc = (acc + i * mu[i]) % mod
        pre_imu[i] = acc

    imu_cache: Dict[int, int] = {0: 0}

    def imu_func(x: int) -> int:
        if x <= sieve_limit:
            return pre_imu[x]
        got = imu_cache.get(x)
        if got is not None:
            return got
        res = 1 % mod
        i = 2
        while i <= x:
            v = x // i
            j = x // v
            cnt = j - i + 1
            sum_i = (i + j) * cnt // 2
            res = (res - (sum_i % mod) * imu_func(v)) % mod
            i = j + 1
        imu_cache[x] = res
        return res

    sigma = array("i", [0]) * (sqrt_n + 1)
    for d in range(1, sqrt_n + 1):
        for m in range(d, sqrt_n + 1, d):
            sigma[m] += d

    h_small = array("i", [0]) * (sqrt_n + 1)
    acc = 0
    for i in range(1, sqrt_n + 1):
        acc = (acc + sigma[i]) % mod
        h_small[i] = acc

    h_cache: Dict[int, int] = {}

    def h_func(x: int) -> int:
        if x <= sqrt_n:
            return h_small[x]
        got = h_cache.get(x)
        if got is not None:
            return got

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
        h_cache[x] = res
        return res

    total_s = 0
    k = 1
    while k <= n_limit:
        v = n_limit // k
        k_next = n_limit // v
        block_imu = (imu_func(k_next) - imu_func(k - 1)) % mod
        h_v = h_func(v)
        h2 = (h_v * h_v) % mod
        total_s = (total_s + block_imu * h2) % mod
        k = k_next + 1

    return total_s % mod


if __name__ == "__main__":
    print(solve())
