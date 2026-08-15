"""Project Euler 274: Divisibility Multipliers

Find the sum of the divisibility multipliers for all primes coprime to 10 and less than 10^7.
"""

from __future__ import annotations


def solve(limit: int = 10**7) -> str:
    """Calculates the sum of divisibility multipliers m = 10^-1 mod p for all primes p < limit

    coprime to 10 using direct O(1) modular inversion based on the terminal digit of p.
    """
    sieve = [True] * limit
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

    k_map = {1: 9, 3: 3, 7: 7, 9: 1}
    total_multiplier_sum = 0

    for p in range(3, limit):
        if sieve[p] and p != 5:
            k = k_map[p % 10]
            m = (k * p + 1) // 10
            total_multiplier_sum += m

    return str(total_multiplier_sum)


if __name__ == "__main__":
    print(solve())
