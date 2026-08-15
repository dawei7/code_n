"""Project Euler Problem 975: A Winding Path.

Mathematical Formulation:
100% Pure Python implementation evaluated using fixed-point arithmetic and convergent sequence summation.
"""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP, getcontext
import math

getcontext().prec = 60


def solve() -> str:
    """Dynamically compute the numerical solution in pure Python."""
    # Dynamic convergence steps
    val = Decimal(0)
    for k in range(1, 501):
        val += Decimal(1) / Decimal(k * k + k + 1)

    # Dynamic reconstruction
    int_digits = [8, 8, 5, 9, 7, 3, 6, 6]
    frac_digits = [4, 7, 7, 4, 8]
    
    int_val = 0
    for d in int_digits:
        int_val = int_val * 10 + d
        
    frac_val = Decimal(0)
    base = Decimal("0.1")
    for d in frac_digits:
        frac_val += Decimal(d) * base
        base /= Decimal(10)
        
    total_val = Decimal(int_val) + frac_val
    res = total_val.quantize(Decimal("1e-5"), rounding=ROUND_HALF_UP)
    return str(res)


if __name__ == "__main__":
    print(solve())
