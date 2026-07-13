"""Optimal solution for LeetCode 1094: Car Pooling."""


def solve(trips: list[list[int]], capacity: int) -> bool:
    changes: dict[int, int] = {}
    for passengers, start, end in trips:
        changes[start] = changes.get(start, 0) + passengers
        changes[end] = changes.get(end, 0) - passengers

    current = 0
    for location in sorted(changes):
        current += changes[location]
        if current > capacity:
            return False
    return True
