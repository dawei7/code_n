"""Project Euler Problem 648: Skipping Squares.

Find F(1000) mod 10^9, where F(n) is the sum of coefficients a_k for k = 0, ..., n
in the power series f(rho) = sum_{k=0}^infty a_k rho^k representing the expected number
of skipped squares.
"""

from typing import List

_MOD = 1_000_000_000
_SHIFT = 70
_BASE = 1 << _SHIFT
_MASK = _BASE - 1


def _pack_digits(coeffs: List[int]) -> int:
    v = 0
    for c in reversed(coeffs):
        v = (v << _SHIFT) + c
    return v


def _mul_trunc(a: List[int], b: List[int], out_len: int) -> List[int]:
    if out_len <= 0:
        return []
    val_a = _pack_digits(a)
    val_b = _pack_digits(b)
    prod = val_a * val_b
    out = [0] * out_len
    for i in range(out_len):
        out[i] = (prod & _MASK) % _MOD
        prod >>= _SHIFT
    return out


def _next_v(v_prev1: List[int], v_prev2: List[int], n_max: int) -> List[int]:
    v = [0] * (n_max + 1)
    v[0] = v_prev2[0]
    for i in range(n_max):
        v[i + 1] = (v_prev2[i + 1] + v_prev1[i] - v_prev2[i]) % _MOD
    return v


def solve(n: int = 1000) -> int:
    """Compute F(n) modulo 10^9 using truncated Markov renewal polynomial multiplication."""
    a = [0] * (n + 1)

    s_offset = 0
    s_poly = [0] * (n + 1)
    s_poly[0] = 1
    s_poly[1] = _MOD - 1

    for i, c in enumerate(s_poly):
        a[i] = (a[i] + c) % _MOD

    v_prev2 = [0] * (n + 1)
    v_prev1 = s_poly[:]

    for k in range(2, 2 * n + 1):
        vk = _next_v(v_prev1, v_prev2, n)
        v_prev2, v_prev1 = v_prev1, vk

        if k % 2 != 0:
            continue

        b_poly = vk
        maxdeg_factor = n - s_offset
        factor = b_poly[1 : maxdeg_factor + 1]

        new_offset = s_offset + 1
        out_len = n - new_offset + 1
        left = s_poly[s_offset : s_offset + out_len]
        right = factor[:out_len]

        prod = _mul_trunc(left, right, out_len)

        s_offset = new_offset
        s_poly = [0] * s_offset + prod + [0] * (n - (s_offset + len(prod)) + 1)

        for i, c in enumerate(prod):
            a[s_offset + i] = (a[s_offset + i] + c) % _MOD

    return sum(a[: n + 1]) % _MOD


if __name__ == "__main__":
    print(solve())
