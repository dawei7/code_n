"""Optimal solution for dc_04: Karatsuba Multiplication.

Multiply two non-negative integers using Karatsuba's
"""


def solve(x, y, n):
    """Karatsuba multiplication: x * y.

    Recursive 3-way multiplication beats the schoolbook 4-way
    multiplication by trading one extra add/subtract for one
    fewer recursive product.
    """
    if x < 10 or y < 10:
        return x * y
    m = max(len(str(x)), len(str(y)))
    half = m // 2
    pow10 = 10 ** half
    a, b = divmod(x, pow10)
    c, d = divmod(y, pow10)
    ac = solve(a, c, n)
    bd = solve(b, d, n)
    ad_bc = solve(a + b, c + d, n) - ac - bd
    return ac * 10 ** (2 * half) + ad_bc * 10 ** half + bd
