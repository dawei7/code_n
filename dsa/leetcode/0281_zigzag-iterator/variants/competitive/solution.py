from collections import deque
from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.active = deque()
        if v1:
            self.active.append((v1, 0))
        if v2:
            self.active.append((v2, 0))

    def next(self) -> int:
        values, index = self.active.popleft()
        value = values[index]
        if index + 1 < len(values):
            self.active.append((values, index + 1))
        return value

    def hasNext(self) -> bool:
        return bool(self.active)
