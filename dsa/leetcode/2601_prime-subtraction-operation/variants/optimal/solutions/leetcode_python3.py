from bisect import bisect_left
from math import isqrt


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        maximum = max(nums)
        is_prime = [True] * (maximum + 1)
        is_prime[0] = False
        if maximum >= 1:
            is_prime[1] = False

        for prime in range(2, isqrt(maximum) + 1):
            if is_prime[prime]:
                for multiple in range(prime * prime, maximum + 1, prime):
                    is_prime[multiple] = False

        primes = [number for number in range(2, maximum + 1) if is_prime[number]]
        previous = 0

        for number in nums:
            prime_index = bisect_left(primes, number - previous) - 1
            if prime_index >= 0:
                number -= primes[prime_index]
            if number <= previous:
                return False
            previous = number

        return True
