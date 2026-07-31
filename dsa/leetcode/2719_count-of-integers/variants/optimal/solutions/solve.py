from functools import cache


def solve(num1: str, num2: str, min_sum: int, max_sum: int) -> int:
    modulus = 1_000_000_007

    def count_up_to(bound: str) -> int:
        @cache
        def dp(position: int, digit_sum: int, tight: bool) -> int:
            if digit_sum > max_sum:
                return 0
            if position == len(bound):
                return int(digit_sum >= min_sum)

            limit = int(bound[position]) if tight else 9
            total = 0
            for digit in range(limit + 1):
                total += dp(
                    position + 1,
                    digit_sum + digit,
                    tight and digit == limit,
                )
            return total % modulus

        return dp(0, 0, True)

    lower_is_valid = min_sum <= sum(map(int, num1)) <= max_sum
    return (count_up_to(num2) - count_up_to(num1) + lower_is_valid) % modulus
