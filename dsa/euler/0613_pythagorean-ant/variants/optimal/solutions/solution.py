"""Project Euler Problem 613: Pythagorean Ant.

Find the probability that a random ant on a 30-40-50 right triangle exits along its hypotenuse,
rounded to 10 decimal places.
"""

import math


def solve(a: float = 30.0, b: float = 40.0, c: float = 50.0) -> str:
    """Compute the exact exit probability across the hypotenuse using the analytic double integral closed form."""
    terms = [a * a * math.log(c / a), b * b * math.log(c / b)]
    numerator = 0.0
    for t in terms:
        numerator += t

    prob = 0.5 - numerator / (2.0 * math.pi * a * b)
    return f"{prob:.10f}"


if __name__ == "__main__":
    print(solve())
