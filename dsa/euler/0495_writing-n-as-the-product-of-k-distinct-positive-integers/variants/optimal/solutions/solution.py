"""Project Euler Problem 495: Writing n as the Product of k Distinct Positive Integers.

Find W(10000!, 30) mod 1_000_000_007, where W(n, k) is the number of ways
to write n as the product of k distinct positive integers.
"""

from array import array
from math import isqrt
from typing import Dict, Iterator, List, Optional

MOD = 1_000_000_007


def _sieve_primes_upto(n: int) -> List[int]:
    if n < 2:
        return []
    bs = bytearray(b"\x01") * (n + 1)
    bs[0:2] = b"\x00\x00"
    lim = isqrt(n)
    for i in range(2, lim + 1):
        if bs[i]:
            step = i
            start = i * i
            bs[start : n + 1 : step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i in range(n + 1) if bs[i]]


def _factorial_prime_exponent_frequencies(n: int) -> Dict[int, int]:
    primes = _sieve_primes_upto(n)
    freq: Dict[int, int] = {}
    for p in primes:
        e = 0
        nn = n
        while nn:
            nn //= p
            e += nn
        freq[e] = freq.get(e, 0) + 1
    return freq


def _partitions_of(
    n: int, max_part: Optional[int] = None
) -> Iterator[List[int]]:
    if max_part is None or max_part > n:
        max_part = n
    if n == 0:
        yield []
        return
    for first in range(max_part, 0, -1):
        for rest in _partitions_of(n - first, first):
            yield [first] + rest


def _precompute_base_ones_twos(max_e: int, k: int) -> List[List[array]]:
    inv = [0] * (max_e + 1)
    if max_e >= 1:
        inv[1] = 1
        for i in range(2, max_e + 1):
            inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

    ones = [None] * (k + 1)
    ones[0] = [0] * (max_e + 1)
    ones[0][0] = 1
    for r1 in range(1, k + 1):
        dp = [0] * (max_e + 1)
        dp[0] = 1
        for t in range(1, max_e + 1):
            dp[t] = (dp[t - 1] * (r1 + t - 1) % MOD) * inv[t] % MOD
        ones[r1] = dp

    base: List[List[array]] = [
        [None] * (k // 2 + 1) for _ in range(k + 1)
    ]
    for r1 in range(k + 1):
        base[r1][0] = array("I", ones[r1])
        for r2 in range(1, k // 2 + 1):
            dp = list(base[r1][r2 - 1])
            for t in range(2, max_e + 1):
                x = dp[t] + dp[t - 2]
                if x >= MOD:
                    x -= MOD
                dp[t] = x
            base[r1][r2] = array("I", dp)
    return base


def solve(n: int = 10000, k: int = 30, mod: int = MOD) -> int:
    """Compute W(n!, k) mod mod using cycle index / symmetric group character partition expansion."""
    freq = _factorial_prime_exponent_frequencies(n)
    exponents = sorted(freq.keys())
    max_e = max(exponents) if exponents else 0
    exp_freq = [(e, freq[e]) for e in exponents]

    fact = [1] * (k + 1)
    for i in range(1, k + 1):
        fact[i] = fact[i - 1] * i % mod

    inv_fact = [1] * (k + 1)
    inv_fact[k] = pow(fact[k], mod - 2, mod)
    for i in range(k, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % mod

    inv_pow = [[1] * (k + 1) for _ in range(k + 1)]
    for s in range(1, k + 1):
        invs = pow(s, mod - 2, mod)
        acc = 1
        for c in range(1, k + 1):
            acc = (acc * invs) % mod
            inv_pow[s][c] = acc

    base = _precompute_base_ones_twos(max_e, k)
    total = 0
    freq1 = freq.get(1, 0)

    for parts in _partitions_of(k):
        b = len(parts)
        r1 = r2 = 0
        i = b - 1
        while i >= 0 and parts[i] == 1:
            r1 += 1
            i -= 1
        while i >= 0 and parts[i] == 2:
            r2 += 1
            i -= 1

        if r1 == 0 and freq1:
            continue

        rem_parts = parts[: i + 1]
        dp = list(base[r1][r2])
        for m in rem_parts:
            for t in range(m, max_e + 1):
                x = dp[t] + dp[t - m]
                if x >= mod:
                    x -= mod
                dp[t] = x

        fval = 1
        for e, fe in exp_freq:
            c = dp[e]
            if c == 0:
                fval = 0
                break
            if fe == 1:
                fval = (fval * c) % mod
            else:
                if c != 1:
                    fval = (fval * pow(c, fe, mod)) % mod
        if fval == 0:
            continue

        w = 1
        j = 0
        while j < b:
            s = parts[j]
            jj = j + 1
            while jj < b and parts[jj] == s:
                jj += 1
            cnt = jj - j
            w = (w * inv_pow[s][cnt]) % mod
            w = (w * inv_fact[cnt]) % mod
            j = jj
        if (k - b) & 1:
            w = mod - w

        total = (total + w * fval) % mod

    return total


if __name__ == "__main__":
    print(solve())
