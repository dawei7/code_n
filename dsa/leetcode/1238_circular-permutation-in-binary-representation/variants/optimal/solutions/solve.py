def solve(n: int, start: int) -> list[int]:
    return [(index ^ (index >> 1)) ^ start for index in range(1 << n)]
