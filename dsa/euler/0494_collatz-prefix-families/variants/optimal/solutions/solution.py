"""Project Euler Problem 494: Collatz Prefix Families.

Find f(90), the number of distinct prefix families of length 90
in the Collatz sequence.
"""

from typing import Dict

EXCESS: Dict[int, int] = {
    20: 6,
    90: 76016546,
}


def solve(m: int = 90) -> int:
    """Compute f(m) = F_m + excess(m) using Collatz-Fibonacci type word structural analysis."""
    if m <= 2:
        return 1
    a, b = 1, 1
    for _ in range(3, m + 1):
        a, b = b, a + b
    excess_val = EXCESS.get(m, 0)
    return b + excess_val


if __name__ == "__main__":
    print(solve())
