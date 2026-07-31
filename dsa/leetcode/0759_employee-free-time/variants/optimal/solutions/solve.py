class Interval:
    """Local equivalent of LeetCode's Interval for the standalone app."""

    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: list[list[Interval]]) -> list[Interval]:
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


def solve(schedule: list[list[list[int]]]) -> list[list[int]]:
    interval_schedule = [[Interval(start, end) for start, end in employee] for employee in schedule]
    return [[interval.start, interval.end] for interval in Solution().employeeFreeTime(interval_schedule)]
