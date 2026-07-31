def solve(grid: list[list[int]], x: int) -> int:
    values = sorted(value for row in grid for value in row)
    remainder = values[0] % x
    if any(value % x != remainder for value in values):
        return -1

    median = values[len(values) // 2]
    return sum(abs(value - median) // x for value in values)
