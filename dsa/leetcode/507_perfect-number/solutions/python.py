"""Complementary-divisor scan for LeetCode 507."""


def solve(num: int) -> bool:
    if num <= 1:
        return False

    divisor_sum = 1
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            divisor_sum += divisor
            complement = num // divisor
            if complement != divisor:
                divisor_sum += complement
        divisor += 1
    return divisor_sum == num
