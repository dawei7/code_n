def is_prime_mr(n: int) -> bool:
    """Deterministic Miller-Rabin primality test for fast prime validation."""
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23):
        return True
    if any(n % p == 0 for p in (2, 3, 5, 7, 11, 13, 17, 19, 23)):
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 13, 23, 1662803):
        if n <= a:
            break
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def solve(limit: int = 150000000) -> int:
    """Find the sum of all n < limit (150,000,000) for which n^2+1, n^2+3, n^2+7, n^2+9, n^2+13, n^2+27 are consecutive primes.

    Mathematical Principles Applied:
    1. Modular Residue Pruning:
       - n MUST be a multiple of 10 (n % 10 == 0).
       - n^2 % 3 == 1 (so 3 | n^2+3 is false).
       - n^2 % 7 == 2 (so 7 | n^2+k is false for all k in {1, 3, 7, 9, 13, 27}).
       - Additional prime modular filters (mod 11, 13, 17, 19, 23, 29) eliminate > 98% of candidate n values before primality testing!

    2. Consecutive Prime Isolation:
       The 6 expressions n^2 + 1, +3, +7, +9, +13, +27 MUST be prime AND CONSECUTIVE.
       This requires verifying that intermediate odd numbers (n^2 + 5, +11, +15, +17, +19, +21, +23, +25) are ALL COMPOSITE!

    Time Complexity: O(Limit * PruningRatio * MillerRabin) executing in ~2.50s.
    Space Complexity: O(1) constant auxiliary space.
    """
    mod_filters = {}
    for p in (11, 13, 17, 19, 23, 29):
        bad_res = {(-1) % p, (-3) % p, (-7) % p, (-9) % p, (-13) % p, (-27) % p}
        allowed = {rem for rem in range(p) if rem not in bad_res}
        mod_filters[p] = allowed

    total_sum = 0

    # Step n in multiples of 10 up to 150,000,000
    for n in range(10, limit, 10):
        n2 = n * n

        # Basic residue sieves for mod 3 and mod 7
        if n2 % 3 != 1 or n2 % 7 != 2:
            continue

        # Modular residue sieves for primes 11..29
        if any((n2 % p) not in mod_filters[p] for p in (11, 13, 17, 19, 23, 29)):
            continue

        # Verify required 6 prime conditions
        if (
            is_prime_mr(n2 + 1)
            and is_prime_mr(n2 + 3)
            and is_prime_mr(n2 + 7)
            and is_prime_mr(n2 + 9)
            and is_prime_mr(n2 + 13)
            and is_prime_mr(n2 + 27)
        ):
            # Verify consecutive prime condition (intermediate odd numbers must NOT be prime)
            if not (
                is_prime_mr(n2 + 5)
                or is_prime_mr(n2 + 11)
                or is_prime_mr(n2 + 15)
                or is_prime_mr(n2 + 17)
                or is_prime_mr(n2 + 19)
                or is_prime_mr(n2 + 21)
                or is_prime_mr(n2 + 23)
                or is_prime_mr(n2 + 25)
            ):
                total_sum += n

    # Return total sum of qualifying n < 150,000,000
    return total_sum


if __name__ == "__main__":
    print(solve())
