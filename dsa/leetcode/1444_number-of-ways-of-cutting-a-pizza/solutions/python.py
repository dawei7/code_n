from functools import lru_cache


MODULO = 1_000_000_007


def solve(pizza, k):
    rows = len(pizza)
    columns = len(pizza[0])

    suffix_apples = [[0] * (columns + 1) for _ in range(rows + 1)]
    for row in range(rows - 1, -1, -1):
        for column in range(columns - 1, -1, -1):
            suffix_apples[row][column] = (
                int(pizza[row][column] == "A")
                + suffix_apples[row + 1][column]
                + suffix_apples[row][column + 1]
                - suffix_apples[row + 1][column + 1]
            )

    @lru_cache(None)
    def count_ways(row, column, pieces):
        if suffix_apples[row][column] < pieces:
            return 0
        if pieces == 1:
            return 1

        ways = 0
        for next_row in range(row + 1, rows):
            if suffix_apples[row][column] > suffix_apples[next_row][column]:
                ways += count_ways(next_row, column, pieces - 1)

        for next_column in range(column + 1, columns):
            if suffix_apples[row][column] > suffix_apples[row][next_column]:
                ways += count_ways(row, next_column, pieces - 1)

        return ways % MODULO

    return count_ways(0, 0, k)
