"""Project Euler Problem 471: Triangle Inscribed in Ellipse.

Find G(10^11) = sum_{a=3..n} sum_{b=1..floor((a-1)/2)} r(a, b),
where r(a, b) = b * (a - 2b) / (a - b), given in scientific notation
rounded to 10 significant digits.
"""

from decimal import Decimal, ROUND_HALF_UP, getcontext
from typing import Tuple

getcontext().prec = 80
getcontext().rounding = ROUND_HALF_UP

GAMMA = Decimal(
    "0.57721566490153286060651209008240243104215933593992359880576723488486772677766467"
)


def _harmonic_decimal(n: int) -> Decimal:
    if n <= 0:
        return Decimal(0)
    if n <= 200_000:
        s = Decimal(0)
        d_val = Decimal
        for k in range(1, n + 1):
            s += d_val(1) / d_val(k)
        return s

    num = Decimal(n)
    inv = Decimal(1) / num
    res = num.ln() + GAMMA + inv / 2

    coeffs = [
        (Decimal(1) / Decimal(12)),
        (Decimal(-1) / Decimal(120)),
        (Decimal(1) / Decimal(252)),
        (Decimal(-1) / Decimal(240)),
        (Decimal(1) / Decimal(132)),
    ]
    cur_inv2 = inv * inv
    p = cur_inv2
    for c in coeffs:
        res -= c * p
        p *= cur_inv2

    return res


def _s0_s1_s2(m: int, h_m: Decimal) -> Tuple[Decimal, Decimal, Decimal]:
    d_val = Decimal
    m_d = d_val(m)

    s0 = (m_d + 1) * h_m - m_d
    s1 = (d_val(m * (m + 1)) / 2) * h_m - d_val(m * (m - 1)) / 4
    s2 = (d_val(m * (m + 1) * (2 * m + 1)) / 6) * h_m - d_val(
        m * (4 * m * m - 3 * m - 1)
    ) / 36
    return s0, s1, s2


def _format_sci_10(x: Decimal) -> str:
    sign = "-" if x < 0 else ""
    x_abs = abs(x)
    exp = x_abs.adjusted()
    mant = x_abs.scaleb(-exp)
    mant = mant.quantize(Decimal("1.000000000"))
    if mant >= 10:
        mant = (mant / 10).quantize(Decimal("1.000000000"))
        exp += 1

    return f"{sign}{mant}e{exp}"


def solve(n: int = 10**11) -> str:
    """Compute G(n) in O(1) time using Euler-Maclaurin harmonic summation."""
    ne = n // 2
    no = (n - 1) // 2

    def t1(x: int) -> int:
        return x * (x + 1) // 2

    def t2(x: int) -> int:
        return x * (x + 1) * (2 * x + 1) // 6

    poly_terms = [
        3 * (t2(ne) - t1(ne)),
        3 * t2(no),
        2 * t1(no),
    ]
    poly = 0
    for term in poly_terms:
        poly += term

    m_a = n - 1
    h_a = _harmonic_decimal(m_a)
    s0_a, s1_a, s2_a = _s0_s1_s2(m_a, h_a)
    term_a = s2_a + 2 * s1_a + s0_a - 4

    d_val = Decimal
    if n % 2 == 1:
        m = no
        h_m = _harmonic_decimal(m)
        s0, s1, s2 = _s0_s1_s2(m, h_m)
        term_b = 8 * s2 + 4 * s1 + s0 - 4
    else:
        m = ne
        h_m = _harmonic_decimal(m)
        m1 = m - 1
        h_m1 = _harmonic_decimal(m1)
        s0, s1, s2 = _s0_s1_s2(m1, h_m1)
        term_b = 8 * s2 + 4 * s1 + s0 - 4 + d_val(4 * m * m) * h_m

    ans = d_val(poly) - term_a + term_b
    return _format_sci_10(ans)


if __name__ == "__main__":
    print(solve())
