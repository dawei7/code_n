def solve(matrix):
    columns = len(matrix[0])
    dp = [0] * (columns + 1)
    total = 0

    for row in matrix:
        above_left = 0
        for column, value in enumerate(row, start=1):
            above = dp[column]
            if value == 1:
                dp[column] = 1 + min(above, dp[column - 1], above_left)
                total += dp[column]
            else:
                dp[column] = 0
            above_left = above

    return total
