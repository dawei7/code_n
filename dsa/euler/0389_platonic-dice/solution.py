"""Project Euler Problem 389: Platonic Dice.

Find the variance of I (the sum of iterated rolls of 4, 6, 8, 12, 20-sided Platonic dice),
rounded to 4 decimal places.
"""

from fractions import Fraction
from typing import List


def solve(dice_faces: List[int] = None) -> str:
    """Compute exact variance of iterated dice rolls using the Law of Total Variance."""
    if dice_faces is None:
        dice_faces = [4, 6, 8, 12, 20]

    # Initial state: 1 throw of 0-sided constant (or start before first die)
    mean = Fraction(1, 1)
    variance = Fraction(0, 1)

    for sides in dice_faces:
        mu = Fraction(sides + 1, 2)
        var = Fraction(sides * sides - 1, 12)

        # Law of Total Expectation & Law of Total Variance (Eve's Law):
        # E[S_N] = E[N] * mu
        # Var(S_N) = E[N] * Var(X) + Var(N) * (mu^2)
        new_mean = mean * mu
        new_variance = mean * var + variance * (mu * mu)

        mean = new_mean
        variance = new_variance

    return f"{float(variance):.4f}"


if __name__ == "__main__":
    print(solve())
