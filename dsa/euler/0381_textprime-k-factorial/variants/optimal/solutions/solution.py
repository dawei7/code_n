"""Project Euler Problem 381: (prime-k) Factorial.

Find sum_{5 <= p < 10^8} S(p), where S(p) = (sum_{k=1..5} (p-k)!) mod p.
"""

from math import isqrt


def solve(limit: int = 10**8) -> int:
    """Compute sum of S(p) for primes 5 <= p < limit via Wilson's theorem modular reduction."""
    if limit <= 5:
        return 0

    # Odd-only bit/byte sieve up to limit
    half_lim = limit // 2
    is_prime = bytearray([1]) * half_lim

    limit_sqrt = isqrt(limit) // 2
    for i in range(1, limit_sqrt + 1):
        if is_prime[i]:
            p = 2 * i + 1
            start = (p * p) // 2
            is_prime[start::p] = bytearray([0]) * len(is_prime[start::p])

    # Wilson's theorem reduction: S(p) = (-3 / 8) mod p
    total_sum = 0
    for i in range(2, half_lim):  # i=2 corresponds to p = 2*2 + 1 = 5
        if is_prime[i]:
            p = 2 * i + 1
            rem = p & 7
            if rem == 1:
                total_sum += (3 * (p - 1)) // 8
            elif rem == 3:
                total_sum += (p - 3) // 8
            elif rem == 5:
                total_sum += (7 * p - 3) // 8
            elif rem == 7:
                total_sum += (5 * p - 3) // 8

    return total_sum


if __name__ == "__main__":
    print(solve())
