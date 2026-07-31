def solve(n: int) -> int:
    digits = list(str(n))
    suffix_start = len(digits)

    for index in range(len(digits) - 1, 0, -1):
        if digits[index - 1] > digits[index]:
            digits[index - 1] = str(int(digits[index - 1]) - 1)
            suffix_start = index

    for index in range(suffix_start, len(digits)):
        digits[index] = "9"

    return int("".join(digits))
