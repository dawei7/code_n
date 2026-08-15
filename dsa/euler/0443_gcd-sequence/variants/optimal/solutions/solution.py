"""Project Euler Problem 443: GCD Sequence.

Find g(10^15), where g(4) = 13 and g(n) = g(n-1) + gcd(n, g(n-1)) for n > 4.
"""

from math import gcd


def _is_prime(value: int) -> bool:
    if value < 2:
        return False

    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small_primes:
        if value == prime:
            return True
        if value % prime == 0:
            return False

    d = value - 1
    shifts = 0
    while (d & 1) == 0:
        d >>= 1
        shifts += 1

    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % value == 0:
            continue
        x = pow(base, d, value)
        if x == 1 or x == value - 1:
            continue
        for _ in range(shifts - 1):
            x = (x * x) % value
            if x == value - 1:
                break
        else:
            return False

    return True


def _smallest_prime_factor(value: int) -> int:
    if _is_prime(value):
        return value
    if value % 3 == 0:
        return 3

    factor = 5
    step = 2
    while factor * factor <= value:
        if value % factor == 0:
            return factor
        factor += step
        step = 6 - step

    return value


def solve(n: int = 10**15) -> int:
    """Compute g(n) using the 3k structural jump theorem and prime factorization of 2k-1."""
    if n < 9:
        current = 13
        for index in range(5, n + 1):
            current += gcd(index, current)
        return current

    structural_index = 9
    while True:
        prime = _smallest_prime_factor(2 * structural_index - 1)
        next_index = structural_index + (prime - 1) // 2

        if next_index > n:
            return n + 2 * structural_index
        if next_index == n:
            return 3 * n
        structural_index = next_index


if __name__ == "__main__":
    print(solve())
