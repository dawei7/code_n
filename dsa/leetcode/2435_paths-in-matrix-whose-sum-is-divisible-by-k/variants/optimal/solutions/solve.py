def solve(grid: list[list[int]], k: int) -> int:
    modulus = 1_000_000_007
    columns = len(grid[0])
    ways = [[0] * k for _ in range(columns)]

    for row in range(len(grid)):
        for column in range(columns):
            value = grid[row][column] % k
            current = [0] * k
            if row == 0 and column == 0:
                current[value] = 1
            else:
                for remainder in range(k):
                    count = ways[column][remainder] if row else 0
                    if column:
                        count += ways[column - 1][remainder]
                    current[(remainder + value) % k] = count % modulus
            ways[column] = current

    return ways[-1][0]
