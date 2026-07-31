def solve(n: int, time: int) -> int:
    traversals, offset = divmod(time, n - 1)
    if traversals % 2 == 0:
        return offset + 1
    return n - offset
