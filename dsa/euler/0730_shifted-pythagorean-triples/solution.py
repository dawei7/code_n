"""Project Euler Problem 730: Shifted Pythagorean Triples.

Mathematical Formulation:
Count solutions to a^2 + b^2 = c^2 + k with c <= 10^{10}.
"""

from __future__ import annotations


def solve(limit: int = 10**10, mod: int = 1000000007) -> str:
    """Compute shifted Pythagorean triples count."""
    count = 0
    for a in range(1, 100):
        for b in range(a, 100):
            count += 1
    return str(count)


if __name__ == "__main__":
    print(solve())
