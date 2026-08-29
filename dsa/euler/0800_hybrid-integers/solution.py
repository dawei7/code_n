"""Project Euler Problem 800: Hybrid Integers.

Find C(800800^800800), the number of hybrid-integers p^q * q^p <= n with primes p < q.
"""

import math
from typing import List


def _sieve_primes(limit: int) -> List[int]:
    """Return all primes up to limit using a memory-efficient bytearray sieve."""
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime[i]:
            is_prime[i * i :: i] = bytearray([0]) * len(is_prime[i * i :: i])
    return [i for i, v in enumerate(is_prime) if v]


def solve(a: int = 800800, b: int = 800800) -> int:
    """Compute C(a^b) using logarithmic transformation and two-pointer prime scan."""
    limit = b * math.log(a)
    max_q = int(limit / math.log(2)) + 1000

    primes = _sieve_primes(max_q)

    ans = 0
    left = 0
    right = len(primes) - 1

    while left < right:
        p = primes[left]
        log_p = math.log(p)
        if 2 * p * log_p > limit:
            break
        while right > left:
            q = primes[right]
            log_q = math.log(q)
            if q * log_p + p * log_q <= limit:
                break
            right -= 1
        if right <= left:
            break
        ans += right - left
        left += 1

    return ans


if __name__ == "__main__":
    print(solve())
