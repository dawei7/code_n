def solve(tasks: list[list[int]]) -> int:
    return min(start + duration for start, duration in tasks)
