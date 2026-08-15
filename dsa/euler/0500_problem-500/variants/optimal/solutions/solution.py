"""Project Euler Problem 500: Problem 500!!!.

Find the smallest number with 2^500500 divisors modulo 500500507.
"""

import heapq
from math import isqrt
from typing import List

MOD = 500500507


def _sieve_primes(limit: int) -> List[int]:
    if limit < 2:
        return []
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for i in range(2, isqrt(limit) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            is_prime[start : limit + 1 : step] = b"\x00" * (
                ((limit - start) // step) + 1
            )
    return [i for i, v in enumerate(is_prime) if v]


def solve(target_power: int = 500500, mod: int = MOD) -> int:
    """Compute smallest number with 2^target_power divisors mod mod via greedy min-heap factor selection."""
    limit = 8_000_000
    primes = _sieve_primes(limit)

    heap = primes[:target_power]
    heapq.heapify(heap)

    ans = 1
    for _ in range(target_power):
        val = heapq.heappop(heap)
        ans = (ans * val) % mod
        heapq.heappush(heap, val * val)

    return ans


if __name__ == "__main__":
    print(solve())
