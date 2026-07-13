"""Optimal app-local solution for LeetCode 379: Design Phone Directory."""

from collections import deque


def solve(max_numbers: int, operations: list[list]) -> list:
    available = deque(range(max_numbers))
    is_available = [True] * max_numbers
    results: list = []

    for operation in operations:
        name = operation[0]
        if name == "get":
            if not available:
                results.append(-1)
            else:
                number = available.popleft()
                is_available[number] = False
                results.append(number)
        elif name == "check":
            results.append(is_available[operation[1]])
        elif name == "release":
            number = operation[1]
            if not is_available[number]:
                is_available[number] = True
                available.append(number)
        else:
            raise ValueError(f"Unsupported PhoneDirectory operation: {name}")

    return results

