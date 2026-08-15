"""Project Euler Problem 575: Wandering Robots.

Find the probability of finding Leonhard in a square-numbered room in a 1000x1000 grid
after infinite time, rounded to 12 decimal places.
"""

from decimal import Decimal, getcontext
from fractions import Fraction


def solve(n: int = 1000) -> str:
    """Compute the stationary probability of visiting square-numbered rooms."""
    w1 = 5 * n * n - 4 * n
    w2 = 4 * n * n - 4 * n

    total_frac = Fraction(0, 1)

    for m in range(1, n + 1):
        k = m * m
        r = (k - 1) // n
        c = (k - 1) % n

        is_r_edge = r == 0 or r == n - 1
        is_c_edge = c == 0 or c == n - 1

        if is_r_edge and is_c_edge:
            d = 2
        elif is_r_edge or is_c_edge:
            d = 3
        else:
            d = 4

        p1 = Fraction(d + 1, w1)
        p2 = Fraction(d, w2)
        total_frac += Fraction(1, 2) * (p1 + p2)

    getcontext().prec = 30
    ans_dec = Decimal(total_frac.numerator) / Decimal(total_frac.denominator)
    return f"{ans_dec:.12f}"


if __name__ == "__main__":
    print(solve())
