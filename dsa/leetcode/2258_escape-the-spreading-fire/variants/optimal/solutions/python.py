from collections import deque


def solve(grid: list[list[int]]) -> int:
    rows, columns = len(grid), len(grid[0])
    infinity = 10**18
    fire_time = [[infinity] * columns for _ in range(rows)]
    queue = deque()
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                fire_time[row][column] = 0
                queue.append((row, column))

    while queue:
        row, column = queue.popleft()
        for row_step, column_step in directions:
            next_row = row + row_step
            next_column = column + column_step
            if (
                0 <= next_row < rows
                and 0 <= next_column < columns
                and grid[next_row][next_column] != 2
                and fire_time[next_row][next_column] == infinity
            ):
                fire_time[next_row][next_column] = fire_time[row][column] + 1
                queue.append((next_row, next_column))

    def can_escape(wait: int) -> bool:
        if wait >= fire_time[0][0]:
            return False
        person_queue = deque([(0, 0, wait)])
        seen = {(0, 0)}

        while person_queue:
            row, column, time = person_queue.popleft()
            for row_step, column_step in directions:
                next_row = row + row_step
                next_column = column + column_step
                if (
                    not (0 <= next_row < rows and 0 <= next_column < columns)
                    or grid[next_row][next_column] != 0
                    or (next_row, next_column) in seen
                ):
                    continue
                arrival = time + 1
                if (next_row, next_column) == (rows - 1, columns - 1):
                    if arrival <= fire_time[next_row][next_column]:
                        return True
                elif arrival < fire_time[next_row][next_column]:
                    seen.add((next_row, next_column))
                    person_queue.append((next_row, next_column, arrival))
        return False

    if not can_escape(0):
        return -1
    if can_escape(10**9):
        return 10**9

    low, high = 0, 10**9
    while low < high:
        middle = (low + high + 1) // 2
        if can_escape(middle):
            low = middle
        else:
            high = middle - 1
    return low
