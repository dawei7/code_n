"""Optimal app-local solution for LeetCode 359: Logger Rate Limiter."""


def solve(operations: list[list]) -> list[bool]:
    next_allowed: dict[str, int] = {}
    results: list[bool] = []

    for operation in operations:
        if operation[0] != "shouldPrintMessage":
            raise ValueError(f"Unsupported Logger operation: {operation[0]}")

        timestamp = operation[1]
        message = operation[2]
        if timestamp < next_allowed.get(message, timestamp):
            results.append(False)
            continue

        next_allowed[message] = timestamp + 10
        results.append(True)

    return results

