def solve(points: list[list[int]]) -> int:
    if not points:
        return 0
    points.sort(key=lambda interval: interval[1])
    arrows = 1
    arrow = points[0][1]
    for start, end in points[1:]:
        if start > arrow:
            arrows += 1
            arrow = end
    return arrows
