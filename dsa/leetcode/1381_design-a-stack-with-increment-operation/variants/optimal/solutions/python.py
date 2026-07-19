"""Reference solution for LeetCode 1381."""


class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.values: list[int] = []
        self.increments: list[int] = []

    def push(self, x: int) -> None:
        if len(self.values) < self.max_size:
            self.values.append(x)
            self.increments.append(0)

    def pop(self) -> int:
        if not self.values:
            return -1

        index = len(self.values) - 1
        increment = self.increments.pop()
        if index > 0:
            self.increments[index - 1] += increment
        return self.values.pop() + increment

    def increment(self, k: int, val: int) -> None:
        if self.values:
            index = min(k, len(self.values)) - 1
            self.increments[index] += val


def solve(
    max_size: int,
    operations: list[tuple[str, tuple[int, ...]]],
) -> list[int | None]:
    stack = CustomStack(max_size)
    outputs: list[int | None] = []

    for operation, args in operations:
        if operation == "push":
            outputs.append(stack.push(args[0]))
        elif operation == "pop":
            outputs.append(stack.pop())
        elif operation == "increment":
            outputs.append(stack.increment(args[0], args[1]))
        else:
            raise ValueError(f"unknown operation: {operation}")

    return outputs
