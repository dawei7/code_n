from bisect import bisect_left
from itertools import compress
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

    primes = list(compress(range(limit + 1), is_prime))

    operations = 0
    for index, value in enumerate(nums):
        if index % 2 == 0:
            operations += primes[bisect_left(primes, value)] - value
        elif is_prime[value]:
            operations += 2 if value == 2 else 1
    return operations
