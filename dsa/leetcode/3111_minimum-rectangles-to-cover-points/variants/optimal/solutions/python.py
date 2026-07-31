def solve(points: list[list[int]], w: int) -> int:
    ordered_points = sorted(points)
    rectangles = 0
    covered_through = -1

    for x, _ in ordered_points:
        if x > covered_through:
            rectangles += 1
            covered_through = x + w

    return rectangles
