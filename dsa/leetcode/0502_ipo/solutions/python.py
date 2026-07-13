"""Capital sweep with a maximum-profit heap for LeetCode 502."""

from heapq import heappop, heappush


def solve(k: int, w: int, profits: list[int], capital: list[int]) -> int:
    projects = sorted(zip(capital, profits))
    available: list[int] = []
    project_index = 0

    for _ in range(k):
        while project_index < len(projects) and projects[project_index][0] <= w:
            heappush(available, -projects[project_index][1])
            project_index += 1
        if not available:
            break
        w -= heappop(available)
    return w
