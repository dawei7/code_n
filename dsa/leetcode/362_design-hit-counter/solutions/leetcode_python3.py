class HitCounter:

    def __init__(self):
        self.timestamps = [0] * 300
        self.counts = [0] * 300

    def hit(self, timestamp: int) -> None:
        slot = timestamp % 300
        if self.timestamps[slot] != timestamp:
            self.timestamps[slot] = timestamp
            self.counts[slot] = 1
        else:
            self.counts[slot] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for stored_timestamp, count in zip(self.timestamps, self.counts):
            if timestamp - stored_timestamp < 300:
                total += count
        return total

