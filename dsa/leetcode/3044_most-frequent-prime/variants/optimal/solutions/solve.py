from collections import Counter


def solve(mat: list[list[int]]) -> int:
    rows = len(mat)
    columns = len(mat[0])
    directions = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )
    prime_cache: dict[int, bool] = {}

    def is_prime(value: int) -> bool:
        if value in prime_cache:
            return prime_cache[value]

        if value < 2:
            result = False
        elif value == 2:
            result = True
        elif value % 2 == 0:
            result = False
        else:
            result = True
            divisor = 3
            while divisor * divisor <= value:
                if value % divisor == 0:
                    result = False
                    break
                divisor += 2

        prime_cache[value] = result
        return result

    frequencies = Counter()

    for start_row in range(rows):
        for start_column in range(columns):
            for row_step, column_step in directions:
                row = start_row
                column = start_column
                value = 0

                while 0 <= row < rows and 0 <= column < columns:
                    value = value * 10 + mat[row][column]
                    if value > 10 and is_prime(value):
                        frequencies[value] += 1

                    row += row_step
                    column += column_step

    if not frequencies:
        return -1

    return max(frequencies, key=lambda value: (frequencies[value], value))
