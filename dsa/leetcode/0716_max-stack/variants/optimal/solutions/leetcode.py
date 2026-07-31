import heapq


class _Node:
    def __init__(self, value: int = 0, identifier: int = 0):
        self.value = value
        self.identifier = identifier
        self.previous = None
        self.next = None


class MaxStack:
    def __init__(self):
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.previous = self.head
        self.maximums = []
        self.active = {}
        self.next_identifier = 0

    def _append(self, node: _Node) -> None:
        previous = self.tail.previous
        previous.next = node
        node.previous = previous
        node.next = self.tail
        self.tail.previous = node

    @staticmethod
    def _unlink(node: _Node) -> None:
        node.previous.next = node.next
        node.next.previous = node.previous

    def _discard_stale_maximums(self) -> None:
        while self.maximums and -self.maximums[0][1] not in self.active:
            heapq.heappop(self.maximums)

    def push(self, x: int) -> None:
        self.next_identifier += 1
        identifier = self.next_identifier
        node = _Node(x, identifier)
        self._append(node)
        self.active[identifier] = node
        heapq.heappush(self.maximums, (-x, -identifier))

    def pop(self) -> int:
        node = self.tail.previous
        self._unlink(node)
        del self.active[node.identifier]
        return node.value

    def top(self) -> int:
        return self.tail.previous.value

    def peekMax(self) -> int:
        self._discard_stale_maximums()
        return -self.maximums[0][0]

    def popMax(self) -> int:
        self._discard_stale_maximums()
        negative_value, negative_identifier = heapq.heappop(self.maximums)
        identifier = -negative_identifier
        node = self.active.pop(identifier)
        self._unlink(node)
        return -negative_value
