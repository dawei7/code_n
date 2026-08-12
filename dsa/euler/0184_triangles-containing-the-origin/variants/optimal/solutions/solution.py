from collections import defaultdict
import math


def solve(r: int = 105) -> int:
    """Find number of triangles with vertices in I_r containing origin in their interior.
    
    Time Complexity: O(r^2 + m) where m is number of distinct rays (m ~ pi * r^2)
    Space Complexity: O(m)
    """
    r_sq = r * r
    points = []
    for x in range(-r + 1, r):
        y_max = int(math.isqrt(r_sq - 1 - x * x))
        for y in range(-y_max, y_max + 1):
            if x != 0 or y != 0:
                points.append((x, y))

    rays = defaultdict(int)
    for x, y in points:
        g = math.gcd(abs(x), abs(y))
        rays[(x // g, y // g)] += 1

    ray_list = []
    for (dx, dy), count in rays.items():
        angle = math.atan2(dy, dx)
        if angle < 0:
            angle += 2 * math.pi
        ray_list.append((angle, count))

    ray_list.sort(key=lambda item: item[0])
    m = len(ray_list)

    angles = [item[0] for item in ray_list] + [item[0] + 2 * math.pi for item in ray_list] + [item[0] + 4 * math.pi for item in ray_list]
    counts = [item[1] for item in ray_list] + [item[1] for item in ray_list] + [item[1] for item in ray_list]

    k_end = [0] * (2 * m)
    curr_k = 0
    for j in range(2 * m):
        target = angles[j] + math.pi - 1e-11
        while curr_k < 3 * m and angles[curr_k] < target:
            curr_k += 1
        k_end[j] = curr_k

    pref_counts = [0] * (len(counts) + 1)
    for i in range(len(counts)):
        pref_counts[i + 1] = pref_counts[i] + counts[i]

    pref_c_pref_k = [0] * (2 * m + 1)
    pref_c = [0] * (2 * m + 1)
    for j in range(2 * m):
        pref_c_pref_k[j + 1] = pref_c_pref_k[j] + counts[j] * pref_counts[k_end[j]]
        pref_c[j + 1] = pref_c[j] + counts[j]

    total_valid = 0
    j_limit = 0

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

    return total_valid // 3
