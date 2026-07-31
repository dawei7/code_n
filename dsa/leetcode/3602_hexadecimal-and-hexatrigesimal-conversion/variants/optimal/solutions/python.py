"""Optimal app-local solution for LeetCode 3602."""


def solve(n):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def convert(value, base):
        encoded = []
        while value:
            value, remainder = divmod(value, base)
            encoded.append(digits[remainder])
        return "".join(reversed(encoded)) or "0"

    square = n * n
    return convert(square, 16) + convert(square * n, 36)
