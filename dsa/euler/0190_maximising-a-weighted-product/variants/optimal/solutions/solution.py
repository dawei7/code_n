import math


def P(m: int) -> float:
    """Compute maximum value of P_m = prod_{i=1}^m x_i^i subject to sum x_i = m."""
    prod = 1.0
    for i in range(1, m + 1):
        x_i = (2.0 * i) / (m + 1)
        prod *= (x_i**i)
    return prod


def solve(min_m: int = 2, max_m: int = 15) -> int:
    """Find sum_{m=2}^{15} floor(P_m).
    
    Time Complexity: O(m^2)
    Space Complexity: O(1)
    """
    return sum(math.floor(P(m)) for m in range(min_m, max_m + 1))
