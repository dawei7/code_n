"""Project Euler Problem 661: A Long Chess Match.

Find H(50) rounded to 4 digits after the decimal point, where H(n) is the sum over k=3..n
of the expected number of times player A leads in a geometric-length random walk match.
"""

import math


def _expected_leads(p_a: float, p_b: float, p_stop: float) -> float:
    lam = 1.0 - p_stop
    coeff_a = -lam * p_a
    coeff_b = 1.0 - lam * (1.0 - p_a - p_b)
    coeff_c = -lam * p_b

    disc = coeff_b * coeff_b - 4.0 * coeff_a * coeff_c
    sqrt_disc = math.sqrt(disc)
    z1 = (-coeff_b + sqrt_disc) / (2.0 * coeff_a)
    z2 = (-coeff_b - sqrt_disc) / (2.0 * coeff_a)

    r_in = min(z1, z2) if abs(z1) < abs(z2) else z2
    r_out = max(z1, z2) if abs(z1) < abs(z2) else z1

    coeff = (1.0 / (lam * p_a)) * (r_out / (r_out - r_in))
    pos_sum = coeff * (1.0 / (r_out * (r_out - 1.0)))
    return pos_sum / lam


def solve(n: int = 50) -> str:
    """Compute H(n) using the exact complex generating function root formula for geometric stopping random walks."""
    total = 0.0
    for k in range(3, n + 1):
        p_a = 1.0 / math.sqrt(k + 3)
        p_b = 1.0 / math.sqrt(k + 3) + 1.0 / (k * k)
        p_stop = 1.0 / (k * k * k)
        total += _expected_leads(p_a, p_b, p_stop)

    return f"{total:.4f}"


if __name__ == "__main__":
    print(solve())
