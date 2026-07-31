from bisect import bisect_left


def solve(coordinates: list[list[int]], k: int) -> int:
    target_x, target_y = coordinates[k]

    def longest_chain(points: list[list[int]]) -> int:
        tails: list[int] = []
        for _, y in sorted(points, key=lambda point: (point[0], -point[1])):
            position = bisect_left(tails, y)
            if position == len(tails):
                tails.append(y)
            else:
                tails[position] = y
        return len(tails)

    lower = [point for point in coordinates if point[0] < target_x and point[1] < target_y]
    upper = [point for point in coordinates if point[0] > target_x and point[1] > target_y]
    return longest_chain(lower) + 1 + longest_chain(upper)
