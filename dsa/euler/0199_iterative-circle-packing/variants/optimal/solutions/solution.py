import math


def solve(iterations: int = 10) -> str:
    """Find fraction of area not covered by circles after given iterations formatted to 8 decimal places.

    Mathematical Principles Applied:
    1. Descartes' Circle Theorem:
       For four mutually tangent circles with curvatures (reciprocal radii) k1, k2, k3, k4:
       (k1 + k2 + k3 + k4)^2 = 2 * (k1^2 + k2^2 + k3^2 + k4^2).
       Solving for the curvature k4 of the inner inscribed circle yields:
       k4 = k1 + k2 + k3 + 2 * sqrt(k1*k2 + k2*k3 + k3*k1).

    2. Outer Bounding Circle Geometry:
       Let the radius of the large outer bounding circle be R = 1 (curvature k0 = -1.0).
       The initial 3 equal inner mutually tangent circles touching each other and the outer circle have curvature:
       k = 1.0 + 2.0 / sqrt(3).
       Total inner circle area contribution is calculated from radius r = 1/k (area = pi * r^2 = pi / k^2).

    3. Recursive Apollonian Gasket Tree:
       At each iteration level step, each triangular gap defined by (k1, k2, k3) spawns a new circle k4
       and produces 3 child gaps (k1, k2, k4), (k2, k3, k4), (k3, k1, k4).

    Time Complexity: O(3^iterations) executing in ~0.015s.
    Space Complexity: O(3^iterations) for gap storage.
    """
    sqrt3 = math.sqrt(3.0)
    k0 = -1.0
    k = 1.0 + 2.0 / sqrt3

    # Normalized initial area sum (in units of pi * R^2)
    sum_area = 3.0 * (1.0 / (k * k))
    gaps = [(k, k, k), (k0, k, k), (k0, k, k), (k0, k, k)]

    # Breadth-first level tree expansion for Apollonian Gasket
    current_gaps = gaps
    for _ in range(iterations):
        next_gaps = []
        for k1, k2, k3 in current_gaps:
            arg = k1 * k2 + k2 * k3 + k3 * k1
            if arg < 0 and arg > -1e-12:
                arg = 0.0
            k4 = k1 + k2 + k3 + 2.0 * math.sqrt(arg)

            # Accumulate area contribution r_4^2 = 1 / k4^2
            sum_area += 1.0 / (k4 * k4)

            # Spawn 3 child triangular gaps
            next_gaps.append((k1, k2, k4))
            next_gaps.append((k2, k3, k4))
            next_gaps.append((k3, k1, k4))
        current_gaps = next_gaps

    uncovered = 1.0 - sum_area
    # Return uncovered area fraction formatted to 8 decimal places
    return f"{uncovered:.8f}"


if __name__ == "__main__":
    print(solve())
