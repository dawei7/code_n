def solve(grid: list[list[int]], k: int) -> int:
    modulus = 1_000_000_007
    rows = len(grid)
    columns = len(grid[0])
    dp = [[0] * 16 for _ in range(columns)]

    for row in range(rows):
        for column in range(columns):
            value = grid[row][column]
            current = [0] * 16

            if row == 0 and column == 0:
                current[value] = 1
            else:
                for xor_value in range(16):
                    if row > 0:
                        current[xor_value ^ value] += dp[column][xor_value]
                    if column > 0:
                        current[xor_value ^ value] += dp[column - 1][xor_value]

            dp[column] = [count % modulus for count in current]

    return dp[-1][k]
