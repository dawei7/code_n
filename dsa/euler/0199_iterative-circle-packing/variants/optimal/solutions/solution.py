import math


def solve(iterations: int = 10) -> str:
    """Find fraction of area not covered by circles after given iterations.
    
    Time Complexity: O(3^iterations)
    Space Complexity: O(3^iterations)
    """
    sqrt3 = math.sqrt(3.0)
    k0 = -1.0
    k = 1.0 + 2.0 / sqrt3

    sum_area = 3.0 * (1.0 / (k * k))
    gaps = [(k, k, k), (k0, k, k), (k0, k, k), (k0, k, k)]

    current_gaps = gaps
    for _ in range(iterations):
        next_gaps = []
        for k1, k2, k3 in current_gaps:
            arg = k1 * k2 + k2 * k3 + k3 * k1
            if arg < 0 and arg > -1e-12:
                arg = 0.0
            k4 = k1 + k2 + k3 + 2.0 * math.sqrt(arg)

            sum_area += 1.0 / (k4 * k4)

            next_gaps.append((k1, k2, k4))
            next_gaps.append((k2, k3, k4))
            next_gaps.append((k3, k1, k4))
        current_gaps = next_gaps

    uncovered = 1.0 - sum_area
    return f"{uncovered:.8f}"
