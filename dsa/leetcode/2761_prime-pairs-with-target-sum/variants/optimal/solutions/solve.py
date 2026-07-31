from math import isqrt


def solve(n):
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[:2] = b"\x00\x00"

    for candidate in range(2, isqrt(n) + 1):
        if is_prime[candidate]:
            start = candidate * candidate
            count = (n - start) // candidate + 1
            is_prime[start : n + 1 : candidate] = b"\x00" * count

    return [[first, n - first] for first in range(2, n // 2 + 1) if is_prime[first] and is_prime[n - first]]
