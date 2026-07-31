from collections import Counter, deque
from itertools import compress, repeat
from math import isqrt
from operator import setitem


def solve(nums: list[int], maxVal: int) -> int:
    limit = max(maxVal, max(nums))
    counts = Counter(nums)
    frequency = [0] * (limit + 1)
    deque(
        map(setitem, repeat(frequency), counts.keys(), counts.values()),
        maxlen=0,
    )

    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[:2] = b"\x00\x00"
    for prime in range(2, isqrt(limit) + 1):
        if is_prime[prime]:
            start = prime * prime
            is_prime[start::prime] = b"\x00" * ((limit - start) // prime + 1)

    primes = list(compress(range(limit + 1), is_prime))
    smallest_prime = list(range(limit + 1))
    for prime in reversed(primes):
        smallest_prime[prime::prime] = [prime] * (
            (limit - prime) // prime + 1
        )

    candidates = sorted(
        set(range(1, maxVal + 1)).union(counts),
        reverse=True,
    )
    divisible_count: dict[int, int] = {}
    best_score = 0

    for selected_value in candidates:
        if selected_value <= best_score:
            break

        remaining = selected_value
        prime_factors = []
        while remaining > 1:
            prime = smallest_prime[remaining]
            prime_factors.append(prime)
            while remaining % prime == 0:
                remaining //= prime

        signed_products = [(1, -1)]
        for prime in prime_factors:
            signed_products += [
                (product * prime, -sign)
                for product, sign in signed_products
            ]

        shared_factor_count = 0
        for product, sign in signed_products[1:]:
            if product not in divisible_count:
                divisible_count[product] = sum(frequency[product::product])
            shared_factor_count += sign * divisible_count[product]

        if counts.get(selected_value, 0) > 0:
            modification_cost = shared_factor_count
            if selected_value > 1:
                modification_cost -= 1
        elif shared_factor_count > 0:
            modification_cost = shared_factor_count
        else:
            modification_cost = 1

        best_score = max(best_score, selected_value - modification_cost)

    return best_score
