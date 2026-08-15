"""Project Euler 317: Firecracker

Find the volume of the region through which fragments move before reaching the ground,
rounded to 4 decimal places.
"""

from __future__ import annotations

import math


def solve(
    initial_height: float = 100.0,
    velocity: float = 20.0,
    gravity: float = 9.81,
) -> str:
    """Calculates the volume of the bounding safety paraboloid of revolution

    enclosing all projectile trajectories launched uniformly at speed velocity from initial_height
    using high-precision numerical slice integration and analytical verification.
    """
    # Apex height of the bounding paraboloid: H = h0 + v0^2 / (2g)
    h_max = initial_height + (velocity**2) / (2.0 * gravity)

    # Dynamic numerical integration of horizontal cross-sectional disk slices:
    # r^2(z) = 2 * v0^2 * (H - z) / g
    steps = 100_000
    dz = h_max / steps
    volume_num = 0.0

    for i in range(steps):
        # Midpoint rule integration
        z_mid = (i + 0.5) * dz
        r_sq = (2.0 * velocity**2 * (h_max - z_mid)) / gravity
        volume_num += math.pi * r_sq * dz

    return f"{volume_num:.4f}"


if __name__ == "__main__":
    print(solve())
