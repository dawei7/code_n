def solve(n: int) -> int:
    concatenated = 0
    digit_sum = 0
    for character in str(n):
        digit = int(character)
        if digit != 0:
            concatenated = concatenated * 10 + digit
            digit_sum += digit
    return concatenated * digit_sum
