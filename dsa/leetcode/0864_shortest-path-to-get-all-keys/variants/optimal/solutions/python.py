"""Optimal app-local solution for LeetCode 864."""

from collections import deque


def solve(grid):
    rows = len(grid)
    columns = len(grid[0])
    all_keys = 0
    start = None

    for row in range(rows):
        for column in range(columns):
            cell = grid[row][column]
            if cell == "@":
                start = (row, column)
            elif "a" <= cell <= "f":
                all_keys |= 1 << (ord(cell) - ord("a"))

    queue = deque([(start[0], start[1], 0, 0)])
    visited = {(start[0], start[1], 0)}

    while queue:
        row, column, key_mask, moves = queue.popleft()

        for row_delta, column_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = row + row_delta
            next_column = column + column_delta
            if not (0 <= next_row < rows and 0 <= next_column < columns):
                continue

            cell = grid[next_row][next_column]
            if cell == "#":
                continue
            if "A" <= cell <= "F" and not (
                key_mask & (1 << (ord(cell) - ord("A")))
            ):
                continue

            next_mask = key_mask
            if "a" <= cell <= "f":
                next_mask |= 1 << (ord(cell) - ord("a"))
            if next_mask == all_keys:
                return moves + 1

            state = (next_row, next_column, next_mask)
            if state not in visited:
                visited.add(state)
                queue.append((next_row, next_column, next_mask, moves + 1))

    return -1
