def solve(num1: int, num2: int) -> int:
    total = 0
    for value in range(num1, num2 + 1):
        digits = str(value)
        for index in range(1, len(digits) - 1):
            middle = digits[index]
            if (
                middle > digits[index - 1]
                and middle > digits[index + 1]
                or (middle < digits[index - 1] and middle < digits[index + 1])
            ):
                total += 1
    return total
