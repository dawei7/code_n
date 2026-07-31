"""App-local reference solution for LeetCode 1837."""


def solve(n: int, k: int) -> int:
    digit_sum = 0
    while n > 0:
        n, digit = divmod(n, k)
        digit_sum += digit
    return digit_sum
