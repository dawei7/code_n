def solve(operations: list[str]) -> int:
    return sum(1 if "+" in operation else -1 for operation in operations)
