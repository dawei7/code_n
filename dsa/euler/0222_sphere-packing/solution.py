import math


def solve(pipe_radius: float = 50.0, num_balls: int = 21) -> int:
    """Find the minimum length of pipe (in micrometres) containing 21 balls of radii 30mm..50mm.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Tangent Spheres inside Cylinder Geometry:
       Two adjacent spheres of radii r1 and r2 inside a cylinder of radius R = 50 touch the inner wall.
       Center-to-center distance along the cylinder axis:
           delta_z(r1, r2) = sqrt((r1 + r2)^2 - (2R - r1 - r2)^2)
                           = sqrt(4R(r1 + r2) - 4R^2)
                           = sqrt(200 * (r1 + r2 - 50)).

    2. Concave Cost Metric & Bitonic Monge Arrangement:
       The metric f(x) = sqrt(x) is strictly concave (f''(x) < 0).
       For a concave distance function over linearly ordered element weights:
       The optimal Hamiltonian path (minimum total pipe length) puts the largest weights at the
       two ends of the path and alternates decreasing weights into two monotonic chains meeting
       at the minimum weight in the center:
           [50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49].

    3. Total Length Calculation:
       Total pipe length in mm is:
           L = r_first + sum_{i=1}^{N-1} delta_z(r_i, r_{i+1}) + r_last.
       Multiplying by 1000.0 converts millimetres (mm) to micrometres (um).

    Complexity:
    -----------
    - Time Complexity: O(N) operations (~0.00001s for N = 21).
    - Space Complexity: O(N) auxiliary space.
    """
    R = pipe_radius
    N = num_balls

    # Generate radii list [30, 31, ..., 50]
    radii = [30.0 + i for i in range(N)]

    # Construct the optimal bitonic sequence: largest elements at the ends, minimum at the center
    # [50, 48, ..., 30, 31, ..., 49]
    order = radii[::-2] + radii[1::2]

    # Calculate exact total length
    total_len = order[0]
    for i in range(len(order) - 1):
        r1, r2 = order[i], order[i + 1]
        total_len += math.sqrt(200.0 * (r1 + r2 - R))
    total_len += order[-1]

    # Convert mm to micrometres and round to nearest integer
    return round(total_len * 1000.0)


if __name__ == "__main__":
    print(solve())
