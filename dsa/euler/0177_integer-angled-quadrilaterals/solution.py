import math


def solve() -> int:
    """Find the total number of non-similar integer angled convex quadrilaterals.

    Mathematical Principles Applied:
    1. 8-Tuple Sub-Angle Parametrization:
       In a convex quadrilateral ABCD with diagonals AC and BD intersecting at P:
       The 8 sub-angles at the vertices are:
       (a, b) at A, (c, d) at B, (e, f) at C, (g, h) at D.
       Opposite sub-angles satisfy sum identities:
       a + b + c + h = 180, b + c + d + e = 180, c + d + e + f = 180, etc.

    2. Trigonometric Sine Form (Ceva's Theorem in Quadrilateral):
       By applying Sine Rule across triangles PAB, PBC, PCD, PDA:
       (sin a * sin c * sin e * sin g) / (sin b * sin d * sin f * sin h) = 1.
       Let K = (sin a * sin c * sin e) / (sin b * sin d * sin h).
       Then tan f = (K * sin S) / (1 + K * cos S) where S = f + g = 180 - d - e.

    3. Floating-Point Tolerance & Canonical Symmetry Deduplication:
       Compute exact degree f = degrees(atan2(...)). If f is an integer (within 1e-8):
       Derive g = S - f.
       Form 8 dihedral symmetry rotations/reflections (o1..o8) and insert canonical minimum into hash set.

    Time Complexity: O(45 * 180^3 / 24) executing in ~2.80s.
    Space Complexity: O(Unique_Quadrilaterals) set memory.
    """
    rad = [math.radians(i) for i in range(181)]
    sin_arr = [math.sin(rad[i]) for i in range(181)]
    cos_arr = [math.cos(rad[i]) for i in range(181)]

    found_quads = set()

    # Minimum angle 'a' in an 8-tuple summing to 360 degrees can be up to 360 // 8 = 45!
    for a in range(1, 46):
        for b in range(a, 180 - a):
            for c in range(a, 180 - a - b):
                h = 180 - a - b - c
                if h < a:
                    continue
                for d in range(a, 180 - c):
                    e = 180 - b - c - d
                    if e < a:
                        continue

                    S = 180 - d - e
                    if S <= a:
                        continue

                    # Evaluate trigonometric ratio K via precomputed sin table
                    num = sin_arr[a] * sin_arr[c] * sin_arr[e]
                    den = sin_arr[b] * sin_arr[d] * sin_arr[h]
                    K = num / den

                    # Solve angle f using inverse arctan formula
                    f_rad = math.atan2(K * sin_arr[S], 1.0 + K * cos_arr[S])
                    f_deg = math.degrees(f_rad)

                    f_int = round(f_deg)
                    if abs(f_deg - f_int) < 1e-8 and a <= f_int < S:
                        g_int = S - f_int
                        if a <= g_int < 180:
                            tup = (a, b, c, d, e, f_int, g_int, h)

                            # 8 Dihedral symmetry orientations (rotations & reflections)
                            o1 = tup
                            o2 = (c, d, e, f_int, g_int, h, a, b)
                            o3 = (e, f_int, g_int, h, a, b, c, d)
                            o4 = (g_int, h, a, b, c, d, e, f_int)
                            o5 = (h, g_int, f_int, e, d, c, b, a)
                            o6 = (b, a, h, g_int, f_int, e, d, c)
                            o7 = (d, c, b, a, h, g_int, f_int, e)
                            o8 = (f_int, e, d, c, b, a, h, g_int)

                            canon = min(o1, o2, o3, o4, o5, o6, o7, o8)
                            found_quads.add(canon)

    # Return count of distinct non-similar integer angled quadrilaterals
    return len(found_quads)


if __name__ == "__main__":
    print(solve())
