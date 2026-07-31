def solve(n: int, t: int) -> int:
    for candidate in range(n, n + 10):
        digit_product = 1
        value = candidate

        while value:
            digit_product *= value % 10
            value //= 10

        if digit_product % t == 0:
            return candidate

    raise AssertionError("a multiple of ten must appear within ten candidates")
