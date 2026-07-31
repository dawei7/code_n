from bisect import bisect_left, bisect_right


class ExamTracker:
    def __init__(self):
        self.times: list[int] = []
        self.prefix: list[int] = [0]

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.prefix.append(self.prefix[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        left = bisect_left(self.times, startTime)
        right = bisect_right(self.times, endTime)
        return self.prefix[right] - self.prefix[left]
