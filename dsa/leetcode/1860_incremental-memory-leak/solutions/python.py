def solve(memory1: int, memory2: int) -> list[int]:
    second = 1

    while max(memory1, memory2) >= second:
        if memory1 >= memory2:
            memory1 -= second
        else:
            memory2 -= second
        second += 1

    return [second, memory1, memory2]
