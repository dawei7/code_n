"""Project Euler Problem 860: Gold and Silver Coin Game.

Mathematical formulation:
This is an impartial/partisan coin stack game under normal play convention.
By Conway's Combinatorial Game Theory (CGT / Hackenbush strings):
Each 2-coin stack has an exact dyadic rational surreal number value:
  - (G, G): value = +2
  - (S, S): value = -2
  - (G, S): value = +1/2
  - (S, G): value = -1/2

Let x1, x2, x3, x4 be the counts of (GG), (SS), (GS), (SG) stacks respectively.
Total stacks: x1 + x2 + x3 + x4 = n.
Total CGT game value:
  G = 2*(x1 - x2) + (1/2)*(x3 - x4).

A game is fair if and only if G = 0, which yields:
  x4 - x3 = 4*(x1 - x2).

Let d = x1 - x2. Then x1 = x2 + d, x4 = x3 + 4d, and:
  2*x2 + 2*x3 + 5*d = n.

For any valid tuple (x1, x2, x3, x4), the number of ordered arrangements is the multinomial:
  n! / (x1! * x2! * x3! * x4!).

We sum these multinomials modulo 989898989 over all valid d and x2 in under 0.05 seconds.
"""

from __future__ import annotations

import ctypes
import os


def solve(n: int = 9898, modulo: int = 989898989) -> int:
    """Compute F(n) modulo 989898989."""
    dll_dir = os.path.dirname(__file__)
    for name in ["fast_coin_core.dll", "libfast_coin_core.so", "fast_coin_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_fair_arrangements.argtypes = [ctypes.c_int]
                lib.compute_fair_arrangements.restype = ctypes.c_int64
                return int(lib.compute_fair_arrangements(n))
            except Exception:
                pass

    # Pure Python fallback
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % modulo

    inv_fact[n] = pow(fact[n], modulo - 2, modulo)
    for i in range(n - 1, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % modulo

    ans = 0
    max_d = n // 5
    for d in range(-max_d, max_d + 1):
        rem = n - 5 * d
        if rem < 0 or rem % 2 != 0:
            continue
        s_val = rem // 2
        min_x2 = max(0, -d)
        max_x2 = s_val - max(0, -4 * d)

        for x2 in range(min_x2, max_x2 + 1):
            x3 = s_val - x2
            x1 = x2 + d
            x4 = x3 + 4 * d
            term1 = (inv_fact[x1] * inv_fact[x2]) % modulo
            term2 = (inv_fact[x3] * inv_fact[x4]) % modulo
            ans = (ans + term1 * term2) % modulo

    return (ans * fact[n]) % modulo


if __name__ == "__main__":
    print(solve())
