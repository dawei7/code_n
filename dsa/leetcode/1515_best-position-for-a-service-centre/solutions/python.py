import math


def solve(positions):
    points = []
    for index, point in enumerate(positions):
        if isinstance(point, list) and len(point) >= 2:
            points.append((float(point[0]), float(point[1])))
        else:
            points.append((float(index), float(point)))
    if not points:
        return 0.0

    def total(cx, cy):
        return sum(math.hypot(px - cx, py - cy) for px, py in points)

    min_x = min(px for px, _ in points)
    max_x = max(px for px, _ in points)
    min_y = min(py for _, py in points)
    max_y = max(py for _, py in points)

    def best_for_x(cx):
        lo, hi = min_y, max_y
        for _ in range(80):
            third = (hi - lo) / 3.0
            y1 = lo + third
            y2 = hi - third
            if total(cx, y1) < total(cx, y2):
                hi = y2
            else:
                lo = y1
        cy = (lo + hi) / 2.0
        return total(cx, cy)

    lo, hi = min_x, max_x
    for _ in range(80):
        third = (hi - lo) / 3.0
        x1 = lo + third
        x2 = hi - third
        if best_for_x(x1) < best_for_x(x2):
            hi = x2
        else:
            lo = x1
    return best_for_x((lo + hi) / 2.0)
