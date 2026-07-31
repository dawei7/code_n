from collections import defaultdict


def solve(segments: list[list[int]]) -> list[list[int]]:
    changes: dict[int, int] = defaultdict(int)
    for start, end, color in segments:
        changes[start] += color
        changes[end] -= color

    painting: list[list[int]] = []
    mixed_color = 0
    previous: int | None = None
    for coordinate in sorted(changes):
        if previous is not None and mixed_color:
            painting.append([previous, coordinate, mixed_color])
        mixed_color += changes[coordinate]
        previous = coordinate

    return painting
