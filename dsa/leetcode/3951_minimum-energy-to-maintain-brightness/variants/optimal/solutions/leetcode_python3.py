class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        intervals.sort()

        active_time = 0
        current_start, current_end = intervals[0]

        for start, end in intervals[1:]:
            if start > current_end:
                active_time += current_end - current_start + 1
                current_start, current_end = start, end
            elif end > current_end:
                current_end = end

        active_time += current_end - current_start + 1
        bulbs_needed = (brightness + 2) // 3
        return bulbs_needed * active_time
