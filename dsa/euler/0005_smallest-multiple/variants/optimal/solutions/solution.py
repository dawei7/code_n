import math


def solve(n: int = 20) -> int:
    """Find the smallest positive integer divisible by all numbers from 1 to n.

    Mathematical Principles Applied:
    1. Least Common Multiple (LCM):
       The smallest integer divisible by all numbers in the set {1, 2, ..., n} is
       lcm(1, 2, ..., n).

    2. Associativity of LCM:
       lcm(a_1, a_2, ..., a_n) = lcm(lcm(a_1, a_2, ...), a_n).
       This allows computing the global LCM iteratively or via Python's built-in math.lcm.

    3. Prime Exponent Formulation:
       Equivalent to multiplying p^{floor(log_p n)} for all primes p <= n.

    Time Complexity: O(n log n) using Euclidean GCD reduction.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Accumulate LCM starting at 1
    ans = 1

    # Iteratively compute LCM with each integer k from 2 to n
    for k in range(2, n + 1):
        # Formula: lcm(a, b) = (a * b) // gcd(a, b)
        ans = (ans * k) // math.gcd(ans, k)

    # Return the least common multiple of all numbers from 1 to n
    return ans


if __name__ == "__main__":
    print(solve())
