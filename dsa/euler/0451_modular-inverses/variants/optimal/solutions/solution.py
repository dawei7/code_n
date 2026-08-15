"""Project Euler Problem 451: Modular Inverses.

Find sum_{n=3..2*10^7} I(n), where I(n) is the largest integer m < n - 1
such that m^2 = 1 (mod n).
"""

from array import array
from typing import List


def _smallest_prime_factors(n: int) -> array:
    spf = array("i", range(n + 1))
    root = int(n**0.5)
    for p in range(2, root + 1):
        if spf[p] != p:
            continue
        for multiple in range(p * p, n + 1, p):
            if spf[multiple] == multiple:
                spf[multiple] = p
    return spf


def _modular_inverse(a: int, modulus: int) -> int:
    b = modulus
    x0, x1 = 1, 0
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
    return x0 % modulus


def solve(limit: int = 20_000_000) -> int:
    """Compute sum_{n=3..limit} I(n) via CRT idempotents and square roots of unity."""
    spf = _smallest_prime_factors(limit)

    total = 0
    for n in range(3, limit + 1):
        roots = [n - 1]
        best = 1
        remaining = n

        while remaining > 1:
            p = spf[remaining]
            prime_power = 1
            while remaining % p == 0:
                remaining //= p
                prime_power *= p

            if prime_power == 2:
                continue

            cofactor = n // prime_power
            projector = (
                cofactor
                * _modular_inverse(cofactor % prime_power, prime_power)
                % n
            )
            delta_two = (2 * projector) % n

            delta_half = 0
            delta_half_plus_two = 0
            has_extra_two_roots = (
                prime_power % 2 == 0 and prime_power >= 8
            )
            if has_extra_two_roots:
                half = prime_power // 2
                delta_half = (half * projector) % n
                delta_half_plus_two = ((half + 2) * projector) % n

            previous_roots = list(roots)
            for root in previous_roots:
                candidate = (root + delta_two) % n
                roots.append(candidate)
                if best < candidate < n - 1:
                    best = candidate

                if has_extra_two_roots:
                    candidate = (root + delta_half) % n
                    roots.append(candidate)
                    if best < candidate < n - 1:
                        best = candidate

                    candidate = (root + delta_half_plus_two) % n
                    roots.append(candidate)
                    if best < candidate < n - 1:
                        best = candidate

        total += best

    return total


if __name__ == "__main__":
    print(solve())
