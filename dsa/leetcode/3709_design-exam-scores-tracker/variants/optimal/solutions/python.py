from bisect import bisect_left, bisect_right


class ExamTracker:
    def __init__(self) -> None:
        self.times: list[int] = []
        self.prefix: list[int] = [0]

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.prefix.append(self.prefix[-1] + score)

    def totalScore(self, start_time: int, end_time: int) -> int:
        left = bisect_left(self.times, start_time)
        right = bisect_right(self.times, end_time)
        return self.prefix[right] - self.prefix[left]


def solve(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    tracker: ExamTracker | None = None
    output: list[int | None] = []

    for operation, values in zip(operations, arguments):
        if operation == "ExamTracker":
            tracker = ExamTracker()
            output.append(None)
        elif operation == "record":
            assert tracker is not None
            tracker.record(values[0], values[1])
            output.append(None)
        elif operation == "totalScore":
            assert tracker is not None
            output.append(tracker.totalScore(values[0], values[1]))
        else:
            raise ValueError(f"unknown operation: {operation}")

    return output
