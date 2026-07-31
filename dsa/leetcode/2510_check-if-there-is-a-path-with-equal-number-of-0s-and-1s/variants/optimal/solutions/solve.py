def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    path_length = rows + cols - 1
    if path_length % 2:
        return False

    target = path_length // 2
    reachable = [set() for _ in range(cols)]

    for row in range(rows):
        for col in range(cols):
            previous = set()
            if row > 0:
                previous.update(reachable[col])
            if col > 0:
                previous.update(reachable[col - 1])
            if row == 0 and col == 0:
                previous.add(0)

            value = grid[row][col]
            reachable[col] = {ones + value for ones in previous if ones + value <= target}

    return target in reachable[-1]
