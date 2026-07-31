def solve(num: int) -> int:
    digit_sum = 0
    value = num
    while value:
        digit_sum += value % 10
        value //= 10
    return (num - digit_sum % 2) // 2
