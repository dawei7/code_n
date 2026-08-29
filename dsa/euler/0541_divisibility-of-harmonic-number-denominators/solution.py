"""Project Euler Problem 541: Divisibility of Harmonic Number Denominators.

Find M(137), where M(p) is the largest value of n such that the reduced denominator
of the n-th harmonic number H_n is not divisible by p.
"""

from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Set, Tuple


def _inv_mod(a: int, mod: int) -> int:
    a %= mod
    t, newt = 0, 1
    r, newr = mod, a
    while newr:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if r != 1:
        raise ValueError("inverse does not exist")
    return t % mod


class HarmonicDenominatorSolver:
    def __init__(self, p: int) -> None:
        self.p = p
        self.s_max = 12

        self.binom: List[List[int]] = [
            [0] * (self.s_max + 1) for _ in range(self.s_max + 1)
        ]
        for n in range(self.s_max + 1):
            self.binom[n][0] = self.binom[n][n] = 1
            for k in range(1, n):
                self.binom[n][k] = (
                    self.binom[n - 1][k - 1] + self.binom[n - 1][k]
                )

        self.prefix_pows: List[List[int]] = [
            [0] * (self.s_max + 1) for _ in range(self.p + 1)
        ]
        for r in range(1, self.p + 1):
            b = r - 1
            row = self.prefix_pows[r]
            prev = self.prefix_pows[r - 1]
            for k in range(self.s_max + 1):
                row[k] = prev[k] + (b**k)

        self.digit_pows: List[int] = [
            self.prefix_pows[self.p][k] for k in range(self.s_max + 1)
        ]
        self.ha_to_digits: Dict[int, List[int]] = self._build_ha_digit_map()

    def _build_ha_digit_map(self) -> Dict[int, List[int]]:
        p = self.p
        invs = [0] * p
        for a in range(1, p):
            invs[a] = _inv_mod(a, p)
        ha = [0] * p
        s = 0
        for a in range(1, p):
            s = (s + invs[a]) % p
            ha[a] = s
        ha[0] = 0

        mp: Dict[int, List[int]] = {}
        for a, v in enumerate(ha):
            mp.setdefault(v, []).append(a)
        return mp

    @lru_cache(maxsize=None)
    def _pow_sum(self, m: int, q: int, s: int) -> int:
        if q <= 0:
            return 0
        mod = self.p**s
        p = self.p
        if q <= p:
            return self.prefix_pows[q][m] % mod

        big_q, r = divmod(q, p)
        res = 0

        for t in range(m + 1):
            res = (
                res
                + self.binom[m][t]
                * pow(p, t, mod)
                * self._pow_sum(t, big_q, s)
                * (self.digit_pows[m - t] % mod)
            ) % mod

        base = (big_q * p) % mod
        for t in range(m + 1):
            res = (
                res
                + self.binom[m][t]
                * pow(base, t, mod)
                * (self.prefix_pows[r][m - t] % mod)
            ) % mod

        return res

    @lru_cache(maxsize=None)
    def _cm(self, s: int) -> Tuple[int, ...]:
        mod = self.p**s
        p = self.p
        out = []
        for m in range(s):
            sm = 0
            for j in range(1, p):
                invj = _inv_mod(j, mod)
                sm = (sm + pow(invj, m + 1, mod)) % mod
            out.append(sm)
        return tuple(out)

    @lru_cache(maxsize=None)
    def unit_inverse_sum(self, n_val: int, s: int) -> int:
        if n_val <= 0:
            return 0
        p = self.p
        mod = p**s
        q, r = divmod(n_val, p)
        cm = self._cm(s)

        total = 0
        if q > 0:
            for m in range(s):
                sm = self._pow_sum(m, q, s)
                term = (pow(p, m, mod) * sm) % mod
                term = (term * cm[m]) % mod
                if m & 1:
                    term = (-term) % mod
                total = (total + term) % mod

        base = q * p
        for j in range(1, r + 1):
            if j % p == 0:
                continue
            total = (total + _inv_mod(base + j, mod)) % mod

        return total

    @lru_cache(maxsize=None)
    def v_func(self, e: int, m: int, mod_power: int) -> int:
        p = self.p
        mod = p**mod_power
        val = 0
        div = 1
        for t in range(1, e + 1):
            coeff = p ** (e - t)
            n_val = m // div
            val = (val + coeff * self.unit_inverse_sum(n_val, mod_power)) % mod
            div *= p
        return val


def solve(p: int = 137) -> int:
    """Compute M(p) using p-adic tree lifting on base-p digits."""
    if p == 3:
        h = Fraction(0, 1)
        best_n = 0
        for n in range(1, 500):
            h += Fraction(1, n)
            if h.denominator % 3 != 0:
                best_n = n
        return best_n

    solver = HarmonicDenominatorSolver(p)
    best = p - 1

    active_a: List[int] = solver.ha_to_digits.get(0, [])
    active_a = [m for m in active_a if 1 <= m < p]

    e = 1
    while active_a:
        best = max(best, p * max(active_a) + (p - 1))

        next_set: Set[int] = set()
        for q in active_a:
            val = solver.v_func(e, q, e + 1)
            d = (val // (p**e)) % p
            target = (-d) % p
            for a in solver.ha_to_digits.get(target, []):
                next_set.add(q * p + a)

        active_a = sorted(next_set)
        e += 1
        if e > 30:
            break

    return best


if __name__ == "__main__":
    print(solve())
