from typing import List


# Definition for an Interval.
# class Interval:
#     def __init__(self, start: int = None, end: int = None):
#         self.start = start
#         self.end = end


class Solution:
    def employeeFreeTime(self, schedule: "List[List[Interval]]") -> "List[Interval]":
        intervals = sorted(
            (interval for employee in schedule for interval in employee),
            key=lambda interval: interval.start,
        )

        free_time = []
        current_end = intervals[0].end

        for interval in intervals[1:]:
            if interval.start > current_end:
                free_time.append(Interval(current_end, interval.start))
            current_end = max(current_end, interval.end)

        return free_time
