from collections import defaultdict, deque


class Solution:
    def maxRequests(self, requests: list[list[int]], k: int, window: int) -> int:
        times_by_user = defaultdict(list)

        for user, time in requests:
            times_by_user[user].append(time)

        kept = 0

        for times in times_by_user.values():
            times.sort()
            active = deque()

            for time in times:
                while active and time - active[0] > window:
                    active.popleft()

                if len(active) < k:
                    active.append(time)
                    kept += 1

        return kept
