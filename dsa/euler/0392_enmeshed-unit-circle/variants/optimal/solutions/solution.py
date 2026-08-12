import math


def solve(n: int = 400, decimals: int = 10) -> str:
    """Find the min red cell area overlapping unit circle for N gridlines.

    Time Complexity: O(N * BSearch_Steps) via Shooting Method Recurrence Optimization
    Space Complexity: O(N)
    """
    M = n // 2

    def simulate(theta1: float) -> tuple[float, list[float]]:
        theta = [0.0] * (M + 2)
        theta[0] = 0.0
        theta[1] = theta1

        sin2 = 2.0 * math.sin(theta1) - math.tan(theta1 / 2.0)
        if sin2 >= 1.0 or sin2 <= math.sin(theta1):
            return 2.0, theta
        theta[2] = math.asin(sin2)

        for i in range(2, M + 1):
            cot_i = math.cos(theta[i]) / math.sin(theta[i])
            diff = math.cos(theta[i - 1]) - math.cos(theta[i])
            sin_next = math.sin(theta[i]) + cot_i * diff
            if sin_next >= 1.0:
                return 2.0, theta
            theta[i + 1] = math.asin(sin_next)

        return theta[M + 1], theta

    low = 0.0
    high = math.pi / 2.0

    best_theta: list[float] = []
    for _ in range(500):
        mid = (low + high) / 2.0
        res, t_arr = simulate(mid)
        if res >= 2.0 or res > math.pi / 2.0:
            high = mid
        else:
            best_theta = t_arr
            low = mid

    area_1st = math.sin(best_theta[1]) * 1.0
    for i in range(1, M + 1):
        dx = math.sin(best_theta[i + 1]) - math.sin(best_theta[i])
        height = math.cos(best_theta[i])
        area_1st += dx * height

    area = 4.0 * area_1st
    return f"{area:.{decimals}f}"
