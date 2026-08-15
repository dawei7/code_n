"""Project Euler Problem 605: Pairwise Coin-Tossing Game.

Find the last 8 digits of M_{10^8+7}(10^4+7), where M_n(k) is the product of the numerator
and denominator of the reduced probability fraction P_n(k) that player k wins.
"""

from math import gcd
from typing import Tuple

_MOD = 10**8


def _reduced_fraction_p(n: int, k: int) -> Tuple[int, int]:
    a = (1 << n) - 1
    n0 = (k - 1) * a + n
    num = (1 << (n - k)) * n0
    den = a * a
    g1 = gcd(n0, a)
    g2 = gcd(n0 // g1, a)
    g = g1 * g2
    num //= g
    den //= g
    gnd = gcd(num, den)
    return num // gnd, den // gnd


def solve(n: int = 10**8 + 7, k: int = 10**4 + 7) -> str:
    """Compute the last 8 digits of M_n(k) using geometric series closed forms and modular exponentiation."""
    two_n = pow(2, n, _MOD)
    a_mod = (two_n - 1) % _MOD

    n0_mod = ((k - 1) * a_mod + (n % _MOD)) % _MOD
    part1 = pow(2, n - k, _MOD)
    part2 = (a_mod * a_mod) % _MOD

    ans = (part1 * n0_mod % _MOD) * part2 % _MOD
    digits = [(ans // (10**i)) % 10 for i in range(7, -1, -1)]
    return "".join(str(d) for d in digits)


if __name__ == "__main__":
    print(solve())
