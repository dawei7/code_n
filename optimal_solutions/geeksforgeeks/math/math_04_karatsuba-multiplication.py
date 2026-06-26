"""Optimal solution for math_04: Karatsuba Multiplication.

Recursive divide and conquer: split each number into halves,
compute 3 half-sized products (instead of 4), combine.
"""


def solve(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    power = 10 ** half
    a, b = divmod(x, power)
    c, d = divmod(y, power)
    ac = solve(a, c)
    bd = solve(b, d)
    ad_bc = solve(a + b, c + d) - ac - bd
    return ac * (10 ** (2 * half)) + ad_bc * power + bd
