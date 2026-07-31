def solve(grid: list[list[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])
    best = [0] * 10

    for column in range(columns):
        frequency = [0] * 10
        for row in range(rows):
            frequency[grid[row][column]] += 1

        next_best = [0] * 10
        for digit in range(10):
            next_best[digit] = frequency[digit] + max(
                best[other]
                for other in range(10)
                if other != digit
            )
        best = next_best

    return rows * columns - max(best)
