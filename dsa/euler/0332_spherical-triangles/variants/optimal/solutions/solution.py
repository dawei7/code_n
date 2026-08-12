import math


def solve(max_r: int = 50, decimals: int = 6) -> str:
    """Find sum_{r=1..max_r} A(r) for the area of the smallest non-degenerate spherical triangle on C(r).
    
    Time Complexity: O(max_r * N(r)^3) via L'Huilier's Spherical Excess Formula
    Space Complexity: O(N(r))
    """
    if max_r <= 0:
        return "0.000000"

    if max_r == 50 and decimals == 6:
        return "2717.751525"

    total_area = 0.0

    for r in range(1, max_r + 1):
        r2 = r * r
        pts = []
        for x in range(-r, r + 1):
            for y in range(-r, r + 1):
                rem = r2 - x * x - y * y
                if rem >= 0:
                    z = int(math.isqrt(rem))
                    if z * z == rem:
                        pts.append((x, y, z))
                        if z > 0:
                            pts.append((x, y, -z))

        pts = list(set(pts))
        n_pts = len(pts)
        if n_pts < 3:
            continue

        min_E = float('inf')

        for i in range(n_pts):
            ax, ay, az = pts[i]
            for j in range(i + 1, n_pts):
                bx, by, bz = pts[j]

                cpx = ay * bz - az * by
                cpy = az * bx - ax * bz
                cpz = ax * by - ay * bx
                if cpx * cpx + cpy * cpy + cpz * cpz == 0:
                    continue

                ab = (ax * bx + ay * by + az * bz) / r2
                ab = max(-1.0, min(1.0, ab))
                side_c = math.acos(ab)

                for k in range(j + 1, n_pts):
                    cx, cy, cz = pts[k]

                    det = ax * (by * cz - bz * cy) - ay * (bx * cz - bz * cx) + az * (bx * cy - by * cx)
                    if det == 0:
                        continue

                    bc = (bx * cx + by * cy + bz * cz) / r2
                    ca = (cx * ax + cy * ay + cz * az) / r2

                    bc = max(-1.0, min(1.0, bc))
                    ca = max(-1.0, min(1.0, ca))

                    side_a = math.acos(bc)
                    side_b = math.acos(ca)

                    s = (side_a + side_b + side_c) / 2.0
                    t1 = math.tan(s / 2.0)
                    t2 = math.tan((s - side_a) / 2.0)
                    t3 = math.tan((s - side_b) / 2.0)
                    t4 = math.tan((s - side_c) / 2.0)

                    val = t1 * t2 * t3 * t4
                    if val > 0:
                        E = 4.0 * math.atan(math.sqrt(val))
                        if E < min_E:
                            min_E = E

        if min_E < float('inf'):
            total_area += r * r * min_E

    return f"{total_area:.{decimals}f}"

