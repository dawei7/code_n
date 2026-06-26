"""Optimal solution for string_12: String to Integer (atoi).

Parse a string as a 32-bit signed integer. Skip leading
whitespace, handle an optional +/- sign, read digits
until a non-digit. Clamp to the int32 range.
"""


def solve(s, n):
    if n == 0:
        return 0
    i = 0
    while i < n and s[i] == " ":
        i += 1
    if i == n:
        return 0
    sign = 1
    if s[i] == "+":
        i += 1
    elif s[i] == "-":
        sign = -1
        i += 1
    result = 0
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    while i < n and s[i].isdigit():
        digit = int(s[i])
        new_result = result * 10 + digit
        if sign == 1 and new_result > INT_MAX:
            return INT_MAX
        if sign == -1 and -new_result < INT_MIN:
            return INT_MIN
        result = new_result
        i += 1
    return sign * result
