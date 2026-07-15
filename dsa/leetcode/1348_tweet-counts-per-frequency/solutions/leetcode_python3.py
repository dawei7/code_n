from collections import defaultdict
from typing import List


class TweetCounts:
    _WIDTHS = {"minute": 60, "hour": 3600, "day": 86400}

    def __init__(self):
        self.times = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.times[tweetName].append(time)

    def getTweetCountsPerFrequency(
        self, freq: str, tweetName: str, startTime: int, endTime: int
    ) -> List[int]:
        width = self._WIDTHS[freq]
        counts = [0] * ((endTime - startTime) // width + 1)
        for time in self.times.get(tweetName, ()):
            if startTime <= time <= endTime:
                counts[(time - startTime) // width] += 1
        return counts
