def solve(n: int) -> list[int]:
    return [value ^ (value >> 1) for value in range(1 << n)]
