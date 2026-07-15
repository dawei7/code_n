class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        minute_angle = minutes * 6
        difference = abs(hour_angle - minute_angle)
        return min(difference, 360 - difference)
