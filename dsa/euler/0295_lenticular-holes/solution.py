"""Project Euler 295: Lenticular Holes

Find L(100 000), the number of distinct lenticular pairs (r1, r2) for which 0 < r1 <= r2 <= 100 000.
A lenticular hole is the convex area enclosed by two circles with integer centers intersecting at two
lattice points with no interior lattice points inside the lens.
"""

from __future__ import annotations

import math


def solve(limit_n: int = 100_000) -> str:
    """Calculates L(limit_n) using Chord Lattice Reduction, Geometric Closest-Point Bounds,

    and Compressed Bitmask Adjacency.
    """

    def ext_gcd(a: int, b: int) -> tuple[int, int]:
        if b == 0:
            return 1, 0
        x1, y1 = ext_gcd(b, a % b)
        return y1, x1 - (a // b) * y1

    chords: list[tuple[list[int], list[int]]] = []
    # For limit_n = 100_000, max_d = 2 * limit_n completely covers all admissible chords.
    max_d = 2 * limit_n

    for u in range(1, int(math.isqrt(max_d)) + 1, 2):
        for v in range(1, int(math.isqrt(max_d - u * u)) + 1, 2):
            if math.gcd(u, v) != 1:
                continue
            d_val = u * u + v * v
            x_g, y_g = ext_gcd(u, v)
            m_val = d_val // 2
            x0 = x_g * m_val
            y0 = y_g * m_val

            xv, _ = ext_gcd(v, u)
            x1_base = xv
            y1_base = (v * x1_base - 1) // u
            t1 = -math.floor((x1_base * u + y1_base * v) / d_val)
            p1_x = x1_base + t1 * u
            p1_y = y1_base + t1 * v
            p2_x = u - p1_x
            p2_y = v - p1_y

            k_opt = round((x0 * v - y0 * u) / d_val)
            k_span = int(limit_n / math.sqrt(d_val)) + 2

            s1: list[int] = []
            s2: list[int] = []
            for k in range(k_opt - k_span, k_opt + k_span + 1):
                cx = x0 - k * v
                cy = y0 + k * u
                r2 = cx * cx + cy * cy
                if r2 <= limit_n * limit_n:
                    side = v * cx - u * cy
                    if side < 0:
                        if p1_x * p1_x + p1_y * p1_y >= 2 * (p1_x * cx + p1_y * cy):
                            s1.append(r2)
                    elif side > 0:
                        if p2_x * p2_x + p2_y * p2_y >= 2 * (p2_x * cx + p2_y * cy):
                            s2.append(r2)

            if s1 and s2:
                chords.append((s1, s2))

    num_chords = len(chords)

    # Map each radius to its active chord bitmask:
    # Bit c (0 <= c < num_chords) for side 1, bit (num_chords + c) for side 2.
    radius_masks: dict[int, int] = {}
    for c, (s1, s2) in enumerate(chords):
        b1 = 1 << c
        b2 = 1 << (num_chords + c)
        for r in s1:
            radius_masks[r] = radius_masks.get(r, 0) | b1
        for r in s2:
            radius_masks[r] = radius_masks.get(r, 0) | b2

    mask_to_radii: dict[int, list[int]] = {}
    for r, m in radius_masks.items():
        mask_to_radii.setdefault(m, []).append(r)

    def get_opp(m: int) -> int:
        m1 = m & ((1 << num_chords) - 1)
        m2 = m >> num_chords
        return (m1 << num_chords) | m2

    unique_masks = list(mask_to_radii.keys())
    opp_masks = [get_opp(m) for m in unique_masks]

    total_pairs = 0
    num_u = len(unique_masks)

    for i in range(num_u):
        u_opp = opp_masks[i]
        len_u = len(mask_to_radii[unique_masks[i]])
        for j in range(i, num_u):
            if (u_opp & unique_masks[j]) != 0:
                len_v = len(mask_to_radii[unique_masks[j]])
                if i == j:
                    total_pairs += len_u * (len_u + 1) // 2
                else:
                    total_pairs += len_u * len_v

    return str(total_pairs)


if __name__ == "__main__":
    print(solve())
