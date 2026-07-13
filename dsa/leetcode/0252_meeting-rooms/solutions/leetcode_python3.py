from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(intervals[i - 1][1] <= intervals[i][0] for i in range(1, len(intervals)))
