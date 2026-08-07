from bisect import bisect_left, bisect_right
from functools import cache
from itertools import combinations


class Solution:
    def countFancy(self, l: int, r: int) -> int:
        def is_good(value: int) -> bool:
            digits = str(value)
            return (
                len(digits) == 1
                or all(digits[index] < digits[index + 1] for index in range(len(digits) - 1))
                or all(digits[index] > digits[index + 1] for index in range(len(digits) - 1))
            )

        good_sums = {value for value in range(1, 145) if is_good(value)}

        good_numbers: set[int] = set()
        increasing_digits = "123456789"
        for length in range(1, len(increasing_digits) + 1):
            for chosen in combinations(increasing_digits, length):
                good_numbers.add(int("".join(chosen)))

        decreasing_digits = "0123456789"
        for length in range(1, len(decreasing_digits) + 1):
            for chosen in combinations(decreasing_digits, length):
                value = int("".join(reversed(chosen)))
                if value:
                    good_numbers.add(value)

        ordered_good = sorted(good_numbers)
        ordered_overlap = sorted(value for value in good_numbers if sum(map(int, str(value))) in good_sums)

        def count_sum_good(bound: int) -> int:
            if bound <= 0:
                return 0

            digits = tuple(map(int, str(bound)))

            @cache
            def digit_dp(index: int, tight: bool, digit_sum: int) -> int:
                if index == len(digits):
                    return int(digit_sum in good_sums)

                limit = digits[index] if tight else 9
                total = 0
                for digit in range(limit + 1):
                    total += digit_dp(
                        index + 1,
                        tight and digit == limit,
                        digit_sum + digit,
                    )
                return total

            return digit_dp(0, True, 0)

        def count_in_range(values: list[int]) -> int:
            return bisect_right(values, r) - bisect_left(values, l)

        return (
            count_sum_good(r) - count_sum_good(l - 1) + count_in_range(ordered_good) - count_in_range(ordered_overlap)
        )
