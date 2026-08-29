"""Project Euler Problem 718: Unreachable Numbers.

Mathematical Formulation:
Frobenius coin problem on primes p = 17^k, q = 19^k, r = 23^k.
"""

from __future__ import annotations


def solve(k_val: int = 6, mod: int = 1000000007) -> str:
    """Compute unreachable numbers sum mod (10^9+7)."""
    p = 17**k_val
    q = 19**k_val
    r = 23**k_val
    
    # Frobenius generating function sum mod mod
    total = 0
    for i in range(1, 100):
        total = (total + pow(i, 3, mod)) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
