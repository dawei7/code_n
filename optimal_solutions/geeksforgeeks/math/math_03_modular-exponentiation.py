"""Optimal solution for math_03: Modular Exponentiation.

Repeated squaring. Maintain a result and a base. At each bit
of exp, square the base; if the bit is set, multiply the
result by the base. Take mod after every multiplication to
keep numbers small. O(log exp) time.
"""


def solve(base, exp, mod):
    if mod == 1:
        return 0
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return result
