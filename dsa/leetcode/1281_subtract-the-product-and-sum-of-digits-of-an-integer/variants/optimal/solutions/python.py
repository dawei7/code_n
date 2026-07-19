def solve(n):
    product = 1
    digit_sum = 0

    while n:
        n, digit = divmod(n, 10)
        product *= digit
        digit_sum += digit

    return product - digit_sum
