from collections import Counter, defaultdict
from math import isqrt


def solve(nums: list[int]) -> int:
    frequency = Counter(nums)
    if len(frequency) == 1:
        return 0

    limit = isqrt(max(nums))
    is_prime = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        is_prime[0] = 0
    if limit >= 1:
        is_prime[1] = 0

    for value in range(2, isqrt(limit) + 1):
        if is_prime[value]:
            start = value * value
            is_prime[start : limit + 1 : value] = b"\x00" * (
                (limit - start) // value + 1
            )

    primes = [value for value in range(2, limit + 1) if is_prime[value]]
    multiples = defaultdict(int)
    divisors_present = {}

    for value, count in frequency.items():
        if value == 1:
            continue

        remaining = value
        factorization = []
        for prime in primes:
            if prime * prime > remaining:
                break
            if remaining % prime != 0:
                continue

            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            factorization.append((prime, exponent))

        if remaining > 1:
            factorization.append((remaining, 1))

        divisors = [1]
        for prime, exponent in factorization:
            previous = divisors[:]
            power = 1
            for _ in range(exponent):
                power *= prime
                divisors.extend(divisor * power for divisor in previous)

        divisors_present[value] = sum(frequency.get(divisor, 0) for divisor in divisors)
        for divisor in divisors:
            if divisor in frequency and divisor > 1:
                multiples[divisor] += count

    n = len(nums)
    answer = n
    for target in frequency:
        if target > 1:
            cost = 2 * n - multiples[target] - divisors_present[target]
            answer = min(answer, cost)

    return answer
