from collections import deque


class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        lower_bound = t - 3000
        while self.requests[0] < lower_bound:
            self.requests.popleft()
        return len(self.requests)
