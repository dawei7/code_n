from functools import lru_cache


def solve(low: int, high: int) -> int:
    @lru_cache(None)
    def ways(remaining: int, difference: int, next_is_odd: bool) -> int:
        if abs(difference) > 9 * remaining:
            return 0
        if remaining == 0:
            return int(difference == 0)
        return sum(
            ways(
                remaining - 1,
                difference + digit if next_is_odd else difference - digit,
                not next_is_odd,
            )
            for digit in range(10)
        )

    def count_up_to(bound: int) -> int:
        if bound < 10:
            return 0
        digits = [int(char) for char in str(bound)]
        length = len(digits)
        total = sum(ways(size - 1, first, False) for size in range(2, length) for first in range(1, 10))
        difference = 0
        for position, limit in enumerate(digits):
            for digit in range(1 if position == 0 else 0, limit):
                next_difference = difference + digit if position % 2 == 0 else difference - digit
                total += ways(length - position - 1, next_difference, position % 2 == 1)
            difference += limit if position % 2 == 0 else -limit
        return total + int(difference == 0)

    return count_up_to(high) - count_up_to(low - 1)
