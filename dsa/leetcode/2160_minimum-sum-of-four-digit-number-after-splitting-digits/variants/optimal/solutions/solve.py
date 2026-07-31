def solve(num: int) -> int:
    digits = sorted(int(digit) for digit in str(num))
    return 10 * (digits[0] + digits[1]) + digits[2] + digits[3]
