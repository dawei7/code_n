"""Optimal app-local solution for LeetCode 1503."""


def solve(n: int, left: list[int], right: list[int]) -> int:
    """Return the last endpoint-arrival time among all ant trajectories."""
    answer = 0
    for position in left:
        if position > answer:
            answer = position
    for position in right:
        distance = n - position
        if distance > answer:
            answer = distance
    return answer
