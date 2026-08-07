from collections import defaultdict
from typing import List


class Solution:
    def maxIntersectionCount(self, y: List[int]) -> int:
        events = defaultdict(int)

        for first, second in zip(y, y[1:]):
            if first < second:
                events[2 * first] += 1
                events[2 * second] -= 1
            else:
                events[2 * second + 1] += 1
                events[2 * first + 1] -= 1

        events[2 * y[-1]] += 1
        events[2 * y[-1] + 1] -= 1

        active = 0
        answer = 0
        for height in sorted(events):
            active += events[height]
            answer = max(answer, active)

        return answer
