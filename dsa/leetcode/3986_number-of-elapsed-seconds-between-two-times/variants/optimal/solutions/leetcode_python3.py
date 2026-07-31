class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def to_seconds(time: str) -> int:
            hours, minutes, seconds = map(int, time.split(":"))
            return hours * 3600 + minutes * 60 + seconds

        return to_seconds(endTime) - to_seconds(startTime)
