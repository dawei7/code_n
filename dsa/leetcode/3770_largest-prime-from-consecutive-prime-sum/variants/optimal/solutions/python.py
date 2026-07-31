from math import isqrt


def solve(n: int) -> int:
    prime_flags = bytearray([1]) * (n + 1)
    prime_flags[0:2] = bytearray([0, 0])

    limit = isqrt(n)
    for factor in range(2, limit + 1):
        if not prime_flags[factor]:
            continue
        first = factor * factor
        multiples = (n - first) // factor + 1
        prime_flags[first::factor] = bytearray(multiples)

    running_sum = 0
    largest = 0
    for value, is_prime in enumerate(prime_flags):
        if not is_prime:
            continue
        running_sum += value
        if running_sum > n:
            return largest
        if prime_flags[running_sum]:
            largest = running_sum
    return largest
