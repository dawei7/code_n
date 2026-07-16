def solve(points: list[list[int]]) -> int:
    point_count = len(points)
    in_tree = [False] * point_count
    best_distance = [float("inf")] * point_count
    best_distance[0] = 0
    total = 0

    for _ in range(point_count):
        next_point = -1
        for point in range(point_count):
            if not in_tree[point] and (
                next_point == -1 or best_distance[point] < best_distance[next_point]
            ):
                next_point = point

        in_tree[next_point] = True
        total += best_distance[next_point]
        x_value, y_value = points[next_point]

        for point, (other_x, other_y) in enumerate(points):
            if not in_tree[point]:
                distance = abs(x_value - other_x) + abs(y_value - other_y)
                if distance < best_distance[point]:
                    best_distance[point] = distance

    return total
