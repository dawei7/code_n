from collections import deque


class FrontMiddleBackQueue:
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def _rebalance(self) -> None:
        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        elif len(self.left) < len(self.right):
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self._rebalance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self._rebalance()

    def popFront(self) -> int:
        if not self.left:
            return -1
        value = self.left.popleft()
        self._rebalance()
        return value

    def popMiddle(self) -> int:
        if not self.left:
            return -1
        value = self.left.pop()
        self._rebalance()
        return value

    def popBack(self) -> int:
        if self.right:
            value = self.right.pop()
        elif self.left:
            value = self.left.pop()
        else:
            return -1
        self._rebalance()
        return value


def solve(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    queue = None
    output: list[int | None] = []

    for operation, values in zip(operations, arguments, strict=True):
        if operation == "FrontMiddleBackQueue":
            queue = FrontMiddleBackQueue()
            output.append(None)
            continue
        if queue is None:
            raise ValueError("FrontMiddleBackQueue must be constructed first")
        if operation.startswith("push"):
            getattr(queue, operation)(values[0])
            output.append(None)
        else:
            output.append(getattr(queue, operation)())

    return output
