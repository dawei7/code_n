"""Optimal solution for LeetCode 1381: Design a Stack With Increment Operation."""


def solve(max_size: int, operations: list[tuple[str, tuple[int, ...]]]) -> list[int | None]:
    stack: list[int] = []
    increments: list[int] = []
    outputs: list[int | None] = []

    for op, args in operations:
        if op == "push":
            if len(stack) < max_size:
                stack.append(args[0])
                increments.append(0)
            outputs.append(None)
        elif op == "pop":
            if not stack:
                outputs.append(-1)
                continue
            index = len(stack) - 1
            inc = increments.pop()
            if index > 0:
                increments[index - 1] += inc
            outputs.append(stack.pop() + inc)
        elif op == "increment":
            if stack:
                index = min(args[0], len(stack)) - 1
                increments[index] += args[1]
            outputs.append(None)
        else:
            raise ValueError(f"unknown operation: {op}")
    return outputs
