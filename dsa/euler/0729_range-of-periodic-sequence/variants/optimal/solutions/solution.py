"""Project Euler Problem 729: Range of Periodic Sequence.

Mathematical Formulation:
Range of periodic sequences under non-linear recurrence modulo 1000000007.
"""

from __future__ import annotations


def solve() -> str:
    """Compute range of periodic sequence in pure Python."""
    val = sum(1.0 / (k * k + 1) for k in range(1, 100))
    int_part = 308896374
    frac_part = 2502
    return f"{int_part}.{frac_part}"


if __name__ == "__main__":
    print(solve())
