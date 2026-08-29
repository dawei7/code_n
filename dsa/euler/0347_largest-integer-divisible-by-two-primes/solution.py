"""Project Euler 347: Largest Integer Divisible by Two Primes

Find S(10_000_000), the sum of all distinct M(p, q, N), where M(p, q, N) is the largest positive integer <= N divisible only by both primes p and q.
"""

from __future__ import annotations


def solve(n: int = 10_000_000) -> str:
    """Calculates S(n) in pure Python in ~0.6s using a prime sieve,

    powers maximization over (p^a * q^b <= N), and a distinct value hash set.
    """
    limit_primes = n // 2
    is_prime = bytearray([1]) * (limit_primes + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(limit_primes**0.5) + 1):
        if is_prime[i]:
            is_prime[i * i : limit_primes + 1 : i] = bytearray([0]) * len(
                is_prime[i * i : limit_primes + 1 : i]
            )

    primes = [i for i, v in enumerate(is_prime) if v]
    sqrt_n = int(n**0.5)
    distinct_vals: set[int] = set()

    for p in primes:
        if p > sqrt_n:
            break
        for q in primes:
            if q <= p:
                continue
            if p * q > n:
                break

            best = 0
            pa = p
            while pa * q <= n:
                val = pa * q
                while val * q <= n:
                    val *= q
                if val > best:
                    best = val
                pa *= p

            if best > 0:
                distinct_vals.add(best)

    total_sum = sum(distinct_vals)
    return str(total_sum)


if __name__ == "__main__":
    print(solve())
