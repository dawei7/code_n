def solve(n: int) -> bool:
    original = n
    digit_sum = 0
    digit_product = 1

    while n:
        n, digit = divmod(n, 10)
        digit_sum += digit
        digit_product *= digit

    return original % (digit_sum + digit_product) == 0
