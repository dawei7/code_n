"""Project Euler Problem 431: Square Space Silo.

Determine the values of x for all possible square space wastage options V(x) = k^2,
and calculate sum(x) correct to 9 decimal places.
"""

from math import ceil, cos, floor, pi, radians, sin, sqrt, tan
from typing import List


def _volume_wasted(x: float, radius: float = 6.0, alpha_deg: float = 40.0) -> float:
    """Compute the wasted volume V(x) inside the cylinder above the repose cone."""
    tan_alpha = tan(radians(alpha_deg))
    num_steps = 10000
    d_theta = pi / num_steps
    accum = 0.0

    r2 = radius * radius
    for i in range(num_steps + 1):
        theta = i * d_theta
        s_th = sin(theta)
        c_th = cos(theta)
        r_theta = sqrt(r2 - (x * s_th) ** 2) - x * c_th
        term = (r_theta**3) / 3.0
        weight = (
            1.0
            if (i == 0 or i == num_steps)
            else (4.0 if (i & 1) == 1 else 2.0)
        )
        accum += weight * term

    return 2.0 * tan_alpha * accum * (d_theta / 3.0)


def _find_x_for_target_volume(
    target_v: float, radius: float = 6.0, alpha_deg: float = 40.0
) -> float:
    """Find root x in [0, radius) such that V(x) = target_v using high-precision bisection."""
    low, high = 0.0, radius
    for _ in range(60):
        mid = (low + high) / 2.0
        if _volume_wasted(mid, radius, alpha_deg) < target_v:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0


def solve(radius: float = 6.0, alpha_deg: float = 40.0) -> str:
    """Compute sum of all valid x values where V(x) is a perfect square, rounded to 9 decimal places."""
    v_min = _volume_wasted(0.0, radius, alpha_deg)
    v_max = _volume_wasted(radius - 1e-6, radius, alpha_deg)

    k_start = ceil(sqrt(v_min))
    k_end = floor(sqrt(v_max))

    all_x: List[float] = []
    for k in range(k_start, k_end + 1):
        target_v = float(k * k)
        x_val = _find_x_for_target_volume(target_v, radius, alpha_deg)
        all_x.append(x_val)

    total_sum = sum(all_x)
    return f"{total_sum:.9f}"


if __name__ == "__main__":
    print(solve())
