"""Average-constant-time LFU operation trace for LeetCode 460."""

from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values: dict[int, list[int]] = {}
        self.frequencies: defaultdict[int, OrderedDict[int, None]] = defaultdict(OrderedDict)
        self.minimum_frequency = 0

    def _promote(self, key: int) -> None:
        frequency = self.values[key][1]
        bucket = self.frequencies[frequency]
        del bucket[key]
        if not bucket:
            del self.frequencies[frequency]
            if self.minimum_frequency == frequency:
                self.minimum_frequency += 1
        self.values[key][1] = frequency + 1
        self.frequencies[frequency + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        self._promote(key)
        return self.values[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.values:
            self.values[key][0] = value
            self._promote(key)
            return
        if len(self.values) == self.capacity:
            victim, _ = self.frequencies[self.minimum_frequency].popitem(last=False)
            if not self.frequencies[self.minimum_frequency]:
                del self.frequencies[self.minimum_frequency]
            del self.values[victim]
        self.values[key] = [value, 1]
        self.frequencies[1][key] = None
        self.minimum_frequency = 1


def solve(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    cache: LFUCache | None = None
    output: list[int | None] = []
    for operation, args in zip(operations, arguments):
        if operation == "LFUCache":
            cache = LFUCache(args[0])
            output.append(None)
        elif operation == "put":
            assert cache is not None
            cache.put(args[0], args[1])
            output.append(None)
        else:
            assert cache is not None
            output.append(cache.get(args[0]))
    return output
