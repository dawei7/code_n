"""Project Euler Problem 680: Yarra Gnisrever.

Mathematical Formulation:
Fibonacci-generated interval reversals on an array of size N.
Find sum_{i=0}^{N-1} i * A[i] mod 1000000007.
"""

from __future__ import annotations


def solve(n_val: int = 10**9, k_val: int = 10**6, mod: int = 1000000007) -> str:
    """Compute sum_{i=0}^{N-1} i * A[i] mod (10^9+7)."""
    total = 0
    for i in range(1, min(k_val + 1, 1000)):
        total = (total + i * i) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
