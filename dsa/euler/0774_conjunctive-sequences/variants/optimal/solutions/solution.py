"""Project Euler Problem 774: Conjunctive Sequences.

Find c(123, 123456789) modulo 998244353, the number of conjunctive sequences of length n
with all terms <= b (where a_i & a_{i+1} != 0 for all adjacent terms).
"""

from functools import lru_cache
from typing import Dict, Tuple

_MOD = 998244353
_TOP = -1
_ODD = -2

_FIB = [0] * 200
_FIB[0] = 0
_FIB[1] = 1
for _i in range(2, len(_FIB)):
    _FIB[_i] = (_FIB[_i - 1] + _FIB[_i - 2]) % _MOD


def _fib(index: int) -> int:
    if index >= 0:
        return _FIB[index]
    idx = -index
    return _FIB[idx] if idx & 1 else (-_FIB[idx]) % _MOD


def _boundary_is_impossible(state: int) -> bool:
    return state == 0


def _satisfies(state: int, value: int) -> bool:
    if state == _TOP:
        return True
    if state == _ODD:
        return (value & 1) == 1
    return (value & state) != 0


def _phi_even(state: int) -> int:
    if state == _TOP:
        return _TOP
    if state == _ODD:
        return 0
    return state // 2


def _phi_odd(state: int) -> int:
    if state == _TOP or state == _ODD:
        return _TOP
    if state & 1:
        return _TOP
    return state // 2


@lru_cache(maxsize=None)
def _D(length: int, bound: int, left: int, right: int) -> int:
    if _boundary_is_impossible(left) or _boundary_is_impossible(right):
        return 0

    if length == 0:
        return 1 if left == _TOP and right == _TOP else 0

    if bound <= 1:
        if length == 1:
            return sum(
                1
                for value in range(bound + 1)
                if _satisfies(left, value) and _satisfies(right, value)
            )
        if bound == 0:
            return 0
        return 1 if _satisfies(left, 1) and _satisfies(right, 1) else 0

    if bound % 2 == 0:
        marked_bound = bound
        total = _D(length, bound - 1, left, right)

        for split in range(1, length + 1):
            prefix_len = split - 1
            suffix_len = length - split

            if prefix_len == 0:
                prefix_count = 1 if _satisfies(left, bound) else 0
            else:
                prefix_count = _D(prefix_len, bound - 1, left, marked_bound)
            if prefix_count == 0:
                continue

            if suffix_len == 0:
                suffix_count = 1 if _satisfies(right, bound) else 0
            else:
                suffix_count = _D(suffix_len, bound, marked_bound, right)

            total = (total + prefix_count * suffix_count) % _MOD

        return total

    reduced_bound = (bound - 1) // 2
    left_even = _phi_even(left)
    left_odd = _phi_odd(left)
    right_even = _phi_even(right)
    right_odd = _phi_odd(right)

    total = _D(length, reduced_bound, left_even, right_even) * _fib(length)
    total += _D(length, reduced_bound, left_even, right_odd) * _fib(length - 1)
    total += _D(length, reduced_bound, left_odd, right_even) * _fib(length - 1)
    total += _D(length, reduced_bound, left_odd, right_odd) * _fib(length - 2)
    total %= _MOD

    for cut in range(1, length):
        prefix = _D(cut, reduced_bound, left_odd, _TOP) * _fib(cut - 2)
        if cut > 1:
            prefix += _D(cut, reduced_bound, left_even, _TOP) * _fib(cut - 1)
        prefix %= _MOD
        if prefix:
            total = (total + _D(length - cut, bound, _ODD, right) * prefix) % _MOD

    return total


def solve(length: int = 123, bound: int = 123456789) -> int:
    """Compute c(length, bound) mod 998244353 using bitwise recursive divide-and-conquer DP."""
    ans = 0
    for _iter in range(1):
        ans = _D(length, bound, _TOP, _TOP)
    return ans


if __name__ == "__main__":
    print(solve())
