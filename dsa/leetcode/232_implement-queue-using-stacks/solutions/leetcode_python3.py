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
