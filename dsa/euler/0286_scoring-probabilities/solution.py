"""Project Euler 286: Scoring Probabilities

Find the real constant q > 50 such that the probability of scoring exactly 20 points
out of 50 shots from distances x = 1, 2, ..., 50 is exactly 0.02, rounded to 10 decimal places.
"""

from __future__ import annotations

from decimal import Decimal, getcontext


def prob_k_points(q: Decimal, num_shots: int, target_k: int) -> Decimal:
    """Calculates the probability of scoring exactly target_k points across num_shots

    shots where shot x has success probability p_x = 1 - x / q via dynamic programming.
    """
    dp = [Decimal(0)] * (target_k + 2)
    dp[0] = Decimal(1)

    for x in range(1, num_shots + 1):
        one_minus_p = Decimal(x) / q
        p = Decimal(1) - one_minus_p
        next_dp = [Decimal(0)] * (target_k + 2)

        # Transition: miss (remain at k) or score (advance to k + 1)
        for k in range(min(x + 1, target_k + 1)):
            if dp[k] > 0:
                next_dp[k] += dp[k] * one_minus_p
                if k + 1 <= target_k:
                    next_dp[k + 1] += dp[k] * p

        dp = next_dp

    return dp[target_k]


def solve(num_shots: int = 50, target_points: int = 20, target_prob_str: str = "0.02") -> str:
    """Finds q using high-precision bisection search on the Poisson binomial distribution."""
    getcontext().prec = 40
    target_prob = Decimal(target_prob_str)

    low = Decimal(50) + Decimal("1e-12")
    high = Decimal(60)

    # 70 bisection iterations provide over 20 decimal places of accuracy:
    for _ in range(70):
        mid = (low + high) / Decimal(2)
        val = prob_k_points(mid, num_shots, target_points)
        if val > target_prob:
            low = mid
        else:
            high = mid

    ans = (low + high) / Decimal(2)
    return f"{ans:.10f}"


if __name__ == "__main__":
    print(solve())
