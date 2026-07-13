def solve(dungeon: list[list[int]]) -> int:
    columns = len(dungeon[0])
    required = [float("inf")] * (columns + 1)
    required[columns - 1] = 1

    for row in range(len(dungeon) - 1, -1, -1):
        for column in range(columns - 1, -1, -1):
            next_required = min(required[column], required[column + 1])
            required[column] = max(1, int(next_required) - dungeon[row][column])
    return int(required[0])
