from bisect import bisect_right


def solve(grid: list[list[int]]) -> int:
    low = min(row[0] for row in grid)
    high = max(row[-1] for row in grid)
    target = (len(grid) * len(grid[0])) // 2 + 1

    while low < high:
        middle = (low + high) // 2
        not_greater = sum(
            bisect_right(row, middle)
            for row in grid
        )
        if not_greater < target:
            low = middle + 1
        else:
            high = middle

    return low
