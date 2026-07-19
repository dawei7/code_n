from collections import deque


def solve(maze: list[list[str]], entrance: list[int]) -> int:
    rows = len(maze)
    columns = len(maze[0])
    start_row, start_column = entrance
    queue = deque([(start_row, start_column, 0)])
    maze[start_row][start_column] = "+"

    while queue:
        row, column, distance = queue.popleft()
        for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = row + row_step
            next_column = column + column_step
            if not (0 <= next_row < rows and 0 <= next_column < columns):
                continue
            if maze[next_row][next_column] != ".":
                continue
            if (
                next_row == 0
                or next_row == rows - 1
                or next_column == 0
                or next_column == columns - 1
            ):
                return distance + 1
            maze[next_row][next_column] = "+"
            queue.append((next_row, next_column, distance + 1))
    return -1
