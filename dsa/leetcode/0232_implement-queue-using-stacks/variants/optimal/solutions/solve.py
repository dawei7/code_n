class MyQueue:
    def __init__(self):
        self.incoming = []
        self.outgoing = []

    def push(self, x: int) -> None:
        self.incoming.append(x)

    def _prepare_front(self) -> None:
        if not self.outgoing:
            while self.incoming:
                self.outgoing.append(self.incoming.pop())

    def pop(self) -> int:
        self._prepare_front()
        return self.outgoing.pop()

    def peek(self) -> int:
        self._prepare_front()
        return self.outgoing[-1]

    def empty(self) -> bool:
        return not self.incoming and not self.outgoing


def solve(operations: list[str], values: list[int | None]) -> list[object]:
    queue = MyQueue()
    results: list[object] = []
    for operation, value in zip(operations, values):
        if operation == "push":
            queue.push(int(value))
            results.append(None)
        elif operation == "pop":
            results.append(queue.pop())
        elif operation == "peek":
            results.append(queue.peek())
        else:
            results.append(queue.empty())
    return results
