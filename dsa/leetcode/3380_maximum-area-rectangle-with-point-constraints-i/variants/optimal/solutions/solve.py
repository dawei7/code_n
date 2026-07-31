def solve(points: list[list[int]]) -> int:
    point_set = {tuple(point) for point in points}
    best = -1

    for first in range(len(points)):
        x1, y1 = points[first]
        for second in range(first):
            x2, y2 = points[second]
            if x1 == x2 or y1 == y2:
                continue

            corners = {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
            if not corners.issubset(point_set):
                continue

            left, right = sorted((x1, x2))
            bottom, top = sorted((y1, y2))
            blocked = any(left <= x <= right and bottom <= y <= top and (x, y) not in corners for x, y in points)
            if not blocked:
                best = max(best, (right - left) * (top - bottom))

    return best
