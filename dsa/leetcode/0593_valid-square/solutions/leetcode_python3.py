class Solution:
    def validSquare(
        self,
        p1: list[int],
        p2: list[int],
        p3: list[int],
        p4: list[int],
    ) -> bool:
        def squared_distance(first, second):
            dx = first[0] - second[0]
            dy = first[1] - second[1]
            return dx * dx + dy * dy

        points = [p1, p2, p3, p4]
        distances = sorted(
            squared_distance(points[first], points[second])
            for first in range(4)
            for second in range(first + 1, 4)
        )

        return (
            distances[0] > 0
            and distances[0]
            == distances[1]
            == distances[2]
            == distances[3]
            and distances[4] == distances[5]
            and distances[4] == 2 * distances[0]
        )

