from heapq import heappop, heappush
from typing import List


class Solution:
    def smallestChair(
        self,
        times: List[List[int]],
        targetFriend: int,
    ) -> int:
        arrivals = sorted(
            (arrival, leaving, friend)
            for friend, (arrival, leaving) in enumerate(times)
        )
        available: List[int] = []
        occupied: List[tuple[int, int]] = []
        next_chair = 0

        for arrival, leaving, friend in arrivals:
            while occupied and occupied[0][0] <= arrival:
                _, chair = heappop(occupied)
                heappush(available, chair)

            if available:
                chair = heappop(available)
            else:
                chair = next_chair
                next_chair += 1

            if friend == targetFriend:
                return chair

            heappush(occupied, (leaving, chair))

        raise RuntimeError("target friend must arrive")
