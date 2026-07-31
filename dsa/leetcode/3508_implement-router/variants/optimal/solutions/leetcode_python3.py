from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from typing import List


class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()
        self.packets = set()
        self.timestamps = defaultdict(list)
        self.left_index = defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packets:
            return False

        if len(self.queue) == self.limit:
            self._remove_oldest()

        self.queue.append(packet)
        self.packets.add(packet)
        self.timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        return list(self._remove_oldest())

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        values = self.timestamps.get(destination, [])
        left = self.left_index.get(destination, 0)
        return bisect_right(values, endTime, lo=left) - bisect_left(
            values, startTime, lo=left
        )

    def _remove_oldest(self):
        packet = self.queue.popleft()
        self.packets.remove(packet)
        self.left_index[packet[1]] += 1
        return packet
