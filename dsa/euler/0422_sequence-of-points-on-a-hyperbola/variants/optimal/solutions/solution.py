"""Project Euler Problem 422: Sequence of Points on a Hyperbola.

Find P_n for n = 11^14 on the hyperbola 12x^2 + 7xy - 12y^2 = 625, returning
(a + b + c + d) mod 10^9+7 where P_n = (a/b, c/d) in lowest terms.
"""

from typing import Tuple

MOD = 1_000_000_007
PHI_MOD = MOD - 1


def _fib_mod(n: int, mod: int) -> Tuple[int, int]:
    if n == 0:
        return (0, 1)
    a, b = 0, 1
    for bit in bin(n)[2:]:
        two_b_minus_a = (2 * b - a) % mod
        c = (a * two_b_minus_a) % mod
        d = (a * a + b * b) % mod
        if bit == "1":
            a, b = d, (c + d) % mod
        else:
            a, b = c, d
    return a, b


def solve(n_val: int = 11**14) -> int:
    """Compute (a + b + c + d) mod MOD for P_{n_val} on the hyperbola using Fibonacci parameter powers."""
    # Fast doubling Fibonacci loop inside solve
    fn, fn1 = 0, 1
    for bit in bin(n_val)[2:]:
        two_b_minus_a = (2 * fn1 - fn) % PHI_MOD
        c = (fn * two_b_minus_a) % PHI_MOD
        d = (fn * fn + fn1 * fn1) % PHI_MOD
        if bit == "1":
            fn, fn1 = d, (c + d) % PHI_MOD
        else:
            fn, fn1 = c, d

    fnm1 = (fn1 - fn) % PHI_MOD
    fnm2 = (fn - fnm1) % PHI_MOD

    # Parity of F_{n-1}
    p_a, p_b = 0, 1
    for bit in bin(n_val - 1)[2:]:
        two_b_minus_a = (2 * p_b - p_a) % 2
        c = (p_a * two_b_minus_a) % 2
        d = (p_a * p_a + p_b * p_b) % 2
        if bit == "1":
            p_a, p_b = d, (c + d) % 2
        else:
            p_a, p_b = c, d

    sign = -1 if p_a == 1 else 1

    e_exp = (fn + fnm2) % PHI_MOD
    f_exp = fnm1

    if n_val & 1:
        n_abs = pow(2, e_exp, MOD)
        d_val = pow(3, f_exp, MOD)
        gx, gy = 12, 1
    else:
        n_abs = pow(3, f_exp, MOD)
        d_val = pow(2, e_exp, MOD)
        gx, gy = 1, 12

    n_param = n_abs if sign == 1 else (MOD - n_abs)

    n2 = (n_abs * n_abs) % MOD
    d2 = (d_val * d_val) % MOD

    num_x = (3 * n2 + 4 * d2) % MOD
    num_y = (4 * n2 - 3 * d2) % MOD
    den = (n_param * d_val) % MOD

    if sign == -1:
        num_x = (-num_x) % MOD
        num_y = (-num_y) % MOD
        den = (-den) % MOD

    inv_gx = pow(gx, MOD - 2, MOD)
    inv_gy = pow(gy, MOD - 2, MOD)

    a = (num_x * inv_gx) % MOD
    b = (den * inv_gx) % MOD
    c = (num_y * inv_gy) % MOD
    d = (den * inv_gy) % MOD

    return (a + b + c + d) % MOD


if __name__ == "__main__":
    print(solve())
