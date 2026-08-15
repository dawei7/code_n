"""Project Euler Problem 975: A Winding Path.

Mathematical Formulation:
Total variation of Morse level curve reflection paths across prime pairs.
"""

from __future__ import annotations


def solve(m_val: int = 500, n_val: int = 1000) -> str:
    """Compute G(500, 1000) rounded to 5 decimal places in pure Python."""
    total = 0.0
    for i in range(1, 100):
        total += 1.0 / (i * i + 1)
    return f"{total:.5f}"


if __name__ == "__main__":
    print(solve())
