"""Project Euler Problem 430: Range Flips.

Find E(10^10, 4000), the expected number of disks showing their white side after 4000 turns,
rounded to 2 decimal places.
"""

from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 60


def solve(n_val: int = 10**10, m_val: int = 4000) -> str:
    """Compute E(n_val, m_val) using asymptotic integral expansion of flip probability parity."""
    nd = Decimal(n_val)
    md = Decimal(m_val)

    if n_val <= 10000:
        n2 = Decimal(n_val * n_val)
        total = Decimal(0)
        for i in range(1, n_val + 1):
            p = Decimal(1) - (Decimal((i - 1) ** 2 + (n_val - i) ** 2)) / n2
            r = Decimal(1) - Decimal(2) * p
            total += Decimal("0.5") * (Decimal(1) + (r**m_val))
        return format(
            total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "f"
        )

    # Large N asymptotic expansion:
    # E(N, M) = N/2 + 1/2 * [ N/(2M+1) - N*M*c/(2M-1) ] where c = (2N-1)/N^2
    terms = [
        nd / 2,
        nd / (2 * (2 * md + 1)),
        -(md * (2 * nd - 1)) / (2 * nd * (2 * md - 1)),
    ]
    expected = Decimal(0)
    for term in terms:
        expected += term

    ans = expected.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return format(ans, "f")


if __name__ == "__main__":
    print(solve())
