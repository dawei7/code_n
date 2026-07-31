def solve(
    m: int,
    n: int,
    guards: list[list[int]],
    walls: list[list[int]],
) -> int:
    empty, guard, wall, watched = 0, 1, 2, 3
    grid = [[empty] * n for _ in range(m)]
    for row, column in guards:
        grid[row][column] = guard
    for row, column in walls:
        grid[row][column] = wall

    for row in range(m):
        visible = False
        for column in range(n):
            if grid[row][column] == guard:
                visible = True
            elif grid[row][column] == wall:
                visible = False
            elif visible:
                grid[row][column] = watched
        visible = False
        for column in range(n - 1, -1, -1):
            if grid[row][column] == guard:
                visible = True
            elif grid[row][column] == wall:
                visible = False
            elif visible:
                grid[row][column] = watched

    for column in range(n):
        visible = False
        for row in range(m):
            if grid[row][column] == guard:
                visible = True
            elif grid[row][column] == wall:
                visible = False
            elif visible:
                grid[row][column] = watched
        visible = False
        for row in range(m - 1, -1, -1):
            if grid[row][column] == guard:
                visible = True
            elif grid[row][column] == wall:
                visible = False
            elif visible:
                grid[row][column] = watched

    return sum(cell == empty for row in grid for cell in row)
