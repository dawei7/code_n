from collections import Counter, deque
from heapq import heappop, heappush


class StatisticsTracker:
    def __init__(self):
        self.numbers = deque()
        self.total = 0

        self.lower = []
        self.upper = []
        self.lower_size = 0
        self.upper_size = 0
        self.delayed = Counter()

        self.frequency = Counter()
        self.mode_heap = []

    def _prune(self, heap, sign):
        while heap:
            value = sign * heap[0]
            if self.delayed[value] == 0:
                break
            heappop(heap)
            self.delayed[value] -= 1

    def _rebalance(self):
        if self.upper_size > self.lower_size + 1:
            self._prune(self.upper, 1)
            value = heappop(self.upper)
            self.upper_size -= 1
            heappush(self.lower, -value)
            self.lower_size += 1
            self._prune(self.upper, 1)
        elif self.lower_size > self.upper_size:
            self._prune(self.lower, -1)
            value = -heappop(self.lower)
            self.lower_size -= 1
            heappush(self.upper, value)
            self.upper_size += 1
            self._prune(self.lower, -1)

    def addNumber(self, number: int) -> None:
        self.numbers.append(number)
        self.total += number

        self.frequency[number] += 1
        heappush(self.mode_heap, (-self.frequency[number], number))

        if not self.upper or number >= self.upper[0]:
            heappush(self.upper, number)
            self.upper_size += 1
        else:
            heappush(self.lower, -number)
            self.lower_size += 1
        self._rebalance()

    def removeFirstAddedNumber(self) -> None:
        number = self.numbers.popleft()
        self.total -= number

        self.frequency[number] -= 1
        self.delayed[number] += 1

        if self.upper and number >= self.upper[0]:
            self.upper_size -= 1
            if number == self.upper[0]:
                self._prune(self.upper, 1)
        else:
            self.lower_size -= 1
            if self.lower and number == -self.lower[0]:
                self._prune(self.lower, -1)
        self._rebalance()

    def getMean(self) -> int:
        return self.total // len(self.numbers)

    def getMedian(self) -> int:
        self._prune(self.upper, 1)
        return self.upper[0]

    def getMode(self) -> int:
        while -self.mode_heap[0][0] != self.frequency[self.mode_heap[0][1]]:
            heappop(self.mode_heap)
        return self.mode_heap[0][1]
