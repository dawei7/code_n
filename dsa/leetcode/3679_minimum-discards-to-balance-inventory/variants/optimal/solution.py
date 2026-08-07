from collections import defaultdict, deque
from typing import List


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        kept_days = defaultdict(deque)
        discarded = 0

        for day, item_type in enumerate(arrivals):
            days = kept_days[item_type]
            while days and days[0] <= day - w:
                days.popleft()

            if len(days) == m:
                discarded += 1
            else:
                days.append(day)

        return discarded
