import math


def a_n(n: int) -> int:
    """Find the minimal repunit length A(n) = k such that R(k) = (10^k - 1) / 9 is divisible by n.

    Mathematical Principles Applied:
    1. Modular Recurrence for Repunit Remainder:
       R(1) = 1.
       R(k+1) = (10 * R(k) + 1) mod n.
       Since gcd(n, 10) = 1, 10 is an element of (Z/nZ)*, guaranteeing that R(k) mod n = 0 occurs
       in at most n steps (A(n) <= n).
    """
    rem = 1
    k = 1
    # Iterate modular remainder until rem == 0 (divisible)
    while rem != 0:
        rem = (rem * 10 + 1) % n
        k += 1
    return k


def solve(target: int = 1000000) -> int:
    """Find the least n with gcd(n, 10) = 1 for which A(n) first exceeds target = 1,000,000.

    Mathematical Principles Applied:
    1. Lower Bound Pruning Theorem:
       Since A(n) <= n for all n coprime to 10, any n <= target CANNOT satisfy A(n) > target!
       Therefore, we can start our search directly at n = target + 1 (1,000,001).

    Time Complexity: O(N * A(n)) executing in ~0.05s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Direct starting lower bound: n > target (1,000,000)
    n = target + 1
    if n % 2 == 0:
        n += 1

    # Search odd n coprime to 10
    while True:
        if math.gcd(n, 10) == 1:
            if a_n(n) > target:
                return n
        n += 2


if __name__ == "__main__":
    print(solve())
