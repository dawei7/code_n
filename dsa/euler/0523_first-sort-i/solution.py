"""Project Euler Problem 523: First Sort I.

Find E(30) rounded to two decimal places, where E(n) is the expected number
of moves to sort a random permutation of {1, 2, ..., n} using First Sort.
"""

from fractions import Fraction


def solve(n: int = 30) -> str:
    """Compute E(n) using exact rational expectation formula E(n) = sum_{k=2..n} (2^(k-1) - 1)/k."""
    total = Fraction(0, 1)
    for k in range(2, n + 1):
        total += Fraction(pow(2, k - 1) - 1, k)

    ans = float(total)
    return f"{ans:.2f}"


if __name__ == "__main__":
    print(solve())
