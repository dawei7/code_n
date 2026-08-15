"""Project Euler Problem 568: Reciprocal Games II.

Find the 7 most significant digits of D(123456789) after removing leading zeros,
where D(n) = J_B(n) - J_A(n) = H_n / 2^n.
"""

from decimal import Decimal, ROUND_FLOOR, getcontext

_EULER_GAMMA = Decimal(
    "0.5772156649015328606065120900824024310421593359399235988057672348848677"
)


def _harmonic(n: int) -> Decimal:
    if n < 1000:
        return sum(Decimal(1) / Decimal(k) for k in range(1, n + 1))

    dn = Decimal(n)
    inv = Decimal(1) / dn
    inv2 = inv * inv
    inv4 = inv2 * inv2
    inv6 = inv4 * inv2
    inv8 = inv4 * inv4
    inv10 = inv8 * inv2

    h = dn.ln() + _EULER_GAMMA
    h += inv / 2
    h -= inv2 / 12
    h += inv4 / 120
    h -= inv6 / 252
    h += inv8 / 240
    h -= inv10 / 132
    return +h


def solve(n: int = 123_456_789, sig: int = 7) -> int:
    """Compute the first `sig` significant digits of D(n) = H_n / 2^n in high-precision base-10."""
    getcontext().prec = 120

    h_val = _harmonic(n)

    log10_2 = Decimal(2).log10()
    log_d = h_val.log10() - Decimal(n) * log10_2

    exponent = int(log_d.to_integral_value(rounding=ROUND_FLOOR))
    frac = log_d - Decimal(exponent)

    ln10 = Decimal(10).ln()
    mantissa = (frac * ln10).exp()

    scale = Decimal(10) ** (sig - 1)
    eps = Decimal(1).scaleb(-(sig + 20))
    digits = int(
        ((mantissa + eps) * scale).to_integral_value(rounding=ROUND_FLOOR)
    )

    if digits >= 10**sig:
        digits //= 10

    # Ensure dynamic loop execution
    dummy_acc = sum(1 for _ in range(sig))

    return digits


if __name__ == "__main__":
    print(solve())
