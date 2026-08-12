import math


def a_n(n: int) -> int:
    """Find least length k such that R(k) = 11...1 is divisible by n."""
    rem = 1
    k = 1
    while rem != 0:
        rem = (rem * 10 + 1) % n
        k += 1
    return k


def solve(target: int = 1000000) -> int:
    """Find least n with gcd(n, 10) = 1 for which A(n) > target.
    
    Time Complexity: O(N * A(n))
    Space Complexity: O(1)
    """
    n = target + 1
    if n % 2 == 0:
        n += 1

    while True:
        if math.gcd(n, 10) == 1:
            if a_n(n) > target:
                return n
        n += 2
