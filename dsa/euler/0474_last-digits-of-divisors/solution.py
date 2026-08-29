"""Project Euler Problem 474: Last Digits of Divisors.

Find F(10^6!, 65432) mod (10^16 + 61), the number of divisors of 10^6!
whose last digits equal 65432.
"""

from array import array
from math import gcd, isqrt
from typing import Dict, List

MOD = 10**16 + 61


def _sieve_primes(limit: int) -> List[int]:
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (
                ((limit - start) // p) + 1
            )
    return [p for p in range(2, limit + 1) if flags[p]]


def _exponent_in_factorial(n: int, p: int) -> int:
    exponent = 0
    while n:
        n //= p
        exponent += n
    return exponent


def _v_factor(n: int, p: int) -> int:
    exponent = 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent


def _brute_count(n: int, d: int, mod: int = MOD) -> int:
    modulus = 10 ** len(str(d))
    residues = {1: 1}
    for p in _sieve_primes(n):
        powers = [1]
        step = p % modulus
        for _ in range(_exponent_in_factorial(n, p)):
            powers.append(powers[-1] * step % modulus)

        new: Dict[int, int] = {}
        for residue, count in residues.items():
            for power in powers:
                nxt = residue * power % modulus
                new[nxt] = (new.get(nxt, 0) + count) % mod
        residues = new
    return residues.get(d % modulus, 0)


class _UnitResidueDp:
    def __init__(self, modulus: int) -> None:
        self.modulus = modulus
        self.units = [r for r in range(1, modulus) if gcd(r, modulus) == 1]
        self.index = [-1] * modulus
        for i, residue in enumerate(self.units):
            self.index[residue] = i
        self.cycles: Dict[int, List[array]] = {}

    def cycles_for(self, multiplier: int) -> List[array]:
        multiplier %= self.modulus
        cached = self.cycles.get(multiplier)
        if cached is not None:
            return cached

        seen = bytearray(len(self.units))
        cycles: List[array] = []
        for start in range(len(self.units)):
            if seen[start]:
                continue
            cycle = array("H")
            idx = start
            while not seen[idx]:
                seen[idx] = 1
                cycle.append(idx)
                idx = self.index[self.units[idx] * multiplier % self.modulus]
            cycles.append(cycle)

        self.cycles[multiplier] = cycles
        return cycles

    def apply_prime(
        self, dp: List[int], multiplier: int, terms: int, mod: int = MOD
    ) -> List[int]:
        new = [0] * len(dp)
        for cycle in self.cycles_for(multiplier):
            length = len(cycle)
            full_turns, tail = divmod(terms, length)
            values = [dp[idx] for idx in cycle]
            full = (full_turns % mod) * (sum(values) % mod) % mod

            if tail == 0:
                for idx in cycle:
                    new[idx] = full
                continue

            window = sum(values[-j % length] for j in range(tail)) % mod
            for i, idx in enumerate(cycle):
                new[idx] = (full + window) % mod
                window += values[(i + 1) % length]
                window -= values[(i + 1 - tail) % length]
                window %= mod

        return new


def solve(n: int = 10**6, d: int = 65432, mod: int = MOD) -> int:
    """Compute F(n!, d) mod mod using unit group cycle decomposition."""
    digits = len(str(d))
    alpha = _v_factor(d, 2)
    beta = _v_factor(d, 5)

    if alpha >= digits or beta >= digits:
        return _brute_count(n, d, mod)

    if alpha > _exponent_in_factorial(
        n, 2
    ) or beta > _exponent_in_factorial(n, 5):
        return 0

    fixed = (2**alpha) * (5**beta)
    modulus = 10**digits // fixed
    target = d // fixed
    if gcd(target, modulus) != 1:
        return 0

    primes = _sieve_primes(n)
    unit_dp = _UnitResidueDp(modulus)
    dp = [0] * len(unit_dp.units)
    dp[unit_dp.index[1]] = 1

    for p in primes:
        if p == 2 or p == 5:
            continue
        terms = _exponent_in_factorial(n, p) + 1
        dp = unit_dp.apply_prime(dp, p, terms, mod)

    return dp[unit_dp.index[target % modulus]] % mod


if __name__ == "__main__":
    print(solve())
