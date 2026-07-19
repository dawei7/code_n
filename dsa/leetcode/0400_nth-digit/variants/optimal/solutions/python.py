"""Optimal app-local solution for LeetCode 400: Nth Digit."""


def solve(n: int) -> int:
    digits = 1
    count = 9
    start = 1

    while n > digits * count:
        n -= digits * count
        digits += 1
        count *= 10
        start *= 10

    offset = n - 1
    number = start + offset // digits
    index = offset % digits
    return number // (10 ** (digits - 1 - index)) % 10
