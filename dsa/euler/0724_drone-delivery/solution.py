"""Project Euler Problem 724: Drone Delivery.

Find E(10^8) rounded to the nearest integer, where E(n) is the expected distance
in centimetres from the depot that supply packages land.
"""

from decimal import Decimal, getcontext
import math

_EULER_GAMMA = 0.5772156649015328606065120900824024310421


def solve(n: int = 100_000_000) -> int:
    """Compute E(n) = (n/2) * (H_n^2 + H_n^(2)) using exact Euler-Maclaurin expansion."""
    if n <= 1000:
        h = sum(1.0 / k for k in range(1, n + 1))
        h2 = sum(1.0 / (k * k) for k in range(1, n + 1))
        val = 0.5 * n * (h * h + h2)
        return int(round(val))

    getcontext().prec = 50
    d_n = Decimal(n)
    inv = Decimal(1) / d_n
    inv2 = inv * inv
    inv4 = inv2 * inv2

    # High-precision H_n and H_n^(2)
    gamma = Decimal("0.57721566490153286060651209008240243104215933593992")
    pi = Decimal(
        "3.141592653589793238462643383279502884197169399375105820974944"
    )

    ln_n = d_n.ln()
    h = (
        ln_n
        + gamma
        + Decimal("0.5") * inv
        - (Decimal(1) / Decimal(12)) * inv2
        + (Decimal(1) / Decimal(120)) * inv4
    )
    h2 = (
        (pi * pi) / Decimal(6)
        - inv
        + Decimal("0.5") * inv2
        - (Decimal(1) / Decimal(6)) * (inv2 * inv)
    )

    exp_val = Decimal("0.5") * d_n * (h * h + h2)
    ans = int(exp_val.quantize(Decimal("1")))
    return ans


if __name__ == "__main__":
    print(solve())
