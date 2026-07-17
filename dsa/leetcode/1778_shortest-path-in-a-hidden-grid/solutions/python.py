from collections import deque


def solve(grid: list[list[int]]) -> int:
    start = target = (-1, -1)
    for row, values in enumerate(grid):
        for column, value in enumerate(values):
            if value == -1:
                start = (row, column)
            elif value == 2:
                target = (row, column)

    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        (row, column), distance = queue.popleft()
        if (row, column) == target:
            return distance
        for row_delta, column_delta in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            neighbor = (row + row_delta, column + column_delta)
            next_row, next_column = neighbor
            if (
                0 <= next_row < len(grid)
                and 0 <= next_column < len(grid[0])
                and grid[next_row][next_column] != 0
                and neighbor not in seen
            ):
                seen.add(neighbor)
                queue.append((neighbor, distance + 1))
    return -1
