"""Project Euler Problem 448: Average Least Common Multiple.

Find S(99999999019) mod 999999017, where S(N) = sum_{k=1..N} A(k)
and A(n) is the average of lcm(n, i) for 1 <= i <= n.
"""

from array import array
from math import isqrt
from typing import Dict, List

MOD = 999_999_017


def solve(n_limit: int = 99_999_999_019, mod: int = MOD) -> int:
    """Compute S(n_limit) mod MOD using Du Sieve on Phi_1(x) = sum_{d<=x} d*phi(d)."""
    sqrt_n = isqrt(n_limit)
    sieve_limit = max(sqrt_n, min(int(n_limit ** (2 / 3)), 8_000_000))

    phi = array("i", range(sieve_limit + 1))
    is_comp = bytearray(sieve_limit + 1)
    primes: List[int] = []

    for i in range(2, sieve_limit + 1):
        if not is_comp[i]:
            primes.append(i)
            phi[i] = i - 1
        for p in primes:
            ip = i * p
            if ip > sieve_limit:
                break
            is_comp[ip] = 1
            if i % p == 0:
                phi[ip] = phi[i] * p
                break
            phi[ip] = phi[i] * (p - 1)

    pre_phi1 = array("i", [0]) * (sieve_limit + 1)
    acc = 0
    for i in range(1, sieve_limit + 1):
        acc = (acc + i * phi[i]) % mod
        pre_phi1[i] = acc

    phi1_cache: Dict[int, int] = {}
    inv6 = pow(6, mod - 2, mod)

    def sum_sq(x: int) -> int:
        xm = x % mod
        return (
            xm * (xm + 1) % mod * (2 * xm + 1) % mod * inv6 % mod
        )

    def phi1_func(x: int) -> int:
        if x <= sieve_limit:
            return pre_phi1[x]
        got = phi1_cache.get(x)
        if got is not None:
            return got
        res = sum_sq(x)
        i = 2
        while i <= x:
            v = x // i
            j = x // v
            cnt = j - i + 1
            sum_i = (i + j) * cnt // 2
            res = (res - (sum_i % mod) * phi1_func(v)) % mod
            i = j + 1
        phi1_cache[x] = res
        return res

    total_f = 0
    k = 1
    while k <= n_limit:
        v = n_limit // k
        k_next = n_limit // v
        block_phi1 = (phi1_func(k_next) - phi1_func(k - 1)) % mod
        total_f = (total_f + block_phi1 * (v % mod)) % mod
        k = k_next + 1

    inv2 = (mod + 1) // 2
    return (n_limit % mod + total_f) % mod * inv2 % mod


if __name__ == "__main__":
    print(solve())
