"""Optimal app-local solution for LeetCode 1429."""

from collections import deque


class FirstUnique:
    def __init__(self, nums: list[int]):
        self._counts: dict[int, int] = {}
        self._unique = deque()
        for value in nums:
            self.add(value)

    def showFirstUnique(self) -> int:
        while self._unique and self._counts[self._unique[0]] > 1:
            self._unique.popleft()
        return self._unique[0] if self._unique else -1

    def add(self, value: int) -> None:
        self._counts[value] = self._counts.get(value, 0) + 1
        if self._counts[value] == 1:
            self._unique.append(value)


def solve(operations: list[str], arguments: list[list[object]]) -> list[object]:
    stream = None
    output: list[object] = []
    for operation, args in zip(operations, arguments):
        if operation == "FirstUnique":
            stream = FirstUnique(args[0])
            output.append(None)
        elif operation == "showFirstUnique":
            assert stream is not None
            output.append(stream.showFirstUnique())
        elif operation == "add":
            assert stream is not None
            stream.add(args[0])
            output.append(None)
        else:
            raise ValueError("unknown operation: " + operation)
    return output
