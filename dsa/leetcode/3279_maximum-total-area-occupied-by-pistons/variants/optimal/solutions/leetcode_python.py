from typing import List


class Solution:
    def maxArea(self, height: int, positions: List[int], directions: str) -> int:
        period = 2 * height
        events = {}
        slope = 0

        for position, direction in zip(positions, directions):
            phase = position if direction == "U" else (period - position) % period

            if phase < height:
                slope += 1
                top_time = height - phase
                bottom_time = period - phase
            else:
                slope -= 1
                bottom_time = period - phase
                top_time = 3 * height - phase

            events[top_time] = events.get(top_time, 0) - 2
            events[bottom_time] = events.get(bottom_time, 0) + 2

        area = sum(positions)
        maximum = area
        previous_time = 0

        for time in sorted(events):
            area += slope * (time - previous_time)
            maximum = max(maximum, area)
            slope += events[time]
            previous_time = time

        return maximum
