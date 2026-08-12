from decimal import Decimal, getcontext
import math


def solve(tosses: int = 1000, target: float = 10**9) -> str:
    """Find the chance of becoming a billionaire after 1000 coin tosses with optimal bet fraction f, rounded to 12 decimal places.
    
    Time Complexity: O(tosses)
    Space Complexity: O(1)
    """
    getcontext().prec = 50

    # 1. Find minimum heads H_min such that max_f C(H, f) >= 10^9:
    h_min = None
    for h in range(tosses + 1):
        f = (3 * h - tosses) / (2.0 * tosses)
        if 0 < f < 1:
            cap = ((1 + 2 * f) ** h) * ((1 - f) ** (tosses - h))
            if cap >= target:
                h_min = h
                break

    # 2. Cumulative binomial probability sum_{k=h_min}^1000 C(1000, k) / 2^1000:
    total_ways = sum(math.comb(tosses, k) for k in range(h_min, tosses + 1))
    prob = Decimal(total_ways) / (Decimal(2) ** tosses)
    return f"{prob:.12f}"
