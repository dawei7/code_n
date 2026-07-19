class MinStack:
    def __init__(self):
        self.values: list[tuple[int, int]] = []

    def push(self, value: int) -> None:
        minimum = value if not self.values else min(value, self.values[-1][1])
        self.values.append((value, minimum))

    def pop(self) -> None:
        self.values.pop()

    def top(self) -> int:
        return self.values[-1][0]

    def getMin(self) -> int:
        return self.values[-1][1]


def solve(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    stack: MinStack | None = None
    output: list[int | None] = []
    for operation, args in zip(operations, arguments):
        if operation == "MinStack":
            stack = MinStack()
            output.append(None)
        elif operation == "push":
            assert stack is not None
            stack.push(args[0])
            output.append(None)
        elif operation == "pop":
            assert stack is not None
            stack.pop()
            output.append(None)
        elif operation == "top":
            assert stack is not None
            output.append(stack.top())
        elif operation == "getMin":
            assert stack is not None
            output.append(stack.getMin())
        else:
            raise ValueError(f"unknown operation: {operation}")
    return output
