import heapq


def solve(grid: list[list[int]]) -> int:
    side = len(grid)
    frontier = [(grid[0][0], 0, 0)]
    visited = {(0, 0)}
    water_level = 0

    while frontier:
        elevation, row, column = heapq.heappop(frontier)
        water_level = max(water_level, elevation)
        if row == side - 1 and column == side - 1:
            return water_level

        for row_delta, column_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = row + row_delta
            next_column = column + column_delta
            if (
                0 <= next_row < side
                and 0 <= next_column < side
                and (next_row, next_column) not in visited
            ):
                visited.add((next_row, next_column))
                heapq.heappush(
                    frontier,
                    (grid[next_row][next_column], next_row, next_column),
                )

    raise ValueError("the destination must be reachable")
