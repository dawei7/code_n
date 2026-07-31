from math import isqrt


def solve(n: int) -> int:
    reversed_n = int(str(n)[::-1])
    lower = min(n, reversed_n)
    upper = max(n, reversed_n)

    is_prime = [True] * (upper + 1)
    is_prime[0] = False
    if upper >= 1:
        is_prime[1] = False

    for prime in range(2, isqrt(upper) + 1):
        if is_prime[prime]:
            for multiple in range(prime * prime, upper + 1, prime):
                is_prime[multiple] = False

    return sum(value for value in range(lower, upper + 1) if is_prime[value])
