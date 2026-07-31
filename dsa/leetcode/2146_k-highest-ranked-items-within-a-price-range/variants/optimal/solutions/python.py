from collections import deque


def solve(
    grid: list[list[int]],
    pricing: list[int],
    start: list[int],
    k: int,
) -> list[list[int]]:
    rows = len(grid)
    columns = len(grid[0])
    low, high = pricing
    start_row, start_column = start
    queue = deque([(start_row, start_column, 0)])
    visited = {(start_row, start_column)}
    ranked: list[tuple[int, int, int, int]] = []

    while queue:
        row, column, distance = queue.popleft()
        price = grid[row][column]
        if low <= price <= high:
            ranked.append((distance, price, row, column))

        for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = row + row_step
            next_column = column + column_step
            next_cell = (next_row, next_column)
            if (
                0 <= next_row < rows
                and 0 <= next_column < columns
                and grid[next_row][next_column] != 0
                and next_cell not in visited
            ):
                visited.add(next_cell)
                queue.append((next_row, next_column, distance + 1))

    ranked.sort()
    return [[row, column] for _, _, row, column in ranked[:k]]
