class _Node:
    def __init__(self, value: int = 0):
        self.value = value
        self.previous = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.previous = self.head
        self.size = 0

    def _node_at(self, index: int) -> _Node:
        if index < self.size // 2:
            current = self.head.next
            for _ in range(index):
                current = current.next
            return current

        current = self.tail.previous
        for _ in range(self.size - 1, index, -1):
            current = current.previous
        return current

    def _insert_between(self, value: int, previous: _Node, following: _Node) -> None:
        node = _Node(value)
        node.previous = previous
        node.next = following
        previous.next = node
        following.previous = node
        self.size += 1

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        return self._node_at(index).value

    def addAtHead(self, val: int) -> None:
        self._insert_between(val, self.head, self.head.next)

    def addAtTail(self, val: int) -> None:
        self._insert_between(val, self.tail.previous, self.tail)

    def addAtIndex(self, index: int, val: int) -> None:
        index = max(index, 0)
        if index > self.size:
            return
        following = self.tail if index == self.size else self._node_at(index)
        self._insert_between(val, following.previous, following)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        node = self._node_at(index)
        node.previous.next = node.next
        node.next.previous = node.previous
        self.size -= 1
