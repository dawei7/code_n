def solve(trees: list[list[int]]) -> list[list[int]]:
    """Return every point on the convex hull boundary."""
    points = sorted(map(tuple, trees))
    if len(points) <= 1:
        return [list(point) for point in points]

    def cross(
        origin: tuple[int, int],
        first: tuple[int, int],
        second: tuple[int, int],
    ) -> int:
        return (
            (first[0] - origin[0]) * (second[1] - origin[1])
            - (first[1] - origin[1]) * (second[0] - origin[0])
        )

    lower: list[tuple[int, int]] = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) < 0:
            lower.pop()
        lower.append(point)

    upper: list[tuple[int, int]] = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) < 0:
            upper.pop()
        upper.append(point)

    boundary = set(lower[:-1] + upper[:-1])
    return [list(point) for point in boundary]

