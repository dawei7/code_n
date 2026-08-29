"""Project Euler 267: Billionaire

Find the maximum probability of reaching at least £1,000,000,000 starting from £1
after 1000 coin tosses by choosing an optimal betting fraction f, rounded to 12 decimal places.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
import math


def solve(n: int = 1000, target_capital: int = 10**9) -> str:
    """Computes the maximum probability of becoming a billionaire by minimizing the required

    number of heads via golden-section search and evaluating exact binomial coefficients.
    """
    target_log = math.log(target_capital)

    def req_heads(f: float) -> float:
        num = target_log - n * math.log(1.0 - f)
        den = math.log(1.0 + 2.0 * f) - math.log(1.0 - f)
        return num / den

    # Minimize required heads H over f in (0, 1) using ternary search
    low, high = 1e-4, 1.0 - 1e-4
    for _ in range(100):
        m1 = low + (high - low) / 3.0
        m2 = high - (high - low) / 3.0
        if req_heads(m1) > req_heads(m2):
            low = m1
        else:
            high = m2

    opt_f = (low + high) / 2.0
    h_min = math.ceil(req_heads(opt_f))

    # Exact binomial tail probability
    getcontext().prec = 50
    total_favorable = sum(math.comb(n, k) for k in range(h_min, n + 1))
    prob = Decimal(total_favorable) / Decimal(1 << n)

    return f"{prob:.12f}"


if __name__ == "__main__":
    print(solve())
