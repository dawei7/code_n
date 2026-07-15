"""Optimal app-local solution for LeetCode 933."""

from collections import deque


class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)
        lower_bound = t - 3000
        while self.requests[0] < lower_bound:
            self.requests.popleft()
        return len(self.requests)


def solve(operations):
    counter = RecentCounter()
    return [counter.ping(operation[1]) for operation in operations]
