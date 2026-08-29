"""Project Euler Problem 436: Unfair Wager.

Find the probability that the second player wins in the continuous wager game,
rounded to 10 decimal places.
"""

from decimal import Decimal, getcontext

getcontext().prec = 60


def solve() -> str:
    """Compute P(y > x) = (1 + 14e - 5e^2)/4 using high-precision Taylor series expansion."""
    e_val = Decimal(0)
    term = Decimal(1)
    for k in range(1, 60):
        e_val += term
        term /= Decimal(k)

    p_val = (
        Decimal(1) + Decimal(14) * e_val - Decimal(5) * e_val * e_val
    ) / Decimal(4)
    return str(p_val.quantize(Decimal("0.0000000000")))


if __name__ == "__main__":
    print(solve())
