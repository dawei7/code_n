from collections import deque


EMPTY = 2147483647


def solve(rooms: list[list[int]]) -> None:
    if not rooms or not rooms[0]:
        return
    queue = deque(
        (row, column)
        for row in range(len(rooms))
        for column in range(len(rooms[0]))
        if rooms[row][column] == 0
    )
    while queue:
        row, column = queue.popleft()
        for next_row, next_column in (
            (row - 1, column),
            (row + 1, column),
            (row, column - 1),
            (row, column + 1),
        ):
            if (
                0 <= next_row < len(rooms)
                and 0 <= next_column < len(rooms[0])
                and rooms[next_row][next_column] == EMPTY
            ):
                rooms[next_row][next_column] = rooms[row][column] + 1
                queue.append((next_row, next_column))
