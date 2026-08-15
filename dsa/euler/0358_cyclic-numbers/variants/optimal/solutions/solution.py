"""Project Euler Problem 358: Cyclic Numbers.

Find the sum of all digits of the unique cyclic number starting with 00000000137 and ending with 56789.
"""

from math import isqrt


def solve() -> int:
    """Find the sum of all digits of the unique cyclic number."""
    # A cyclic number corresponds to the repetend of 1/p for a full reptend prime p.
    # Leftmost 11 digits: 00000000137 => 1.37e-9 <= 1/p < 1.38e-9
    # => 10^11 // 138 < p <= 10^11 // 137
    low_p = 10**11 // 138
    high_p = 10**11 // 137

    # Rightmost 5 digits: N * p = 10^(p-1) - 1 == -1 mod 10^5 => 56789 * p == 99999 mod 100000
    inv = pow(56789, -1, 100000)
    p_mod = (99999 * inv) % 100000

    start_p = low_p + (p_mod - low_p) % 100000

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        if n % 3 == 0:
            return n == 3
        d = 5
        while d * d <= n:
            if n % d == 0 or n % (d + 2) == 0:
                return False
            d += 6
        return True

    for p in range(start_p, high_p + 1, 100000):
        if (10**11 // p) == 137 and is_prime(p):
            # Check if 10 is a primitive root modulo p
            temp = p - 1
            prime_factors = set()
            d = 2
            while d * d <= temp:
                if temp % d == 0:
                    prime_factors.add(d)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1:
                prime_factors.add(temp)

            is_primitive = True
            for q in prime_factors:
                if pow(10, (p - 1) // q, p) == 1:
                    is_primitive = False
                    break

            if is_primitive:
                # By Midy's theorem, the sum of all digits of repetend 1/p is 9 * (p - 1) // 2
                return 9 * (p - 1) // 2

    raise ValueError("No solution found")


if __name__ == "__main__":
    print(solve())
