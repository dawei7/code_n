from functools import lru_cache


def solve(low: int, high: int) -> int:

    @lru_cache(None)
    def ways(remaining: int, difference: int, next_is_odd: bool) -> int:
        if remaining == 0:
            return int(difference == 0)
        total = 0
        for digit in range(10):
            next_difference = difference + digit if next_is_odd else difference - digit
            total += ways(remaining - 1, next_difference, not next_is_odd)
        return total

    def count_up_to(bound: int) -> int:
        if bound < 10:
            return 0
        digits = [int(char) for char in str(bound)]
        digit_count = len(digits)
        total = 0
        for length in range(2, digit_count):
            for first_digit in range(1, 10):
                total += ways(length - 1, first_digit, False)
        difference = 0
        for position, limit in enumerate(digits):
            first = position == 0
            for digit in range(1 if first else 0, limit):
                next_difference = difference + digit if position % 2 == 0 else difference - digit
                total += ways(digit_count - position - 1, next_difference, position % 2 == 1)
            difference += limit if position % 2 == 0 else -limit
        return total + int(difference == 0)

    return count_up_to(high) - count_up_to(low - 1)
