def solve(start: int, goal: int) -> int:
    return (start ^ goal).bit_count()
