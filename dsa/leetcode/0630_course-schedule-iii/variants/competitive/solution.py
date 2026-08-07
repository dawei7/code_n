from heapq import heappop, heappush
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        elapsed = 0
        selected = []

        for duration, deadline in sorted(courses, key=lambda course: course[1]):
            elapsed += duration
            heappush(selected, -duration)
            if elapsed > deadline:
                elapsed += heappop(selected)
        return len(selected)
