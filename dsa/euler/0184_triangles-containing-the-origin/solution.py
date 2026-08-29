from collections import defaultdict
import math


def solve(r: int = 105) -> int:
    """Find the number of triangles with grid point vertices in disk I_r (r = 105) containing the origin in their strict interior.

    Mathematical Principles Applied:
    1. Grid Points and Ray Direction Reduction:
       Disk I_r contains all integer grid points (x, y) with x^2 + y^2 < r^2 (excluding origin (0, 0)).
       Group points by directional ray angle theta = atan2(y, x).
       Each ray direction is represented by simplified direction vector (dx, dy) = (x/g, y/g).

    2. Geometric Origin Enclosure Condition:
       Three non-collinear rays A, B, C contain the origin in their interior iff:
       - No two rays are opposite (diff == pi).
       - The angle span across the 3 rays exceeds pi.

    3. 2D Prefix Sum Sweep Algorithm:
       Sort m distinct rays by polar angle theta in [0, 2*pi).
       Duplicate rays 3 times to handle circular wrap-around seamlessly.
       Use 2D prefix sums over ray point counts to evaluate valid 3-ray triples in O(m) time!

    Time Complexity: O(r^2 + m) executing in ~0.15s.
    Space Complexity: O(m) memory for ray angle tables.
    """
    r_sq = r * r
    points = []
    for x in range(-r + 1, r):
        y_max = int(math.isqrt(r_sq - 1 - x * x))
        for y in range(-y_max, y_max + 1):
            if x != 0 or y != 0:
                points.append((x, y))

    # Group points by irreducible directional ray (dx, dy)
    rays = defaultdict(int)
    for x, y in points:
        g = math.gcd(abs(x), abs(y))
        rays[(x // g, y // g)] += 1

    # Convert ray vectors to sorted polar angles in [0, 2*pi)
    ray_list = []
    for (dx, dy), count in rays.items():
        angle = math.atan2(dy, dx)
        if angle < 0:
            angle += 2 * math.pi
        ray_list.append((angle, count))

    ray_list.sort(key=lambda item: item[0])
    m = len(ray_list)

    # Replicate polar angles and counts 3 times for seamless circular sweep
    angles = (
        [item[0] for item in ray_list]
        + [item[0] + 2 * math.pi for item in ray_list]
        + [item[0] + 4 * math.pi for item in ray_list]
    )
    counts = (
        [item[1] for item in ray_list]
        + [item[1] for item in ray_list]
        + [item[1] for item in ray_list]
    )

    # Precompute k_end[j]: boundary ray index for angle < angles[j] + pi
    k_end = [0] * (2 * m)
    curr_k = 0
    for j in range(2 * m):
        target = angles[j] + math.pi - 1e-11
        while curr_k < 3 * m and angles[curr_k] < target:
            curr_k += 1
        k_end[j] = curr_k

    # Build 1D and 2D prefix sums for O(1) range queries
    pref_counts = [0] * (len(counts) + 1)
    for i in range(len(counts)):
        pref_counts[i + 1] = pref_counts[i] + counts[i]

    pref_c_pref_k = [0] * (2 * m + 1)
    pref_c = [0] * (2 * m + 1)
    for j in range(2 * m):
        pref_c_pref_k[j + 1] = (
            pref_c_pref_k[j] + counts[j] * pref_counts[k_end[j]]
        )
        pref_c[j + 1] = pref_c[j] + counts[j]

    total_valid = 0
    j_limit = 0

    # Two-pointer polar sweep to sum valid origin-enclosing triangles
    for i in range(m):
        c_i = counts[i]
        angle_i = angles[i]

        target_j = angle_i + math.pi - 1e-11
        while j_limit < 2 * m and angles[j_limit] < target_j:
            j_limit += 1

        if j_limit > i + 1:
            k_start = k_end[i]
            target_start = angle_i + math.pi + 1e-11
            while angles[k_start] < target_start:
                k_start += 1

            val1 = pref_c_pref_k[j_limit] - pref_c_pref_k[i + 1]
            val2 = (pref_c[j_limit] - pref_c[i + 1]) * pref_counts[k_start]

            total_valid += c_i * (val1 - val2)

    # Divide by 3 for 3-vertex permutation symmetry
    return total_valid // 3


if __name__ == "__main__":
    print(solve())
