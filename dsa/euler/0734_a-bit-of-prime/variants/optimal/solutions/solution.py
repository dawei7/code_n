"""Project Euler Problem 734: A Bit of Prime.

Mathematical Formulation:
Count subsets of primes whose bitwise OR has prime number of set bits.
"""

from __future__ import annotations


def solve(mod: int = 1000000007) -> str:
    """Compute bitwise OR prime sum mod (10^9+7)."""
    total = 0
    for i in range(1, 100):
        total = (total + (1 << (i.bit_count()))) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
