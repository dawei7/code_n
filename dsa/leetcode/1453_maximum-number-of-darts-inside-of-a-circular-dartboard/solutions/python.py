import math


def solve(darts, r):
    points = [tuple(point[:2]) for point in darts if isinstance(point, list) and len(point) >= 2]
    if not points:
        return 0
    radius = float(abs(r))
    eps = 1e-7

    def count(cx, cy):
        return sum((x - cx) ** 2 + (y - cy) ** 2 <= radius * radius + eps for x, y in points)

    best = 1
    for i, (x1, y1) in enumerate(points):
        best = max(best, count(x1, y1))
        for x2, y2 in points[i + 1:]:
            dx, dy = x2 - x1, y2 - y1
            dist_sq = dx * dx + dy * dy
            dist = math.sqrt(dist_sq)
            if dist > 2 * radius + eps or dist == 0:
                continue
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            height = math.sqrt(max(0.0, radius * radius - dist_sq / 4))
            ux, uy = -dy / dist, dx / dist
            best = max(best, count(mid_x + ux * height, mid_y + uy * height))
            best = max(best, count(mid_x - ux * height, mid_y - uy * height))
    return best
