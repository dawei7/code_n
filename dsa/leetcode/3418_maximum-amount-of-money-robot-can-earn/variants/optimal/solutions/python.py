def solve(coins: list[list[int]]) -> int:
    negative_infinity = -10**18
    rows = len(coins)
    columns = len(coins[0])
    dp = [[negative_infinity] * 3 for _ in range(columns)]

    for row in range(rows):
        for column in range(columns):
            if row == 0 and column == 0:
                incoming = [0, negative_infinity, negative_infinity]
            else:
                incoming = [
                    max(
                        dp[column][used],
                        dp[column - 1][used]
                        if column > 0
                        else negative_infinity,
                    )
                    for used in range(3)
                ]

            value = coins[row][column]
            current = [score + value for score in incoming]
            if value < 0:
                for used in range(2):
                    current[used + 1] = max(current[used + 1], incoming[used])

            dp[column] = current

    return max(dp[-1])
