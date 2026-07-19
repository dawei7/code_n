from collections import defaultdict


def solve(adjacentPairs: list[list[int]]) -> list[int]:
    neighbors: dict[int, list[int]] = defaultdict(list)
    for left, right in adjacentPairs:
        neighbors[left].append(right)
        neighbors[right].append(left)

    current = next(value for value, adjacent in neighbors.items() if len(adjacent) == 1)
    restored = [current]
    previous = None

    while len(restored) < len(neighbors):
        for candidate in neighbors[current]:
            if candidate != previous:
                restored.append(candidate)
                previous, current = current, candidate
                break

    return restored
