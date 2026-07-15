"""Optimal app-local solution for LeetCode 866."""


def solve(n):
    for small_prime_palindrome in (2, 3, 5, 7, 11):
        if n <= small_prime_palindrome:
            return small_prime_palindrome

    digit_count = 0
    remaining = n
    while remaining:
        digit_count += 1
        remaining //= 10

    if digit_count % 2 == 0:
        prefix = 10 ** (digit_count // 2)
    else:
        prefix = n // (10 ** (digit_count // 2))

    while True:
        candidate = prefix
        tail = prefix // 10
        while tail:
            candidate = candidate * 10 + tail % 10
            tail //= 10

        if candidate >= n and _is_prime(candidate):
            return candidate
        prefix += 1


def _is_prime(value):
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2

    factor = 3
    while factor * factor <= value:
        if value % factor == 0:
            return False
        factor += 2
    return True
