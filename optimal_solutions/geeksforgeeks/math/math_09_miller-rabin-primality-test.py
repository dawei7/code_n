"""Optimal solution for math_09: Miller-Rabin Primality Test.

Given a positive integer n, return True iff n is
"""


def solve(n_val, k):
    """Miller-Rabin primality test with k random witnesses."""
    if n_val < 2:
        return False
    if n_val < 4:
        return True
    if n_val % 2 == 0:
        return False
    # Write n - 1 = 2^r * d with d odd.
    r, d = 0, n_val - 1
    while d % 2 == 0:
        d //= 2
        r += 1
    # Test with k random witnesses.
    import random
    rng = random.Random(12345)  # deterministic for testing
    for _ in range(k):
        a = rng.randrange(2, n_val - 1)
        x = pow(a, d, n_val)
        if x == 1 or x == n_val - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % n_val
            if x == n_val - 1:
                break
        else:
            return False
    return True
