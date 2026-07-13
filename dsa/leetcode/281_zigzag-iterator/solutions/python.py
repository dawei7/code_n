from collections import deque


class ZigzagIterator:
    def __init__(self, v1: list[int], v2: list[int]):
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


def solve(v1: list[int], v2: list[int]) -> list[int]:
    iterator = ZigzagIterator(v1, v2)
    output = []
    while iterator.hasNext():
        output.append(iterator.next())
    return output
