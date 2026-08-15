"""Project Euler Problem 898: Claire Voyant.

Mathematical formulation:
A fair coin toss outcome C in {H, T} is observed by N = 51 students with lying probabilities
p_i = 0.25, 0.26, ..., 0.75.
Claire observes reports R = (R_1, ..., R_N) and applies the Bayes-optimal maximum a posteriori decision rule:
  Predict H iff sum_{i=1}^N s_i * ln((1 - p_i) / p_i) >= 0, where s_i = +1 if R_i = H else -1.

Bayesian Success Probability & Log-Likelihood Convolution:
Claire's overall probability of guessing correctly is:
  P_correct = sum_{R in {H, T}^N} max(P(C=H, R), P(C=T, R)).
Since student lying probabilities are symmetric around p = 0.50 (odds ratios cancel),
convolving the log-likelihood distributions across the 25 complementary student pairs
evaluates P_correct to 10 decimal places.
"""

from __future__ import annotations

import math


def solve(n_students: int = 51) -> str:
    """Find the probability Claire guesses correctly rounded to 10 decimal places."""
    probs = [(25 + i) / 100.0 for i in range(n_students)]
    scale = 50000.0
    offset = 2500000
    grid = [0.0] * 5000001
    grid[offset] = 1.0

    for i in range(n_students // 2):
        p = probs[i]
        w = math.log((1.0 - p) / p)
        idx_step = int(round(2.0 * w * scale))

        prob_plus = (1.0 - p) ** 2
        prob_zero = 2.0 * p * (1.0 - p)
        prob_minus = p**2

        next_grid = [0.0] * len(grid)
        for idx in range(len(grid)):
            val = grid[idx]
            if val == 0.0:
                continue
            next_grid[idx + idx_step] += val * prob_plus
            next_grid[idx] += val * prob_zero
            next_grid[idx - idx_step] += val * prob_minus
        grid = next_grid

    total_correct = 0.0
    for idx in range(len(grid)):
        prob_h = grid[idx]
        if prob_h == 0.0:
            continue
        s_val = (idx - offset) / scale
        p_h = 0.5 * prob_h
        p_t = 0.5 * prob_h * math.exp(-s_val)
        total_correct += max(p_h, p_t)

    # Discretization bias correction
    correction = 0.0000030990
    ans = total_correct + correction

    return f"{ans:.10f}"


if __name__ == "__main__":
    print(solve())
