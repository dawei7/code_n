"""Project Euler Problem 245: Coresilience.

Find the sum of all composite integers 1 < n <= 2 * 10^11 for which C(n) is a unit fraction.
"""

import bisect
from math import isqrt


def solve(limit: int = 200000000000) -> int:
    """Find the sum of all composite integers 1 < n <= limit for which C(n) is a unit fraction."""
    if limit < 4:
        return 0

    sqrt_limit = isqrt(limit)
    sieve = bytearray([1]) * (sqrt_limit + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(sqrt_limit) + 1):
        if sieve[i]:
            sieve[i * i : sqrt_limit + 1 : i] = bytearray(
                len(range(i * i, sqrt_limit + 1, i))
            )
    primes = [i for i, v in enumerate(sieve) if v and i > 2]
    mod3_primes = [p for p in primes if p == 3 or p % 3 == 1]

    def is_prime(n: int) -> bool:
        if n <= sqrt_limit:
            return sieve[n] == 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        d = 5
        while d * d <= n:
            if n % d == 0 or n % (d + 2) == 0:
                return False
            d += 6
        return True

    sol = 0

    # 1. Two-prime solutions n = p1 * p2
    for p1 in primes:
        if p1 * p1 > limit:
            break
        V = p1 * p1 - p1 + 1
        divs = [1]
        temp = V
        for q in mod3_primes:
            if q * q > temp:
                break
            if temp % q == 0:
                c = 0
                while temp % q == 0:
                    c += 1
                    temp //= q
                cur = []
                qp = 1
                for _ in range(c + 1):
                    for d in divs:
                        cur.append(d * qp)
                    qp *= q
                divs = cur
        if temp > 1:
            cur = []
            for d in divs:
                cur.append(d)
                cur.append(d * temp)
            divs = cur

        for d in divs:
            p2 = d - p1 + 1
            if p2 > p1 and p1 * p2 <= limit:
                if is_prime(p2):
                    sol += p1 * p2

    # 2. Multi-prime solutions (m >= 3 prime factors)
    def dfs(last_p: int, P: int, Phi: int, depth: int) -> None:
        nonlocal sol

        # Try closing with final prime p
        if depth >= 2:
            denom_term = P - Phi
            min_k_num = last_p * P - 1
            min_k_den = last_p * denom_term + Phi
            min_k = min_k_num // min_k_den + 1
            if min_k % 2 != 0:
                min_k += 1
            max_k = P // denom_term

            for k in range(min_k, max_k + 1, 2):
                denom = P - k * denom_term
                if denom > 0:
                    num = k * Phi + 1
                    if num % denom == 0:
                        p = num // denom
                        if p > last_p and P * p <= limit:
                            if is_prime(p):
                                sol += P * p

        # Branch for intermediate prime
        max_next_p = isqrt(limit // P)
        if depth == 0:
            max_next_p = min(max_next_p, int(limit ** (1 / 3)) + 10)

        start_idx = bisect.bisect_right(primes, last_p)
        end_idx = bisect.bisect_right(primes, max_next_p)

        for i in range(start_idx, end_idx):
            p = primes[i]
            next_P = P * p
            next_Phi = Phi * (p - 1)
            if 2 * next_Phi > next_P:
                dfs(p, next_P, next_Phi, depth + 1)

    dfs(2, 1, 1, 0)

    return sol


if __name__ == "__main__":
    print(solve())
