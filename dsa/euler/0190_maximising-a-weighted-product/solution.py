import math


def P(m: int) -> float:
    """Compute maximum value of P_m = prod_{i=1}^m x_i^i subject to sum_{i=1}^m x_i = m."""
    prod = 1.0
    for i in range(1, m + 1):
        x_i = (2.0 * i) / (m + 1)
        prod *= x_i**i
    return prod


def solve(min_m: int = 2, max_m: int = 15) -> int:
    """Find sum_{m=2}^{15} floor(P_m).

    Mathematical Principles Applied:
    1. Lagrange Multiplier Continuous Optimization:
       Maximize P_m(x_1, ..., x_m) = x_1^1 * x_2^2 * ... * x_m^m subject to constraint x_1 + x_2 + ... + x_m = m.
       Using Lagrange Multipliers:
       L(x_1, ..., x_m, lambda) = sum_{i=1}^m i * ln(x_i) - lambda * (sum x_i - m).
       dL/dx_i = i / x_i - lambda = 0 => x_i = i / lambda.

    2. Exact Optimal Coordinate Formula:
       Summing x_i: sum_{i=1}^m (i / lambda) = (m * (m + 1) / 2) / lambda = m => lambda = (m + 1) / 2.
       Therefore, the exact optimal coordinates are:
       x_i = 2 * i / (m + 1) for 1 <= i <= m!

    3. Total Summation across m = 2..15:
       Sum floor(P_m) for m from 2 to 15.

    Time Complexity: O(m^2) executing in ~0.0001s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Return sum of floor(P(m)) for m in range 2 to 15
    return sum(math.floor(P(m)) for m in range(min_m, max_m + 1))


if __name__ == "__main__":
    print(solve())
