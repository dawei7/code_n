"""Optimal solution for LeetCode 1353: Maximum Number of Events That Can Be Attended."""

from heapq import heappop, heappush


def solve(events: list[list[int]]) -> int:
    events.sort()
    heap: list[int] = []
    day = 0
    i = 0
    attended = 0
    n = len(events)

    while i < n or heap:
        if not heap:
            day = max(day, events[i][0])
        while i < n and events[i][0] <= day:
            heappush(heap, events[i][1])
            i += 1
        while heap and heap[0] < day:
            heappop(heap)
        if heap:
            heappop(heap)
            attended += 1
            day += 1
    return attended
