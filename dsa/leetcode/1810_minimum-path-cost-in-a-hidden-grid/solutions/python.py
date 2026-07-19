from heapq import heappop, heappush


def solve(
    grid: list[list[int]],
    r1: int,
    c1: int,
    r2: int,
    c2: int,
) -> int:
    rows = len(grid)
    columns = len(grid[0])
    target = (r2, c2)
    distances = {(r1, c1): 0}
    heap = [(0, r1, c1)]

    while heap:
        distance, row, column = heappop(heap)
        position = (row, column)
        if distance != distances[position]:
            continue
        if position == target:
            return distance

        for row_delta, column_delta in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            next_row = row + row_delta
            next_column = column + column_delta
            if not (
                0 <= next_row < rows
                and 0 <= next_column < columns
                and grid[next_row][next_column] > 0
            ):
                continue
            neighbor = (next_row, next_column)
            candidate = distance + grid[next_row][next_column]
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                heappush(heap, (candidate, next_row, next_column))

    return -1
