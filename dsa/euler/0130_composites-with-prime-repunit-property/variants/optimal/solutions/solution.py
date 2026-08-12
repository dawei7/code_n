import math


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


def a_n(n: int) -> int:
    """Find least repunit length k such that R(k) is divisible by n."""
    rem = 1
    k = 1
    while rem != 0:
        rem = (rem * 10 + 1) % n
        k += 1
    return k


def solve(target_count: int = 25) -> int:
    """Find sum of first 25 composite n with gcd(n, 10) = 1 such that (n - 1) % A(n) == 0.
    
    Time Complexity: O(N * A(n))
    Space Complexity: O(1)
    """
    composites = []
    n = 6

    while len(composites) < target_count:
        if math.gcd(n, 10) == 1 and not is_prime(n):
            a = a_n(n)
            if (n - 1) % a == 0:
                composites.append(n)
        n += 1

    return sum(composites)
