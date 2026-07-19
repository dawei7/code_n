"""Optimal app-local solution for LeetCode 405."""


def solve(num: int) -> str:
    if num == 0:
        return "0"

    digits = "0123456789abcdef"
    value = num & 0xFFFFFFFF
    result: list[str] = []

    while value:
        result.append(digits[value & 0xF])
        value >>= 4

    return "".join(reversed(result))
