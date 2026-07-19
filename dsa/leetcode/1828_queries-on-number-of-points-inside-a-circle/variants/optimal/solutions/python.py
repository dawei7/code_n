"""App-local reference solution for LeetCode 1828."""


def solve(points: list[list[int]], queries: list[list[int]]) -> list[int]:
    answer = []
    for center_x, center_y, radius in queries:
        radius_squared = radius * radius
        count = 0
        for point_x, point_y in points:
            delta_x = point_x - center_x
            delta_y = point_y - center_y
            if delta_x * delta_x + delta_y * delta_y <= radius_squared:
                count += 1
        answer.append(count)
    return answer
