def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        return True
    if any(n % p == 0 for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)):
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True


def solve(limit: int = 1000000) -> int:
    """Find number of primes p < limit for which n^3 + n^2 * p is a perfect cube.
    
    Time Complexity: O(sqrt(limit))
    Space Complexity: O(1)
    """
    count = 0
    k = 1

    while True:
        p = 3 * k * k + 3 * k + 1
        if p >= limit:
            break

        if is_prime(p):
            count += 1

        k += 1

    return count
