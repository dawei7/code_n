"""Optimal solution for LeetCode 370: Range Addition."""


def solve(length: int, updates: list[list[int]]) -> list[int]:
    difference = [0] * length

    for start, end, increment in updates:
        difference[start] += increment
        if end + 1 < length:
            difference[end + 1] -= increment

    running = 0
    for i in range(length):
        running += difference[i]
        difference[i] = running
    return difference
