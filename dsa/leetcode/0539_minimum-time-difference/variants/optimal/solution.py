from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0
        occupied = [False] * 1440
        for time_point in timePoints:
            hour, minute = map(int, time_point.split(":"))
            value = hour * 60 + minute
            if occupied[value]:
                return 0
            occupied[value] = True

        first = -1
        previous = -1
        minimum = 1440
        for minute, present in enumerate(occupied):
            if not present:
                continue
            if first < 0:
                first = minute
            if previous >= 0:
                minimum = min(minimum, minute - previous)
            previous = minute
        return min(minimum, first + 1440 - previous)
