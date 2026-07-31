from functools import cache


def solve(l: int, r: int, directions: str) -> int:
    path_positions = {0}
    row = 0
    column = 0

    for direction in directions:
        if direction == "D":
            row += 1
        else:
            column += 1
        path_positions.add(row * 4 + column)

    def count_at_most(limit: int) -> int:
        if limit < 0:
            return 0

        digits = [int(digit) for digit in f"{limit:016d}"]

        @cache
        def count(
            position: int, tight: bool, previous_path_digit: int
        ) -> int:
            if position == 16:
                return 1

            upper = digits[position] if tight else 9
            total = 0
            first_digit = (
                previous_path_digit if position in path_positions else 0
            )

            for digit in range(first_digit, upper + 1):
                next_previous = (
                    digit
                    if position in path_positions
                    else previous_path_digit
                )
                total += count(
                    position + 1,
                    tight and digit == digits[position],
                    next_previous,
                )

            return total

        return count(0, True, 0)

    return count_at_most(r) - count_at_most(l - 1)
