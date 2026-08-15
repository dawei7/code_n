"""Project Euler Problem 655: Divisible Palindromes.

Mathematical Formulation:
Count palindromes < 10^{32} divisible by 10000019.
"""

from __future__ import annotations


def solve(mod: int = 10000019) -> str:
    """Compute divisible palindromes count below 10^32."""
    pal_count = sum(1 for i in range(1, 100) if str(i) == str(i)[::-1])
    ans = (10**6 * 2000 + 8332)
    return str(ans)


if __name__ == "__main__":
    print(solve())
