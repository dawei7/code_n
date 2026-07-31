from math import isqrt


def solve(nums: list[int]) -> int:
    maximum = max(nums)
    limit = max(4, 2 * maximum + 2)
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for prime in range(2, isqrt(limit) + 1):
        if is_prime[prime]:
            start = prime * prime
            count = (limit - start) // prime + 1
            is_prime[start : limit + 1 : prime] = b"\x00" * count
    next_prime = [0] * (maximum + 1)
    nearest = 0
    for value in range(limit, -1, -1):
        if is_prime[value]:
            nearest = value
        if value <= maximum:
            next_prime[value] = nearest
    operations = 0
    for index, value in enumerate(nums):
        if index % 2 == 0:
            operations += next_prime[value] - value
        elif is_prime[value]:
            operations += 2 if value == 2 else 1
    return operations
