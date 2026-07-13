class MyCircularDeque:
    def __init__(self, k: int):
        self._values = [0] * k
        self._capacity = k
        self._front = 0
        self._size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self._front = (self._front - 1) % self._capacity
        self._values[self._front] = value
        self._size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        index = (self._front + self._size) % self._capacity
        self._values[index] = value
        self._size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self._size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self._values[self._front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self._values[(self._front + self._size - 1) % self._capacity]

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size == self._capacity


def solve(operations: list[str], arguments: list[list[int]]) -> list:
    deque: MyCircularDeque | None = None
    output = []
    for operation, args in zip(operations, arguments):
        if operation == "MyCircularDeque":
            deque = MyCircularDeque(*args)
            output.append(None)
        else:
            output.append(getattr(deque, operation)(*args))
    return output
