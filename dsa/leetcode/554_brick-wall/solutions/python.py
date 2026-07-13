"""Internal-edge frequency counting for LeetCode 554."""


def solve(wall: list[list[int]]) -> int:
    edge_frequency = {}

    for row in wall:
        position = 0
        for width in row[:-1]:
            position += width
            edge_frequency[position] = edge_frequency.get(position, 0) + 1

    most_aligned = max(edge_frequency.values(), default=0)
    return len(wall) - most_aligned

