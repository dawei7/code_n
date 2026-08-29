"""Project Euler Problem 456: Triangles Containing the Origin II.

Find C(2_000_000), the number of triangles formed by 3 points in P_n
that contain the origin strictly in their interior.
"""

from math import atan2, gcd
from typing import Dict, List, Tuple

SHIFT = 21
MASK = (1 << SHIFT) - 1


def _comb3(k: int) -> int:
    return k * (k - 1) * (k - 2) // 6 if k >= 3 else 0


def solve(n: int = 2_000_000) -> int:
    """Compute C(n) using circular angular sorting and two-pointer radial sweep."""
    modx, mody = 32323, 30103
    offset_x = modx // 2
    offset_y = mody // 2
    ax, ay = 1248, 8421
    x, y = 1, 1

    points: List[Tuple[int, int]] = []
    line_counts: Dict[Tuple[int, int], int] = {}

    for _ in range(n):
        x = (x * ax) % modx
        y = (y * ay) % mody
        px = x - offset_x
        py = y - offset_y

        if px == 0 and py == 0:
            continue

        points.append((px, py))

        g = gcd(abs(px), abs(py))
        dx = px // g
        dy = py // g

        if dx > 0 or (dx == 0 and dy > 0):
            key = (dx, dy)
            side0 = True
        else:
            key = (-dx, -dy)
            side0 = False

        prev = line_counts.get(key, 0)
        if side0:
            line_counts[key] = prev + 1
        else:
            line_counts[key] = prev + (1 << SHIFT)

    m = len(points)
    if m < 3:
        return 0

    total_triples = _comb3(m)
    points.sort(key=lambda pt: atan2(pt[1], pt[0]))

    open_semicircle_triples = 0
    j = 1

    for i in range(m):
        if j < i + 1:
            j = i + 1

        xi, yi = points[i]

        while j < i + m:
            xj, yj = points[j % m]
            cross = xi * yj - yi * xj
            if cross > 0:
                j += 1
                continue
            if cross == 0:
                dot = xi * xj + yi * yj
                if dot > 0:
                    j += 1
                    continue
            break

        k = j - i - 1
        open_semicircle_triples += k * (k - 1) // 2

    antipodal_triples = 0
    for packed in line_counts.values():
        a = packed & MASK
        b = packed >> SHIFT
        if a == 0 or b == 0:
            continue
        t = a + b
        antipodal_triples += a * b * (m - t) + (
            _comb3(t) - _comb3(a) - _comb3(b)
        )

    return total_triples - open_semicircle_triples - antipodal_triples


if __name__ == "__main__":
    print(solve())
