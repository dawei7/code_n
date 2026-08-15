"""Project Euler Problem 446: Retractions B.

Find F(10^7) mod 1000000007, where F(N) = sum_{n=1..N} R(n^4 + 4)
and R(m) is the number of retractions modulo m.
"""

from array import array
from math import isqrt
from typing import List

MOD = 1_000_000_007


def _primes_upto(limit: int) -> List[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit // 2 + 1)
    sieve[0] = 0
    r = isqrt(limit)
    for x in range(3, r + 1, 2):
        if sieve[x // 2]:
            start = x * x // 2
            step = x
            sieve[start::step] = b"\x00" * (
                ((len(sieve) - start - 1) // step) + 1
            )
    primes = [2]
    primes.extend(2 * i + 1 for i in range(1, len(sieve)) if sieve[i])
    return primes


_NONRES_CANDIDATES = (
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
)


def _sqrt_minus_one_mod_prime(p: int) -> int:
    leg_exp = (p - 1) // 2
    quarter = (p - 1) // 4
    for g in _NONRES_CANDIDATES:
        if g >= p:
            break
        if pow(g, leg_exp, p) == p - 1:
            return pow(g, quarter, p)
    g = 115
    while True:
        if pow(g, leg_exp, p) == p - 1:
            return pow(g, quarter, p)
        g += 2


def solve(n_limit: int = 10_000_000) -> int:
    """Compute F(n_limit) mod MOD using Sophie Germain polynomial sieve on n^2+1."""
    if n_limit < 1:
        return 0

    k_max = n_limit + 1
    prime_limit = k_max

    primes = _primes_upto(prime_limit)
    p_list = array("I", [2])
    r_list = array("I", [1])
    for p in primes[1:]:
        if (p & 3) == 1:
            p_list.append(p)
            r_list.append(_sqrt_minus_one_mod_prime(p))

    correction_even = (5 * pow(9, MOD - 2, MOD)) % MOD

    block_size = 1_000_000
    total = 0

    prev2_p = None
    prev1_p = None
    prev2_c = None
    prev1_c = None

    for l_val in range(0, k_max + 1, block_size):
        r_val = min(k_max + 1, l_val + block_size)
        size = r_val - l_val

        rem = array("Q", [0]) * size
        prod = array("I", [1]) * size
        cmod = array("I", [0]) * size

        k = l_val
        v = k * k + 1
        for i in range(size):
            rem[i] = v
            cmod[i] = v % MOD
            v += 2 * k + 1
            k += 1

        mod = MOD
        rem_arr = rem
        prod_arr = prod

        for j in range(len(p_list)):
            p = p_list[j]
            r = r_list[j]
            if p == 2:
                start = (1 - l_val) & 1
                for idx in range(start, size, 2):
                    rem_arr[idx] //= 2
                    prod_arr[idx] = (prod_arr[idx] * 3) % mod
                continue

            start = (r - l_val) % p
            for idx in range(start, size, p):
                x = rem_arr[idx] // p
                pe = p
                while x % p == 0:
                    x //= p
                    pe *= p
                rem_arr[idx] = x
                t = pe + 1
                if t >= mod:
                    t %= mod
                prod_arr[idx] = (prod_arr[idx] * t) % mod

            r2 = p - r
            start = (r2 - l_val) % p
            for idx in range(start, size, p):
                x = rem_arr[idx] // p
                pe = p
                while x % p == 0:
                    x //= p
                    pe *= p
                rem_arr[idx] = x
                t = pe + 1
                if t >= mod:
                    t %= mod
                prod_arr[idx] = (prod_arr[idx] * t) % mod

        for i in range(size):
            x = rem_arr[i]
            if x > 1:
                t = x + 1
                if t >= mod:
                    t %= mod
                prod_arr[i] = (prod_arr[i] * t) % mod

        for i in range(size):
            k = l_val + i
            pk = prod_arr[i]
            ck = cmod[i]

            if prev2_p is not None:
                n = k - 1
                if n <= n_limit:
                    pm = (prev2_p * pk) % mod
                    if (n & 1) == 0:
                        pm = (pm * correction_even) % mod
                    mm = (prev2_c * ck) % mod
                    total = (total + pm - mm) % mod

            prev2_p, prev1_p = prev1_p, pk
            prev2_c, prev1_c = prev1_c, ck

    return total % MOD


if __name__ == "__main__":
    print(solve())
