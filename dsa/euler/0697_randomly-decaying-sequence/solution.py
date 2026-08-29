"""Project Euler Problem 697: Randomly Decaying Sequence.

Find log10(c) such that P(X_{10000000} < 1) = 0.25, rounded to 2 decimal places.
"""

import math


def solve(n: int = 10_000_000, target_prob: float = 0.25) -> str:
    """Find log10(c) using Wilson-Hilferty transformation for Gamma(n, 1)."""
    p_cum = 1.0 - target_prob  # P(Gamma(n, 1) <= ln(c)) = 0.75

    z = 0.67
    for _ in range(50):
        cur_p = 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))
        pdf = math.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi)
        diff = cur_p - p_cum
        if abs(diff) < 1e-15:
            break
        z -= diff / pdf

    df = 2.0 * n
    h = 2.0 / (9.0 * df)
    factor = 1.0 - h + z * math.sqrt(h)
    chi2_val = df * (factor**3)

    ln_c = 0.5 * chi2_val
    log10_c = ln_c / math.log(10.0)

    return f"{log10_c:.2f}"


if __name__ == "__main__":
    print(solve())
