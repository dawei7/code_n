"""Project Euler Problem 694: Cube-full Divisors.

Find S(10^18), where S(n) = sum_{i=1}^n s(i) and s(i) is the number of cube-full divisors of i.
"""

from typing import List


def _sieve_primes(limit: int) -> List[int]:
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            is_prime[i * i :: i] = bytearray(len(is_prime[i * i :: i]))
    return [i for i, p in enumerate(is_prime) if p]


def solve(n: int = 1_000_000_000_000_000_000) -> int:
    """Compute S(n) = sum_{d <= n, d cube-full} floor(n / d) via recursive depth-first search."""
    limit = int(round(n ** (1.0 / 3.0)))
    primes = _sieve_primes(limit)

    total = 0

    def dfs(idx: int, cur: int) -> None:
        nonlocal total
        total += n // cur
        for i in range(idx, len(primes)):
            p = primes[i]
            p3 = p * p * p
            if cur > n // p3:
                break
            mult = p3
            while cur <= n // mult:
                dfs(i + 1, cur * mult)
                if mult > n // (cur * p):
                    break
                mult *= p

    dfs(0, 1)
    return total


if __name__ == "__main__":
    print(solve())
