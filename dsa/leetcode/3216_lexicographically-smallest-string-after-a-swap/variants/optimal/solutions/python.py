def solve(s: str) -> str:
    digits = list(s)
    for index in range(len(digits) - 1):
        if (
            int(digits[index]) % 2 == int(digits[index + 1]) % 2
            and digits[index] > digits[index + 1]
        ):
            digits[index], digits[index + 1] = digits[index + 1], digits[index]
            break
    return "".join(digits)
