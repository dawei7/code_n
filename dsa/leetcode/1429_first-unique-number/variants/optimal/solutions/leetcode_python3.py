from collections import deque
from typing import List


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.counts = {}
        self.unique = deque()
        for value in nums:
            self.add(value)

    def showFirstUnique(self) -> int:
        while self.unique and self.counts[self.unique[0]] > 1:
            self.unique.popleft()
        return self.unique[0] if self.unique else -1

    def add(self, value: int) -> None:
        self.counts[value] = self.counts.get(value, 0) + 1
        if self.counts[value] == 1:
            self.unique.append(value)
