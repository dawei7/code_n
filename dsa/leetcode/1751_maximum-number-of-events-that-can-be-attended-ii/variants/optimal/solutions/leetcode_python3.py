from bisect import bisect_right
from typing import List


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [start for start, _, _ in events]
        next_index = [
            bisect_right(starts, end)
            for _, end, _ in events
        ]

        previous = [0] * (len(events) + 1)
        for _ in range(k):
            current = [0] * (len(events) + 1)
            for index in range(len(events) - 1, -1, -1):
                current[index] = max(
                    current[index + 1],
                    events[index][2] + previous[next_index[index]],
                )
            previous = current

        return previous[0]
