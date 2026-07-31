"""Optimal app-local solution for LeetCode 1353."""

from heapq import heappop, heappush


def solve(events):
    events.sort()
    active = []
    day = 0
    index = 0
    attended = 0

    while index < len(events) or active:
        if not active:
            day = max(day, events[index][0])
        while index < len(events) and events[index][0] <= day:
            heappush(active, events[index][1])
            index += 1
        while active and active[0] < day:
            heappop(active)
        if active:
            heappop(active)
            attended += 1
            day += 1

    return attended
