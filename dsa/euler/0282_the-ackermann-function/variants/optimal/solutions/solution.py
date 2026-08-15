"""Project Euler 282: The Ackermann Function

Find sum_{n=0}^6 A(n, n) mod 14^8.
"""

from __future__ import annotations


def euler_phi(n: int) -> int:
    """Calculates Euler's totient function phi(n)."""
    res = n
    temp = n
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            res -= res // p
        p += 1
    if temp > 1:
        res -= res // temp
    return res


def eval_power_tower_2(height: int, mod: int) -> int:
    """Evaluates the power tower 2^^height mod `mod` using Euler's totient theorem reduction:

    a^b = a^( (b mod phi(m)) + phi(m) ) (mod m) for b >= log2(m).
    """
    if mod == 1:
        return 0
    if height == 0:
        return 1
    if height == 1:
        return 2 % mod
    if height == 2:
        return 4 % mod
    if height == 3:
        return 16 % mod
    if height == 4:
        return 65536 % mod

    p = euler_phi(mod)
    exp = eval_power_tower_2(height - 1, p)
    return pow(2, exp + p, mod)


def ackermann_diagonal(n: int, mod: int) -> int:
    """Computes A(n, n) mod `mod` using algebraic closed forms and power tower reduction."""
    if n == 0:
        return 1 % mod
    if n == 1:
        return 3 % mod
    if n == 2:
        return 7 % mod
    if n == 3:
        return (pow(2, 6, mod) - 3) % mod
    if n == 4:
        return (eval_power_tower_2(7, mod) - 3) % mod
    # For n >= 5, the tower height exceeds the totient chain depth (~25), stabilizing:
    return (eval_power_tower_2(100, mod) - 3) % mod


def solve(max_n: int = 6, base: int = 14, exp: int = 8) -> str:
    """Computes sum_{n=0}^max_n A(n, n) mod base^exp."""
    mod = base**exp
    total = 0
    for n in range(max_n + 1):
        val = ackermann_diagonal(n, mod)
        total = (total + val) % mod
    return str(total)


if __name__ == "__main__":
    print(solve())
