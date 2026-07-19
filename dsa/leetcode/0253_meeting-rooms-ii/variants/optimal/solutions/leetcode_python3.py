from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        starts = sorted(interval[0] for interval in intervals)
        ends = sorted(interval[1] for interval in intervals)
        end_index = 0
        rooms = 0
        maximum = 0
        for start in starts:
            while end_index < len(ends) and ends[end_index] <= start:
                rooms -= 1
                end_index += 1
            rooms += 1
            maximum = max(maximum, rooms)
        return maximum
