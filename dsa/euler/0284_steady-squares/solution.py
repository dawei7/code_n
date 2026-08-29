"""Project Euler 284: Steady Squares

Find the sum of the digits of all the n-digit steady squares in the base 14
numbering system for 1 <= n <= 10000 (decimal), expressed in base 14.
"""

from __future__ import annotations


def solve(max_n: int = 10000, base: int = 14) -> str:
    """Calculates the sum of digits of all base-14 steady squares for 1 <= n <= max_n.

    In base B = 14 = 2 * 7, an n-digit steady square satisfies x^2 = x (mod 14^n).
    By the Chinese Remainder Theorem on coprime factors 2^n and 7^n, there are 4 solutions:
      1. x = 0 (leading zero, invalid)
      2. x = 1 (valid only for n = 1)
      3. x_1 = 7^n * (7^n)^(-1) mod 14^n (with x_1 = 0 mod 2^n, x_1 = 1 mod 7^n)
      4. x_2 = 14^n + 1 - x_1 (with x_2 = 1 mod 2^n, x_2 = 0 mod 7^n)

    Both x_1 and x_2 are fixed infinite sequences in base 14 extending leftwards.
    An n-digit prefix is a valid n-digit steady square iff its n-th digit is non-zero.
    """
    mod = base**max_n
    mod2 = 2**max_n
    mod7 = 7**max_n

    inv_7 = pow(mod7, -1, mod2)
    x1 = (mod7 * inv_7) % mod
    x2 = (mod + 1 - x1) % mod

    digits1: list[int] = []
    temp1 = x1
    digits2: list[int] = []
    temp2 = x2
    for _ in range(max_n):
        digits1.append(temp1 % base)
        temp1 //= base
        digits2.append(temp2 % base)
        temp2 //= base

    # Digit sum accumulator (includes 1 for 1-digit solution x = 1)
    total_digit_sum = 1

    cur_sum1 = 0
    cur_sum2 = 0
    for n in range(1, max_n + 1):
        d1 = digits1[n - 1]
        d2 = digits2[n - 1]
        cur_sum1 += d1
        cur_sum2 += d2
        if d1 != 0:
            total_digit_sum += cur_sum1
        if d2 != 0:
            total_digit_sum += cur_sum2

    # Convert total decimal digit sum to base 14 representation
    digits_chars = "0123456789abcd"
    res: list[str] = []
    temp_sum = total_digit_sum
    while temp_sum > 0:
        res.append(digits_chars[temp_sum % base])
        temp_sum //= base

    return "".join(reversed(res))


if __name__ == "__main__":
    print(solve())
