"""Project Euler Problem 808: Reversible Prime Squares.

Find the sum of the first 50 reversible prime squares.
"""

import math


def is_prime(n: int) -> bool:
    """Deterministic primality test for integers."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, math.isqrt(n) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def solve(target_count: int = 50) -> int:
    """Find the sum of the first target_count reversible prime squares using a linear prime sieve."""
    max_p = 40_000_000
    sieve = bytearray(b"\x01") * (max_p + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(max_p) + 1):
        if sieve[p]:
            sieve[p * p : max_p + 1 : p] = b"\x00" * (((max_p - p * p) // p) + 1)

    primes = [p for p in range(2, max_p + 1) if sieve[p]]

    rps = []
    for p in primes:
        p2 = p * p
        s = str(p2)
        s_rev = s[::-1]
        if s == s_rev:
            continue
        r = int(s_rev)
        q = math.isqrt(r)
        if q * q == r:
            if q <= max_p:
                if sieve[q]:
                    rps.append(p2)
            else:
                if is_prime(q):
                    rps.append(p2)
            if len(rps) == target_count:
                break

    return sum(rps)


if __name__ == "__main__":
    print(solve())
