"""Project Euler Problem 707: Lights Out.

Find S(199, 199) mod 1000000007, where S(w, n) = sum_{k=1}^n F(w, f_k) and F(w, h) is the number
of solvable starting states on a w x h grid in Lights Out.
"""

from typing import Tuple

_MOD = 1_000_000_007


def _poly_deg(p: int) -> int:
    return p.bit_length() - 1


def _poly_rem(a: int, b: int) -> int:
    db = _poly_deg(b)
    while a and _poly_deg(a) >= db:
        a ^= b << (_poly_deg(a) - db)
    return a


def _poly_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, _poly_rem(a, b)
    return a


def _poly_mod_f(a: int, f: int, deg_f: int) -> int:
    while a and _poly_deg(a) >= deg_f:
        a ^= f << (_poly_deg(a) - deg_f)
    return a


def _poly_square_mod(a: int, f: int, deg_f: int) -> int:
    res = 0
    bits = a
    while bits:
        lsb = bits & -bits
        i = lsb.bit_length() - 1
        res |= 1 << (2 * i)
        bits ^= lsb
    return _poly_mod_f(res, f, deg_f)


def _poly_mul_x_mod(a: int, f: int, deg_f: int) -> int:
    return _poly_mod_f(a << 1, f, deg_f)


def _char_poly_l(w: int) -> int:
    if w == 0:
        return 1
    x_plus_1 = 0b11
    if w == 1:
        return x_plus_1
    d0, d1 = 1, x_plus_1
    for _ in range(2, w + 1):
        d2 = (d1 << 1) ^ d1 ^ d0
        d0, d1 = d1, d2
    return d1


def _fib_poly_mod(n: int, f: int, deg_f: int) -> Tuple[int, int]:
    if n == 0:
        return 0, 1

    a, b = _fib_poly_mod(n >> 1, f, deg_f)
    a2 = _poly_square_mod(a, f, deg_f)
    b2 = _poly_square_mod(b, f, deg_f)

    c = _poly_mul_x_mod(a2, f, deg_f)
    d = a2 ^ b2

    if (n & 1) == 0:
        return c, d
    e = _poly_mul_x_mod(d, f, deg_f) ^ c
    return d, e


def _get_fib_sequence(n: int) -> list[int]:
    f = [0] * (n + 1)
    if n >= 1:
        f[1] = 1
    if n >= 2:
        f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f


def solve(w: int = 199, n: int = 199, mod: int = _MOD) -> int:
    """Compute S(w, n) modulo mod using GF(2) characteristic polynomials and Fibonacci fast doubling."""
    f = _char_poly_l(w)
    deg_f = w

    fibs = _get_fib_sequence(n)
    total = 0

    for k in range(1, n + 1):
        h = fibs[k]
        r, _ = _fib_poly_mod(h + 1, f, deg_f)
        g = _poly_gcd(f, r)
        nullity = _poly_deg(g)
        exp = w * h - nullity
        term = pow(2, exp % (mod - 1), mod)
        total = (total + term) % mod

    return total


if __name__ == "__main__":
    print(solve())
