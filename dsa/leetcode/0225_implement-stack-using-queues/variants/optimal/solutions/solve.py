from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


def solve(operations: list[list]) -> list:
    stack = MyStack()
    results = []
    for operation in operations:
        name = operation[0]
        if name == "push":
            stack.push(operation[1])
        elif name == "pop":
            results.append(stack.pop())
        elif name == "top":
            results.append(stack.top())
        else:
            results.append(stack.empty())
    return results
