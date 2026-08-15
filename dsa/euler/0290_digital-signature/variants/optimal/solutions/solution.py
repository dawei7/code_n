"""Project Euler 290: Digital Signature

Find the number of integers 0 <= n < 10^18 such that sum_digits(137 * n) == sum_digits(n).
"""

from __future__ import annotations


def solve(num_digits: int = 18, multiplier: int = 137) -> str:
    """Calculates the number of integers 0 <= n < 10^num_digits where

    digit_sum(multiplier * n) == digit_sum(n) using Digit Dynamic Programming with carry tracking.

    We generate n digit-by-digit from least significant to most significant:
      At step i (digit d in 0..9):
        val = multiplier * d + carry
        out_digit = val % 10
        next_carry = val // 10
        next_diff = diff + (out_digit - d)

    At step num_digits, the remaining carry is flushed into higher decimal digits,
    and a state is valid iff diff + digit_sum(carry) == 0.
    """

    def digit_sum(x: int) -> int:
        s = 0
        while x > 0:
            s += x % 10
            x //= 10
        return s

    # dp[(carry, diff)] = count
    dp: dict[tuple[int, int], int] = {(0, 0): 1}

    for _ in range(num_digits):
        next_dp: dict[tuple[int, int], int] = {}
        for (carry, diff), count in dp.items():
            for d in range(10):
                val = multiplier * d + carry
                out_d = val % 10
                next_c = val // 10
                next_diff = diff + (out_d - d)
                k = (next_c, next_diff)
                next_dp[k] = next_dp.get(k, 0) + count
        dp = next_dp

    total_valid = 0
    for (carry, diff), count in dp.items():
        if diff + digit_sum(carry) == 0:
            total_valid += count

    return str(total_valid)


if __name__ == "__main__":
    print(solve())
