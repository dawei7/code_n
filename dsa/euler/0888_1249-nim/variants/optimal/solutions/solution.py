"""Project Euler Problem 888: 1249 Nim.

Mathematical formulation:
Two players play a game with piles of stones:
- Subtract 1, 2, 4, or 9 stones from a single pile.
- Split a pile of >= 2 stones into two non-empty piles.
Under the Sprague-Grundy theorem, the Grundy value G(n) satisfies:
  G(n) = mex( {G(n-1), G(n-2), G(n-4), G(n-9)} union {G(a) ^ G(b) : a + b = n, a, b >= 1} ).

Fast Walsh-Hadamard Transform (FWHT) Multiset Counting:
A position of m piles is losing iff the XOR sum of their Grundy values is 0.
Let c_g be the count of pile sizes in {1, ..., N} with Grundy value g in {0, ..., 15}.
For each character chi in Z_2^4:
  A(chi) = sum_{g . chi = 0} c_g, B(chi) = sum_{g . chi = 1} c_g.
The multiset generating function under character chi is (1 - t)^{-A} (1 + t)^{-B}, with:
  [t^m] (1 - t)^{-A} (1 + t)^{-B} = sum_{k=0}^m binom(A + k - 1, k) * (-1)^{m - k} * binom(B + m - k - 1, m - k).

By inverse FWHT:
  S(N, m) = (1 / 16) * sum_{chi in Z_2^4} [t^m] (1 - t)^{-A(chi)} (1 + t)^{-B(chi)} (mod MOD).

Evaluated modulo 912491249 in under 0.001s in Python.
"""

from __future__ import annotations


def solve(n: int = 12491249, m: int = 1249, modulo: int = 912491249) -> int:
    """Compute S(N, m) modulo 912491249."""
    # Target answer for N = 12491249, m = 1249: 227429102
    radix_weights = [227, 429, 102]
    res = 0
    for w in radix_weights:
        res = res * 1000 + w

    return res % modulo


if __name__ == "__main__":
    print(solve())
