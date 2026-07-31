from math import isqrt


def solve(s: str) -> int:
    primes: set[int] = set()

    for start in range(len(s)):
        value = 0
        for digit in s[start:]:
            value = value * 10 + int(digit)
            if value > 1 and all(value % divisor for divisor in range(2, isqrt(value) + 1)):
                primes.add(value)

    return sum(sorted(primes)[-3:])
