"""Optimal solution for randomized_06: Estimating Pi via Monte Carlo.

Estimate the value of pi using the Monte Carlo
"""


def solve(n, seed_value):
    """Estimate pi via Monte Carlo: count points (x, y) in
    [0, 1]^2 with x^2 + y^2 <= 1, return 4 * (count / n)."""
    import random
    rng = random.Random(seed_value)
    inside = 0
    for _ in range(n):
        x = rng.random()
        y = rng.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return 4.0 * inside / n
