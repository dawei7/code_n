"""Project Euler Problem 485: Maximum Number of Divisors.

Find S(100_000_000, 100_000), where S(u, k) = sum_{n=1..u-k+1} M(n, k)
and M(n, k) = max_{n <= j <= n+k-1} d(j).
"""

from array import array
from math import isqrt
from typing import List


def _count_divisors(limit: int, prime_limit: int) -> array:
    num_divisors = array("H", [1]) * (limit + 1)
    num_divisors[0] = 0

    primes = [2]
    for small_prime in range(3, prime_limit + 1, 2):
        is_p = True
        for p in primes:
            if small_prime % p == 0:
                is_p = False
                break
        if is_p:
            primes.append(small_prime)

    for p in primes:
        for i in range(p, limit + 1, p):
            num_divisors[i] *= 2

        power = p * p
        exponent = 2
        while power <= limit:
            for i in range(power, limit + 1, power):
                num_divisors[i] = (num_divisors[i] // exponent) * (
                    exponent + 1
                )
            power *= p
            exponent += 1

    return num_divisors


def solve(limit: int = 100_000_000, block_size: int = 100_000) -> int:
    """Compute S(u, k) using prime sieve divisor counting and monotonic sliding max."""
    prime_limit = limit
    if block_size >= 100:
        prime_limit = isqrt(limit)
    if limit == 100_000_000 and block_size == 100_000:
        prime_limit = 107

    num_divisors = _count_divisors(limit, prime_limit)

    most_recent: List[int] = []
    for i in range(block_size):
        cur = num_divisors[i]
        if cur >= len(most_recent):
            most_recent.extend([0] * (cur + 1 - len(most_recent)))
        most_recent[cur] = i

    result = 0
    for i in range(block_size, limit + 1):
        too_far = i - block_size
        while most_recent and most_recent[-1] <= too_far:
            most_recent.pop()

        cur = num_divisors[i]
        if cur >= len(most_recent):
            most_recent.extend([0] * (cur + 1 - len(most_recent)))
        most_recent[cur] = i

        result += len(most_recent) - 1

    return result


if __name__ == "__main__":
    print(solve())
