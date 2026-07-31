from math import isqrt


def solve(nums: list[int]) -> int:
    length = len(nums)
    is_prime = bytearray(b"\x01") * length
    is_prime[0] = 0
    if length > 1:
        is_prime[1] = 0

    for value in range(2, isqrt(length - 1) + 1):
        if is_prime[value]:
            start = value * value
            count = (length - 1 - start) // value + 1
            is_prime[start:length:value] = b"\x00" * count

    prime_sum = sum(number for index, number in enumerate(nums) if is_prime[index])
    return abs(2 * prime_sum - sum(nums))
