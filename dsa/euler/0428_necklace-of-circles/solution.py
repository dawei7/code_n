"""Project Euler Problem 428: Necklace of Circles.

Find T(10^9), the number of necklace triplets (a, b, c) of positive integers with b <= 10^9.
"""

from functools import lru_cache
from math import isqrt
from typing import Callable, Dict, List


def _chi_mod3(n: int) -> int:
    r = n % 3
    if r == 0:
        return 0
    return 1 if r == 1 else -1


def _chi_prefix_integers(x: int) -> int:
    return (x + 2) // 3 - (x + 1) // 3


def _primes_up_to(limit: int) -> List[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    r = isqrt(limit)
    for i in range(2, r + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start : limit + 1 : step] = b"\x00" * (
                ((limit - start) // step) + 1
            )
    return [i for i in range(limit + 1) if sieve[i]]


class _PrimeTables:
    __slots__ = (
        "N",
        "V",
        "vals",
        "id1",
        "id2",
        "pi_tbl",
        "chi_tbl",
        "primes",
    )

    def __init__(self, n_val: int) -> None:
        self.N = n_val
        self.V = isqrt(n_val)

        vals: List[int] = []
        i = 1
        while i <= n_val:
            v = n_val // i
            vals.append(v)
            i = n_val // v + 1
        self.vals = vals

        v_lim = self.V
        id1 = [0] * (v_lim + 1)
        id2 = [0] * (v_lim + 1)
        for idx, v in enumerate(vals):
            if v <= v_lim:
                id1[v] = idx
            else:
                id2[n_val // v] = idx
        self.id1 = id1
        self.id2 = id2

        pi_tbl = [v - 1 for v in vals]
        chi_tbl = [_chi_prefix_integers(v) - 1 for v in vals]

        primes = _primes_up_to(v_lim)
        self.primes = primes

        chi_prime_pref = [0]
        s = 0
        for p in primes:
            s += _chi_mod3(p)
            chi_prime_pref.append(s)

        for pi_idx, p in enumerate(primes, start=1):
            p2 = p * p
            if p2 > n_val:
                break
            pi_before = pi_idx - 1
            chi_before = chi_prime_pref[pi_idx - 1]
            cp = _chi_mod3(p)

            for idx, v in enumerate(vals):
                if v < p2:
                    break
                t = v // p
                j = self.idx_of(t)
                pi_tbl[idx] -= pi_tbl[j] - pi_before
                chi_tbl[idx] -= cp * (chi_tbl[j] - chi_before)

        self.pi_tbl = pi_tbl
        self.chi_tbl = chi_tbl

    def idx_of(self, x: int) -> int:
        if x <= self.V:
            return self.id1[x]
        return self.id2[self.N // x]

    def pi(self, x: int) -> int:
        return self.pi_tbl[self.idx_of(x)]

    def chi_prime_sum(self, x: int) -> int:
        return self.chi_tbl[self.idx_of(x)]


class _Summatory:
    def __init__(self, n_val: int) -> None:
        self.N = n_val
        self.pt = _PrimeTables(n_val)
        self.rec_primes = [p for p in self.pt.primes if p >= 5]
        self._H_F = self._make_h(
            self.prime_sum_f, self.val_f_prime_power
        )
        self._H_G = self._make_h(
            self.prime_sum_g, self.val_g_prime_power
        )

    def prime_sum_f(self, x: int) -> int:
        pi_val = self.pt.pi(x)
        c23 = (1 if x >= 2 else 0) + (1 if x >= 3 else 0)
        return 3 * (pi_val - c23)

    def prime_sum_g(self, x: int) -> int:
        pi_val = self.pt.pi(x)
        c23 = (1 if x >= 2 else 0) + (1 if x >= 3 else 0)
        chi_p = self.pt.chi_prime_sum(x)
        chi_excl = chi_p + (1 if x >= 2 else 0)
        return (pi_val - c23) + 2 * chi_excl

    @staticmethod
    def val_f_prime_power(p: int, e: int) -> int:
        return 2 * e + 1

    @staticmethod
    def val_g_prime_power(p: int, e: int) -> int:
        if p % 3 == 1:
            return 2 * e + 1
        return -1 if (e & 1) else 1

    def _make_h(
        self,
        prime_sum_func: Callable[[int], int],
        val_prime_power: Callable[[int, int], int],
    ) -> Callable[[int, int], int]:
        primes = self.rec_primes

        @lru_cache(maxsize=None)
        def h_rec(n: int, idx: int) -> int:
            prev = primes[idx - 1] if idx > 0 else 1
            if idx >= len(primes) or primes[idx] * primes[idx] > n:
                return prime_sum_func(n) - prime_sum_func(prev)

            res = prime_sum_func(n) - prime_sum_func(prev)
            for k in range(idx, len(primes)):
                p = primes[k]
                if p * p > n:
                    break
                pe = p
                e = 1
                while pe * p <= n:
                    res += val_prime_power(p, e) * h_rec(n // pe, k + 1)
                    res += val_prime_power(p, e + 1)
                    pe *= p
                    e += 1
            return res

        return h_rec

    def sum_f(self, x: int) -> int:
        if x <= 0:
            return 0
        return 1 + self._H_F(x, 0)

    def sum_g(self, x: int) -> int:
        if x <= 0:
            return 0
        return 1 + self._H_G(x, 0)


def solve(n: int = 1_000_000_000) -> int:
    """Compute T(n) using Min_25 sublinear multiplicative summatory functions."""
    summatory = _Summatory(n)
    f_cache: Dict[int, int] = {}
    g_cache: Dict[int, int] = {}

    def f_func(x: int) -> int:
        if x not in f_cache:
            f_cache[x] = summatory.sum_f(x)
        return f_cache[x]

    def g_func(x: int) -> int:
        if x not in g_cache:
            g_cache[x] = summatory.sum_g(x)
        return g_cache[x]

    total = 0

    pow2 = 1
    i = 0
    while pow2 <= n:
        pow3 = 1
        j = 0
        while pow2 * pow3 <= n:
            x = n // (pow2 * pow3)
            fx = f_func(x)

            total += (2 * i + 2) * (2 * j + 1) * fx
            total += (2 * i + 3) * (2 * j + 2) * fx

            if j >= 1:
                total += (2 * j - 1) * (2 * i + 3) * fx

            pow3 *= 3
            j += 1
        pow2 *= 2
        i += 1

    pow2 = 1
    i = 0
    while pow2 <= n:
        x = n // pow2
        sign = 1 if (i % 2 == 0) else -1
        total += ((2 * i + 3) * f_func(x) - sign * g_func(x)) // 2
        pow2 *= 2
        i += 1

    return total


if __name__ == "__main__":
    print(solve())
