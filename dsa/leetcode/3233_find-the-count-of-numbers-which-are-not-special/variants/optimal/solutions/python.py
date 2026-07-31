from math import isqrt


def solve(l: int, r: int) -> int:
    limit = isqrt(r)
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    if limit >= 1:
        is_prime[1] = False

    for factor in range(2, isqrt(limit) + 1):
        if is_prime[factor]:
            start = factor * factor
            is_prime[start : limit + 1 : factor] = [False] * (
                (limit - start) // factor + 1
            )

    first_root = isqrt(l - 1) + 1
    special = sum(is_prime[root] for root in range(first_root, limit + 1))
    return r - l + 1 - special
