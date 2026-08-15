"""Project Euler Problem 533: Minimum Values of the Carmichael Function.

Find the last 9 digits of L(20_000_000), where L(n) is the smallest positive integer
such that lambda(k) >= n for all k >= L(n).
"""

from array import array
import math

MOD = 1_000_000_000


def solve(limit_n: int = 20_000_000, mod: int = MOD) -> int:
    """Compute L(limit_n) mod mod by sieving log M(m) to find the maximal pre-image of lambda."""
    limit_primes = limit_n + 100
    is_prime = bytearray(b"\x01") * limit_primes
    is_prime[0] = is_prime[1] = 0

    for i in range(2, math.isqrt(limit_primes) + 1):
        if is_prime[i]:
            is_prime[i * i : limit_primes : i] = b"\x00" * (
                ((limit_primes - 1 - i * i) // i) + 1
            )

    primes = [i for i in range(2, limit_primes) if is_prime[i]]

    log_m = array("f", [0.0]) * limit_n
    ln2 = math.log(2)

    for m in range(1, limit_n):
        log_m[m] += ln2
        if m % 2 == 0:
            temp = m
            v2 = 0
            while temp % 2 == 0:
                v2 += 1
                temp //= 2
            log_m[m] += (v2 + 1) * ln2

    for p in primes:
        if p == 2:
            continue
        pe = p - 1
        if pe >= limit_n:
            break
        log_p = math.log(p)
        while pe < limit_n:
            for m in range(pe, limit_n, pe):
                log_m[m] += log_p
            pe *= p

    best_m = 1
    max_log = log_m[1]
    for m in range(2, limit_n):
        if log_m[m] > max_log:
            max_log = log_m[m]
            best_m = m

    val = 2
    temp = best_m
    v2 = 0
    while temp % 2 == 0:
        v2 += 1
        temp //= 2
    if v2 >= 1:
        val = (val * pow(2, v2 + 1, mod)) % mod

    for p in primes:
        if p == 2:
            continue
        if p - 1 > best_m:
            break
        pe = p - 1
        while best_m % pe == 0:
            val = (val * p) % mod
            pe *= p

    return (val + 1) % mod


if __name__ == "__main__":
    print(solve())
