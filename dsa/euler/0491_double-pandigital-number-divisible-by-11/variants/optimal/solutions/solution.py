"""Project Euler Problem 491: Double Pandigital Number Divisible by 11.

Find how many double pandigital numbers (using digits 0..9 exactly twice with no leading zero)
are divisible by 11.
"""

from itertools import product
from math import factorial, prod


def solve() -> int:
    """Count valid 20-digit double pandigitals via alternating sum divisibility modulo 11."""
    fact = [factorial(i) for i in range(11)]
    fact9 = fact[9]
    fact10 = fact[10]

    total_ways = 0
    for a in product(range(3), repeat=10):
        if sum(a) != 10:
            continue
        s1 = sum(d * a[d] for d in range(10))
        if s1 % 11 != 1:
            continue

        a0 = a[0]
        den_a = prod(fact[c] for c in a)
        perm_a = (10 - a0) * fact9 // den_a

        b = [2 - c for c in a]
        den_b = prod(fact[c] for c in b)
        perm_b = fact10 // den_b

        total_ways += perm_a * perm_b

    return total_ways


if __name__ == "__main__":
    print(solve())
