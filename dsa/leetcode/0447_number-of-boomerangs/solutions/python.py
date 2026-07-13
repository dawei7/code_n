"""Optimal app-local solution for LeetCode 447."""


def solve(points: list[list[int]]) -> int:
    answer = 0
    for pivot_x, pivot_y in points:
        frequencies: dict[int, int] = {}
        for point_x, point_y in points:
            distance = (point_x - pivot_x) ** 2 + (point_y - pivot_y) ** 2
            previous = frequencies.get(distance, 0)
            answer += 2 * previous
            frequencies[distance] = previous + 1
    return answer
