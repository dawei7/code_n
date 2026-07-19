"""Optimal app-local solution for LeetCode 900."""


class RLEIterator:
    def __init__(self, encoding):
        self.encoding = encoding
        self.index = 0
        self.remaining = encoding[0]

    def next(self, n):
        while self.index < len(self.encoding) and n > self.remaining:
            n -= self.remaining
            self.index += 2
            if self.index < len(self.encoding):
                self.remaining = self.encoding[self.index]

        if self.index == len(self.encoding):
            return -1

        self.remaining -= n
        return self.encoding[self.index + 1]


def solve(encoding, operations):
    iterator = RLEIterator(encoding)
    return [iterator.next(operation[1]) for operation in operations]
