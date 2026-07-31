def solve(n: int) -> int:
    reversed_digits = []
    value = n
    while value:
        digit = value % 10
        if digit:
            reversed_digits.append(digit)
        value //= 10

    concatenated = 0
    digit_sum = 0
    for digit in reversed(reversed_digits):
        concatenated = concatenated * 10 + digit
        digit_sum += digit
    return concatenated * digit_sum
