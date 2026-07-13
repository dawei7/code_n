from bisect import bisect_left, bisect_right
from collections import defaultdict, deque


class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue: deque[tuple[int, int, int]] = deque()
        self.packets: set[tuple[int, int, int]] = set()
        self.timestamps: dict[int, list[int]] = defaultdict(list)
        self.left_index: dict[int, int] = defaultdict(int)

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

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        source, destination, timestamp = self._remove_oldest()
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        values = self.timestamps.get(destination, [])
        left = self.left_index.get(destination, 0)
        return bisect_right(values, endTime, lo=left) - bisect_left(values, startTime, lo=left)

    def _remove_oldest(self) -> tuple[int, int, int]:
        packet = self.queue.popleft()
        self.packets.remove(packet)
        self.left_index[packet[1]] += 1
        return packet


def solve(operations: list[str], arguments: list[list[int]]) -> list[object]:
    router: Router | None = None
    output: list[object] = []
    for operation, args in zip(operations, arguments):
        if operation == "Router":
            router = Router(args[0])
            output.append(None)
        elif operation == "addPacket":
            assert router is not None
            output.append(router.addPacket(args[0], args[1], args[2]))
        elif operation == "forwardPacket":
            assert router is not None
            output.append(router.forwardPacket())
        elif operation == "getCount":
            assert router is not None
            output.append(router.getCount(args[0], args[1], args[2]))
    return output
