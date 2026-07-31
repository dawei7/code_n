from array import array
from math import isqrt


def solve(nums: list[int]) -> int:
    if len(nums) < 2:
        return -1

    limit = max(nums)
    smallest = array("I", range(limit + 1))
    for prime in range(2, isqrt(limit) + 1):
        if smallest[prime] == prime:
            start = prime * prime
            count = (limit - start) // prime + 1
            smallest[start::prime] = array("I", [prime]) * count

    def prime_factors(value):
        while value > 1:
            prime = smallest[value]
            yield prime
            while value % prime == 0:
                value //= prime

    last = {}
    for index, value in enumerate(nums):
        for prime in prime_factors(value):
            last[prime] = index

    rightmost = 0
    for index in range(len(nums) - 1):
        for prime in prime_factors(nums[index]):
            rightmost = max(rightmost, last[prime])
        if rightmost == index:
            return index

    return -1
