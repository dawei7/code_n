class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        points = sorted(map(tuple, trees))
        if len(points) <= 1:
            return [list(point) for point in points]

        def cross(origin, first, second):
            return (
                (first[0] - origin[0]) * (second[1] - origin[1])
                - (first[1] - origin[1]) * (second[0] - origin[0])
            )

        lower = []
        for point in points:
            while (
                len(lower) >= 2
                and cross(lower[-2], lower[-1], point) < 0
            ):
                lower.pop()
            lower.append(point)

        upper = []
        for point in reversed(points):
            while (
                len(upper) >= 2
                and cross(upper[-2], upper[-1], point) < 0
            ):
                upper.pop()
            upper.append(point)

        return [
            list(point)
            for point in set(lower[:-1] + upper[:-1])
        ]

