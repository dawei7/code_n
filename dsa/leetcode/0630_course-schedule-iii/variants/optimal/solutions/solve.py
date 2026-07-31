from heapq import heappop, heappush


def solve(courses: list[list[int]]) -> int:
    elapsed = 0
    selected: list[int] = []

    for duration, deadline in sorted(courses, key=lambda course: course[1]):
        elapsed += duration
        heappush(selected, -duration)
        if elapsed > deadline:
            elapsed += heappop(selected)
    return len(selected)
