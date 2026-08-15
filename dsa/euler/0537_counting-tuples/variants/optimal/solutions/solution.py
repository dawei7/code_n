"""Project Euler Problem 537: Counting Tuples.

Find T(20000, 20000) mod 1_004_535_809, where T(n, k) is the number of k-tuples
of positive integers whose sum of prime counting function pi(x_i) equals n.
"""

import math
from typing import List

MOD = 1_004_535_809  # 479 * 2^21 + 1 (NTT-friendly prime)
G = 3


def _ntt(a: List[int], invert: bool = False) -> None:
    n_len = len(a)
    j = 0
    for i in range(1, n_len):
        bit = n_len >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 2
    while length <= n_len:
        wlen = pow(G, (MOD - 1) // length, MOD)
        if invert:
            wlen = pow(wlen, MOD - 2, MOD)
        for i in range(0, n_len, length):
            w = 1
            for k_idx in range(length // 2):
                u = a[i + k_idx]
                v = (a[i + k_idx + length // 2] * w) % MOD
                a[i + k_idx] = (u + v) % MOD
                a[i + k_idx + length // 2] = (u - v) % MOD
                w = (w * wlen) % MOD
        length <<= 1

    if invert:
        ninv = pow(n_len, MOD - 2, MOD)
        for i in range(n_len):
            a[i] = (a[i] * ninv) % MOD


def _poly_mul(p1: List[int], p2: List[int], deg: int) -> List[int]:
    size = 1
    while size < len(p1) + len(p2):
        size <<= 1
    fa = p1 + [0] * (size - len(p1))
    fb = p2 + [0] * (size - len(p2))
    _ntt(fa)
    _ntt(fb)
    for i in range(size):
        fa[i] = (fa[i] * fb[i]) % MOD
    _ntt(fa, invert=True)
    return fa[: deg + 1]


def solve(n: int = 20000, k: int = 20000) -> int:
    """Compute T(n, k) mod MOD via generating function powers with Number Theoretic Transform."""
    limit = max(300000, int(n * (math.log(n + 10) + math.log(math.log(n + 10)) + 2)))
    is_prime = bytearray(b"\x01") * limit
    is_prime[0] = is_prime[1] = 0
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime[i]:
            is_prime[i * i : limit : i] = b"\x00" * (
                ((limit - 1 - i * i) // i) + 1
            )

    primes = [i for i in range(2, limit) if is_prime[i]]

    c = [0] * (n + 1)
    c[0] = 1
    for j in range(1, n + 1):
        c[j] = (primes[j] - primes[j - 1]) % MOD

    res = [1]
    base = c[:]
    exp = k
    while exp > 0:
        if exp & 1:
            res = _poly_mul(res, base, n)
        exp >>= 1
        if exp > 0:
            base = _poly_mul(base, base, n)

    return res[n]


if __name__ == "__main__":
    print(solve())
