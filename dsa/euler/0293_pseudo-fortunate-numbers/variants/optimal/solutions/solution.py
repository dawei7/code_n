"""Project Euler 293: Pseudo-Fortunate Numbers

Find the sum of all distinct pseudo-Fortunate numbers for admissible numbers N < 10^9.
An even positive integer N is admissible if its distinct prime factors are consecutive primes starting from 2.
The pseudo-Fortunate number for N is the smallest integer M > 1 such that N + M is prime.
"""

from __future__ import annotations


def is_prime(n: int) -> bool:
    """Deterministic primality test for n < 2 * 10^9."""
    if n < 2:
        return False
    if n in (2, 3, 5, 7):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def solve(limit_n: int = 10**9) -> str:
    """Finds all admissible numbers N < limit_n, computes their pseudo-Fortunate numbers M,

    and returns the sum of distinct M values.
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    admissible: list[int] = []

    def generate_admissible(idx: int, cur_val: int) -> None:
        if cur_val >= limit_n:
            return
        admissible.append(cur_val)
        # Multiply by current prime again:
        generate_admissible(idx, cur_val * primes[idx])
        # Transition to next consecutive prime:
        if idx + 1 < len(primes):
            generate_admissible(idx + 1, cur_val * primes[idx + 1])

    generate_admissible(0, 2)

    distinct_m: set[int] = set()
    for n_val in admissible:
        m = 3
        while not is_prime(n_val + m):
            m += 2
        distinct_m.add(m)

    total_sum = sum(distinct_m)
    return str(total_sum)


if __name__ == "__main__":
    print(solve())
