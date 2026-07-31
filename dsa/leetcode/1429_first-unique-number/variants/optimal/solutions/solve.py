from collections import deque


class FirstUnique:
    def __init__(self, nums):
        self.counts = {}
        self.unique = deque()
        for value in nums:
            self.add(value)

    def showFirstUnique(self):
        while self.unique and self.counts[self.unique[0]] > 1:
            self.unique.popleft()
        return self.unique[0] if self.unique else -1

    def add(self, value):
        self.counts[value] = self.counts.get(value, 0) + 1
        if self.counts[value] == 1:
            self.unique.append(value)


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
