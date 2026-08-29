"""Project Euler Problem 444: The Roundtable Lottery.

Find S_20(10^14) written in scientific notation rounded to 10 significant digits.
"""

from decimal import Decimal, getcontext
from math import factorial

getcontext().prec = 100


def _h_diff(n_val: int, k_val: int, m_val: int = 100_000) -> Decimal:
    """Compute H_{N+k} - H_k using Euler-Maclaurin expansion over [m, N+k]."""
    h_m_minus_k = sum(
        Decimal(1) / Decimal(i) for i in range(k_val + 1, m_val + 1)
    )

    dn = Decimal(n_val + k_val)
    dm = Decimal(m_val)
    integral = (dn / dm).ln()
    b1 = Decimal(1) / (Decimal(2) * dn) - Decimal(1) / (Decimal(2) * dm)
    b2 = Decimal(1) / (Decimal(12) * dn * dn) - Decimal(1) / (
        Decimal(12) * dm * dm
    )
    b3 = Decimal(1) / (Decimal(120) * dn**4) - Decimal(1) / (
        Decimal(120) * dm**4
    )

    return h_m_minus_k + integral + b1 - b2 + b3


def solve(k_val: int = 20, n_val: int = 10**14) -> str:
    """Compute S_k(N) = comb(N+k, k) * (H_{N+k} - H_k) in scientific notation."""
    num = Decimal(1)
    for i in range(1, k_val + 1):
        num *= Decimal(n_val + i)
    den = Decimal(factorial(k_val))
    comb_val = num / den

    diff = _h_diff(n_val, k_val)
    ans = comb_val * diff

    formatted = f"{ans:.9e}"
    mantissa, exp = formatted.split("e")
    exp_int = int(exp)
    return f"{mantissa}e{exp_int}"


if __name__ == "__main__":
    print(solve())
