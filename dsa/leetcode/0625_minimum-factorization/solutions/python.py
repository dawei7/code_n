INT_MAX = 2**31 - 1


def solve(a: int) -> int:
    if a < 10:
        return a

    remaining = a
    result = 0
    place = 1
    for digit in range(9, 1, -1):
        while remaining % digit == 0:
            remaining //= digit
            result += digit * place
            place *= 10

    if remaining != 1 or result > INT_MAX:
        return 0
    return result
