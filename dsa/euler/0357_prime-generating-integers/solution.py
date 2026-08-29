"""Project Euler Problem 357: Prime Generating Integers.

Find the sum of all positive integers n <= 100,000,000 such that d + n/d is prime for all divisors d of n.
"""

from math import isqrt


def solve(limit: int = 100000000) -> int:
    """Find the sum of all positive integers n <= limit such that d + n/d is prime for all divisors d of n."""
    if limit <= 0:
        return 0

    # Sieve primes up to limit + 1
    sieve = bytearray([1]) * (limit + 2)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(limit + 1) + 1):
        if sieve[i]:
            sieve[i * i : limit + 2 : i] = bytearray(
                len(range(i * i, limit + 2, i))
            )

    total_sum = 1  # n = 1 (1 + 1 = 2 prime)

    # Valid composite n must satisfy:
    # 1. n is even and square-free (n == 2 mod 4)
    # 2. n + 1 is prime (d = 1)
    # 3. 2 + n / 2 is prime (d = 2)
    for n in range(2, limit + 1, 4):
        if not sieve[n + 1]:
            continue
        if not sieve[2 + n // 2]:
            continue

        valid = True
        limit_d = isqrt(n)
        for d in range(3, limit_d + 1):
            if n % d == 0:
                if not sieve[d + n // d]:
                    valid = False
                    break

        if valid:
            total_sum += n

    return total_sum


if __name__ == "__main__":
    print(solve())
