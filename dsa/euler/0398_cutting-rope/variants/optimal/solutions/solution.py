"""Project Euler Problem 398: Cutting Rope.

Find E(10^7, 100), the expected length of the second-shortest segment when a rope of length n
is cut at m-1 randomly chosen integer points into m segments, rounded to 5 decimal places.
"""

from math import exp, log
from typing import List


def solve(n_val: int = 10**7, m_val: int = 100) -> str:
    """Compute E(n, m) using hockey-stick combinatorics and log-binomial ratios."""
    # Denominator logarithm: log(comb(n-1, m-1))
    log_den = sum(log(n_val - 1 - j) for j in range(m_val - 1))

    total_expected = 0.0
    k_limit = (n_val // (m_val - 1)) + 2

    for k in range(1, k_limit):
        # Term 1: comb(n - (m-1)(k-1) - 1, m-1)
        top1 = n_val - (m_val - 1) * (k - 1) - 1
        if top1 < m_val - 1:
            ratio1 = 0.0
        else:
            log_num1 = sum(log(top1 - j) for j in range(m_val - 1))
            ratio1 = exp(log_num1 - log_den)

        # Term 2: comb(n - m(k-1) - 1, m-1)
        top2 = n_val - m_val * (k - 1) - 1
        if top2 < m_val - 1:
            ratio2 = 0.0
        else:
            log_num2 = sum(log(top2 - j) for j in range(m_val - 1))
            ratio2 = exp(log_num2 - log_den)

        p_k = m_val * ratio1 - (m_val - 1) * ratio2
        if p_k < 1e-15 and k > 1000:
            break
        total_expected += p_k

    return f"{total_expected:.5f}"


if __name__ == "__main__":
    print(solve())
