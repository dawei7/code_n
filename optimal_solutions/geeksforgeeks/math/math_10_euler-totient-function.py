"""Optimal solution for math_10: Euler Totient Function.

Given a positive integer n, return phi(n): the
"""


def solve(n_val):
    """Euler's totient function phi(n) via prime factorization."""
    if n_val <= 0:
        return 0
    if n_val == 1:
        return 1
    result = n_val
    p = 2
    temp = n_val
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        # temp is a prime factor > sqrt(original n).
        result -= result // temp
    return result
