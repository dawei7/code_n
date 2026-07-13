"""Optimal app-local solution for LeetCode 415: Add Strings."""


def solve(num1: str, num2: str) -> str:
    left = len(num1) - 1
    right = len(num2) - 1
    carry = 0
    reversed_digits: list[str] = []

    while left >= 0 or right >= 0 or carry:
        left_digit = ord(num1[left]) - ord("0") if left >= 0 else 0
        right_digit = ord(num2[right]) - ord("0") if right >= 0 else 0
        total = left_digit + right_digit + carry
        reversed_digits.append(chr(ord("0") + total % 10))
        carry = total // 10
        left -= 1
        right -= 1

    return "".join(reversed(reversed_digits))
