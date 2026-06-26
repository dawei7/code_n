"""Optimal solution for dc_05: Closest Pair of Points.

Given n points in the plane, return the smallest
"""


def solve(points, n):
    """Closest pair of points via D&C plane sweep."""
    if n < 2:
        return 0.0
    px = sorted(points, key=lambda p: (p[0], p[1]))
    return _closest(px, 0, n - 1)

def _dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def _brute(pts, lo, hi):
    best = float("inf")
    for i in range(lo, hi + 1):
        for j in range(i + 1, hi + 1):
            d = _dist(pts[i], pts[j])
            if d < best:
                best = d
    return best

def _closest(px, lo, hi):
    n = hi - lo + 1
    if n <= 3:
        return _brute(px, lo, hi)
    mid = (lo + hi) // 2
    mid_x = px[mid][0]
    dl = _closest(px, lo, mid)
    dr = _closest(px, mid + 1, hi)
    d = min(dl, dr)
    strip = [px[k] for k in range(lo, hi + 1) if abs(px[k][0] - mid_x) < d]
    strip.sort(key=lambda p: p[1])
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) ** 2 >= d * d:
                break
            cand = _dist(strip[i], strip[j])
            if cand < d:
                d = cand
    return d
