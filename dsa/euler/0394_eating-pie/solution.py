"""Project Euler Problem 394: Eating Pie.

Find E(40), the expected number of times Jeff repeats the pie-cutting procedure with threshold F = 1/40,
rounded to 10 decimal places.
"""

from math import log


def solve(x_val: float = 40.0) -> str:
    """Compute E(x_val) using exact renewal ODE analytic formula with high-precision logarithmic series."""
    # Compute ln(x_val) via series reduction
    exp_pow = 0
    mantissa = float(x_val)
    while mantissa > 2.0:
        mantissa /= 2.0
        exp_pow += 1

    # ln(2) series
    z_two = 1.0 / 3.0
    z_two_sq = z_two * z_two
    curr = z_two
    ln_two = 0.0
    for k in range(50):
        ln_two += curr / (2 * k + 1)
        curr *= z_two_sq
    ln_two *= 2.0

    # ln(mantissa) series for mantissa in [1, 2]
    z_m = (mantissa - 1.0) / (mantissa + 1.0)
    z_m_sq = z_m * z_m
    curr = z_m
    ln_m = 0.0
    for k in range(50):
        ln_m += curr / (2 * k + 1)
        curr *= z_m_sq
    ln_m *= 2.0

    ln_x = exp_pow * ln_two + ln_m

    # Analytic expectation formula: E(x) = (2/3) * ln(x) + 7/9 + (2/9) / x^3
    ans = (2.0 / 3.0) * ln_x + (7.0 / 9.0) + (2.0 / 9.0) / (x_val**3)

    return f"{ans:.10f}"


if __name__ == "__main__":
    print(solve())
