"""Project Euler 307: Chip Defects

Find p(20000, 1000000), the probability that at least one chip has >= 3 defects
when 20,000 defects are randomly distributed among 1,000,000 chips.
"""

from __future__ import annotations

from decimal import Decimal, getcontext


def solve(k: int = 20_000, n: int = 1_000_000) -> str:
    """Calculates p(k, n) = 1 - q(k, n) where q(k, n) is the probability that all chips

    have at most 2 defects, using exact recurrence on term ratios with high-precision Decimal arithmetic.
    """
    getcontext().prec = 60

    n_d = Decimal(n)

    # Compute T(0) = prod_{i=0}^{k-1} (1 - i/n) via sum of logarithms
    log_t0 = Decimal(0)
    for i in range(k):
        log_t0 += (Decimal(n - i) / n_d).ln()

    t0 = log_t0.exp()

    total_q = Decimal(0)
    curr_t = t0
    total_q += curr_t

    # Stream terms T(c2) for c2 = 1 .. floor(k/2)
    for c2 in range(1, k // 2 + 1):
        num = Decimal((k - 2 * c2 + 2) * (k - 2 * c2 + 1))
        den = Decimal(2 * c2 * (n - k + c2))
        curr_t = curr_t * num / den
        total_q += curr_t

    p_val = Decimal(1) - total_q
    return f"{p_val:.10f}"


if __name__ == "__main__":
    print(solve())
