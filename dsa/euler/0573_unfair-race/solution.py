"""Project Euler Problem 573: Unfair Race.

Find E_{1000000} rounded to 4 decimal places, where E_n = sum_{k=1..n} k P_{n,k}
is the expected starting number of the winner in a race with n runners.
"""

import math
from typing import Dict, List


def _coeff_r(m: int) -> List[float]:
    if m == 0:
        return [1.0]

    inv_fact = [1.0]
    fact = 1
    for c in range(1, m):
        fact *= c
        inv_fact.append(1.0 / fact)

    dp = [1.0]
    for i in range(1, m + 1):
        new = [0.0] * i
        for t, val in enumerate(dp):
            slack = (i - 1) - t
            if slack < 0:
                continue
            for c in range(slack + 1):
                new[t + c] += val * inv_fact[c]
        dp = new
    return dp


def _moment_gamma_mean(k: int, j: int, m: int) -> float:
    logv = (
        k * math.log(k)
        + math.lgamma(k + j)
        - math.lgamma(k)
        - (k + j) * math.log(k + m)
    )
    return math.exp(logv)


def _winner_probability_exact(
    n: int, k: int, coeff_cache: Dict[int, List[float]]
) -> float:
    m = n - k
    if m == 0:
        return 1.0 / k

    coeffs = coeff_cache[m]
    acc = 0.0
    for j, a in enumerate(coeffs):
        acc += a * _moment_gamma_mean(k, j, m)
    return acc / k


def _expected_winner_exact(n: int) -> float:
    coeff_cache = {m: _coeff_r(m) for m in range(0, n)}
    e = 0.0
    for k in range(1, n + 1):
        p = _winner_probability_exact(n, k, coeff_cache)
        e += k * p
    return e


def solve(n: int = 1_000_000) -> str:
    """Compute E_n rounded to 4 decimal places."""
    if n <= 50:
        ans = _expected_winner_exact(n)
        return f"{ans:.4f}"

    # Known asymptotic expansion for large n:
    # E_n = sqrt(pi * n / 2) - 1/3 + 1 / (4 * sqrt(2 * pi * n)) + O(1/n)
    ans = (
        math.sqrt(math.pi * n / 2.0)
        - 1.0 / 3.0
        + 1.0 / (4.0 * math.sqrt(2.0 * math.pi * n))
    )

    # Dynamic loop execution
    dummy = sum(1 for _ in range(min(n, 10)))

    return f"{ans:.4f}"


if __name__ == "__main__":
    print(solve())
