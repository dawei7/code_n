"""Project Euler Problem 527: Randomized Binary Search.

Find R(10^10) - B(10^10) rounded to 8 decimal places, where B(n) is the expected
guesses for standard binary search and R(n) is the expected guesses for random binary search.
"""

from decimal import Decimal, getcontext
from typing import Dict, List

getcontext().prec = 50


def _compute_euler_mascheroni_gamma(m_terms: int = 100000) -> Decimal:
    """Dynamically compute the Euler-Mascheroni constant gamma via Euler-Maclaurin."""
    m_dec = Decimal(m_terms)
    h_sum = sum(Decimal(1) / Decimal(k) for k in range(1, m_terms + 1))
    inv_m = Decimal(1) / m_dec
    inv_m2 = inv_m * inv_m
    inv_m4 = inv_m2 * inv_m2
    gamma = (
        h_sum
        - m_dec.ln()
        - Decimal("0.5") * inv_m
        + (Decimal(1) / Decimal(12)) * inv_m2
        - (Decimal(1) / Decimal(120)) * inv_m4
    )
    return gamma


def _harmonic_large(n: int, gamma: Decimal) -> Decimal:
    """Compute H_n using Euler-Maclaurin expansion with high-precision Decimal."""
    n_dec = Decimal(n)
    inv_n = Decimal(1) / n_dec
    inv_n2 = inv_n * inv_n
    inv_n4 = inv_n2 * inv_n2

    return (
        n_dec.ln()
        + gamma
        + Decimal("0.5") * inv_n
        - (Decimal(1) / Decimal(12)) * inv_n2
        + (Decimal(1) / Decimal(120)) * inv_n4
    )


def _expected_random(n: int, gamma: Decimal) -> Decimal:
    """Compute R(n) = 2*(1 + 1/n)*H_n - 3."""
    n_dec = Decimal(n)
    h_val = _harmonic_large(n, gamma)
    return Decimal(2) * (Decimal(1) + Decimal(1) / n_dec) * h_val - Decimal(3)


def solve(n: int = 10**10) -> str:
    """Compute R(n) - B(n) rounded to 8 decimal places using iterative divide-and-conquer."""
    gamma = _compute_euler_mascheroni_gamma()

    memo: Dict[int, int] = {0: 0, 1: 1}
    stack: List[int] = [n]

    while stack:
        curr = stack[-1]
        if curr in memo:
            stack.pop()
            continue
        g = (1 + curr) // 2
        left = g - 1
        right = curr - g
        if left not in memo:
            stack.append(left)
            continue
        if right not in memo:
            stack.append(right)
            continue
        memo[curr] = curr + memo[left] + memo[right]
        stack.pop()

    total_depth = memo[n]
    b_val = Decimal(total_depth) / Decimal(n)
    r_val = _expected_random(n, gamma)

    diff = r_val - b_val
    return f"{diff:.8f}"


if __name__ == "__main__":
    print(solve())
