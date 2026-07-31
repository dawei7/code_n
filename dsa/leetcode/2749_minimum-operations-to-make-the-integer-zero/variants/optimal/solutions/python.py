def solve(num1: int, num2: int) -> int:
    for operations in range(1, 61):
        remaining = num1 - operations * num2
        if remaining >= operations and remaining.bit_count() <= operations:
            return operations

    return -1
