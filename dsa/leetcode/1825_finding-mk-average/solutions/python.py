"""App-local reference solution for LeetCode 1825."""

from collections import deque


class MKAverage:
    _LIMIT = 100_000

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.window = deque()
        self.counts = [0] * (self._LIMIT + 1)
        self.sums = [0] * (self._LIMIT + 1)

    def _update(self, tree: list[int], index: int, delta: int) -> None:
        while index <= self._LIMIT:
            tree[index] += delta
            index += index & -index

    def _prefix(self, tree: list[int], index: int) -> int:
        total = 0
        while index:
            total += tree[index]
            index -= index & -index
        return total

    def _sum_smallest(self, amount: int) -> int:
        index = 0
        count_before = 0
        step = 1 << (self._LIMIT.bit_length() - 1)
        while step:
            following = index + step
            if following <= self._LIMIT and count_before + self.counts[following] < amount:
                index = following
                count_before += self.counts[following]
            step >>= 1
        value = index + 1
        return self._prefix(self.sums, index) + (amount - count_before) * value

    def addElement(self, num: int) -> None:
        self.window.append(num)
        self._update(self.counts, num, 1)
        self._update(self.sums, num, num)
        if len(self.window) > self.m:
            removed = self.window.popleft()
            self._update(self.counts, removed, -1)
            self._update(self.sums, removed, -removed)

    def calculateMKAverage(self) -> int:
        if len(self.window) < self.m:
            return -1
        middle = self._sum_smallest(self.m - self.k) - self._sum_smallest(self.k)
        return middle // (self.m - 2 * self.k)


def solve(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    instance: MKAverage | None = None
    output: list[int | None] = []
    for operation, args in zip(operations, arguments):
        if operation == "MKAverage":
            instance = MKAverage(args[0], args[1])
            output.append(None)
        elif operation == "addElement":
            assert instance is not None
            instance.addElement(args[0])
            output.append(None)
        elif operation == "calculateMKAverage":
            assert instance is not None
            output.append(instance.calculateMKAverage())
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output
