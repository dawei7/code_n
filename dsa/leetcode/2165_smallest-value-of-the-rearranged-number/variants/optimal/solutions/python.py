def solve(num: int) -> int:
    if num == 0:
        return 0

    digits = sorted(str(abs(num)), reverse=num < 0)
    if num < 0:
        return -int("".join(digits))

    first_nonzero = next(
        index for index, digit in enumerate(digits) if digit != "0"
    )
    digits[0], digits[first_nonzero] = digits[first_nonzero], digits[0]
    return int("".join(digits))
