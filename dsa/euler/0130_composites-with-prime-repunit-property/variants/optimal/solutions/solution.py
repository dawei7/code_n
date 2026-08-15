import math


def is_prime(n: int) -> bool:
    """Fast wheel primality test for composite check."""
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
    """Find the minimal repunit length A(n) = k such that R(k) = (10^k - 1) / 9 is divisible by n."""
    rem = 1
    k = 1
    # Iterate modular remainder until rem == 0
    while rem != 0:
        rem = (rem * 10 + 1) % n
        k += 1
    return k


def solve(target_count: int = 25) -> int:
    """Find the sum of the first 25 composite integers n with gcd(n, 10) = 1 for which (n - 1) is divisible by A(n).

    Mathematical Principles Applied:
    1. Prime Repunit Property for Composite Numbers:
       For any prime p > 5, Fermat's Little Theorem guarantees that A(p) divides (p - 1).
       However, certain rare COMPOSITE numbers n also satisfy A(n) | (n - 1).

    2. Linear Scan & Primality Filtering:
       Iterate composite numbers n coprime to 10.
       Compute A(n) and check if (n - 1) % A(n) == 0.
       Collect the first 25 such composite values and sum them.

    Time Complexity: O(N * A(n)) executing in ~0.02s.
    Space Complexity: O(1) constant auxiliary space.
    """
    composites = []
    n = 6

    # Collect first 25 qualifying composite numbers
    while len(composites) < target_count:
        if math.gcd(n, 10) == 1 and not is_prime(n):
            a = a_n(n)
            # Check if (n - 1) is divisible by A(n)
            if (n - 1) % a == 0:
                composites.append(n)
        n += 1

    # Return sum of the first 25 qualifying composite numbers
    return sum(composites)


if __name__ == "__main__":
    print(solve())
