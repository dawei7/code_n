"""Project Euler Problem 618: Numbers with a Given Prime Factor Sum.

Find the last nine digits of sum_{k=2}^{24} S(F_k), where S(k) is the sum of all numbers
whose prime factor sum (with multiplicity) is k.
"""

from typing import List

_MOD = 1_000_000_000


def _sieve_primes(limit: int) -> List[int]:
    if limit < 2:
        return []
    is_p = bytearray(b"\x01") * (limit + 1)
    is_p[0:2] = b"\x00\x00"
    for i in range(2, int(limit**0.5) + 1):
        if is_p[i]:
            is_p[i * i : limit + 1 : i] = b"\x00" * (
                ((limit - i * i) // i) + 1
            )
    return [p for p in range(2, limit + 1) if is_p[p]]


def solve(max_fib_idx: int = 24) -> str:
    """Compute the last 9 digits of sum_{k=2}^max_fib_idx S(F_k) via unbounded polynomial knapsack DP."""
    fib = [0, 1]
    for _ in range(2, max_fib_idx + 1):
        fib.append(fib[-1] + fib[-2])

    max_k = fib[max_fib_idx]
    primes = _sieve_primes(max_k)

    dp = [0] * (max_k + 1)
    dp[0] = 1

    for p in primes:
        for j in range(p, max_k + 1):
            dp[j] = (dp[j] + p * dp[j - p]) % _MOD

    total = sum(dp[fib[k]] for k in range(2, max_fib_idx + 1)) % _MOD
    return f"{total:09d}"


if __name__ == "__main__":
    print(solve())
