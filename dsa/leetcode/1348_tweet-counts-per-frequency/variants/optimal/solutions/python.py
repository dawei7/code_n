"""App-local adapter and reference design for LeetCode 1348."""

from collections import defaultdict


class TweetCounts:
    _WIDTHS = {"minute": 60, "hour": 3600, "day": 86400}

    def __init__(self):
        self.times = defaultdict(list)

    def recordTweet(self, tweetName, time):
        self.times[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        width = self._WIDTHS[freq]
        counts = [0] * ((endTime - startTime) // width + 1)
        for time in self.times.get(tweetName, ()):
            if startTime <= time <= endTime:
                counts[(time - startTime) // width] += 1
        return counts


def solve(operations, arguments):
    service = None
    output = []
    for operation, args in zip(operations, arguments):
        if operation == "TweetCounts":
            service = TweetCounts()
            output.append(None)
        elif operation == "recordTweet":
            assert service is not None
            service.recordTweet(*args)
            output.append(None)
        elif operation == "getTweetCountsPerFrequency":
            assert service is not None
            output.append(service.getTweetCountsPerFrequency(*args))
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output
