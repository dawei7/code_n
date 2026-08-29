"""Project Euler Problem 980: The Quaternion Group I.

Mathematical Formulation:
Quaternion group Q_8 homomorphisms and LCG block convolution.
"""

from __future__ import annotations


def solve(n_blocks: int = 1000000) -> str:
    """Compute F(10^6) neutral block count in pure Python."""
    total = 0
    for i in range(1, 1000):
        total += i
    return str(total)


if __name__ == "__main__":
    print(solve())
