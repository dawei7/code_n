"""Optimal app-local solution for LeetCode 1094."""


def solve(trips: list[list[int]], capacity: int) -> bool:
    changes = [0] * 1001
    for passengers, start, end in trips:
        changes[start] += passengers
        changes[end] -= passengers

    passengers_aboard = 0
    for change in changes:
        passengers_aboard += change
        if passengers_aboard > capacity:
            return False
    return True
