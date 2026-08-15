"""Project Euler Problem 111: Primes with Runs.

Mathematical Formulation:
Find sum of S(10, d) for d = 0..9, where M(n, d) is the maximum number of repeated digits d
in an n-digit prime, and S(n, d) is the sum of all such primes.
"""

from __future__ import annotations

import itertools
import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.isqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def solve(n_digits: int = 10) -> str:
    """Compute sum of S(10, d) for all digits d in 0..9."""
    total_sum = 0
    for d in range(10):
        found = set()
        for m in range(n_digits - 1, 0, -1):
            other_count = n_digits - m
            for positions in itertools.combinations(range(n_digits), other_count):
                other_digits_choices = [[x for x in range(10) if x != d] for _ in range(other_count)]
                for others in itertools.product(*other_digits_choices):
                    arr = [d] * n_digits
                    for pos, val in zip(positions, others):
                        arr[pos] = val
                    if arr[0] == 0:
                        continue
                    num = 0
                    for digit in arr:
                        num = num * 10 + digit
                    if is_prime(num):
                        found.add(num)
            if found:
                total_sum += sum(found)
                break
    return str(total_sum)


if __name__ == "__main__":
    print(solve())
