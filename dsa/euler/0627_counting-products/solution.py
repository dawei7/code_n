"""Project Euler Problem 627: Counting Products.

Find F(30, 10001) mod 1000000007, where F(m, n) is the number of distinct products
of n positive integers not exceeding m.
"""

from typing import List, Set

_MOD = 1_000_000_007


def _modinv(a: int) -> int:
    return pow(a % _MOD, _MOD - 2, _MOD)


def _rising_mod(a: int, k: int) -> int:
    res = 1
    a %= _MOD
    for i in range(k):
        res = (res * (a + i)) % _MOD
    return res


def solve(m: int = 30, target_n: int = 10001) -> int:
    """Compute F(m, target_n) modulo 1000000007 using Ehrhart polynomial degree-3 factorization."""
    max_n = 5
    nums = list(range(1, m + 1))
    prods: Set[int] = {1}
    f_vals = [1]
    for _ in range(max_n):
        new_set: Set[int] = set()
        for p in prods:
            for x in nums:
                new_set.add(p * x)
        prods = new_set
        f_vals.append(len(prods))

    cvals: List[int] = []
    for k in range(4):
        denom = _rising_mod(k + 1, 7)
        cvals.append((f_vals[k] * _modinv(denom)) % _MOD)

    f0, f1, f2, f3 = cvals[0], cvals[1], cvals[2], cvals[3]
    d1 = (f1 - f0) % _MOD
    d2 = (f2 - 2 * f1 + f0) % _MOD
    d3 = (f3 - 3 * f2 + 3 * f1 - f0) % _MOD

    n_mod = target_n % _MOD
    c1 = n_mod
    c2 = n_mod * (n_mod - 1) % _MOD * _modinv(2) % _MOD
    c3 = n_mod * (n_mod - 1) % _MOD * (n_mod - 2) % _MOD * _modinv(6) % _MOD

    c_at_n = (f0 + d1 * c1 + d2 * c2 + d3 * c3) % _MOD
    ans = (_rising_mod(target_n + 1, 7) * c_at_n) % _MOD
    return ans


if __name__ == "__main__":
    print(solve())
