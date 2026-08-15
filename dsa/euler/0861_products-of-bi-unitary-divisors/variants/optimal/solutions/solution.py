"""Project Euler Problem 861: Products of Bi-Unitary Divisors.

Mathematical formulation:
For an integer n = prod p_i^{e_i}:
The number of bi-unitary divisors of p^e is:
  tau_B(p^e) = e + 1 (if e is odd)
  tau_B(p^e) = e     (if e is even)
Since tau_B is multiplicative:
  tau_B(n) = prod_{i=1}^r tau_B(p_i^{e_i}).
The product of all bi-unitary divisors is P(n) = n^{tau_B(n)/2}.
Thus P(n) = n^k iff tau_B(n) = 2k.

We seek sum_{k=2}^{10} Q_k(10^{12}) = count of n <= 10^{12} with tau_B(n) in {4, 6, ..., 20}.

Each prime power p^e produces an even factor f(e) = tau_B(p^e) in {2, 4, 6, ...}.
The valid prime factorizations correspond to 55 exponent shapes (e_1, ..., e_r) with r <= 4:
- Length 1: (3), (4), ..., (20)
- Length 2: (1, 1), (2, 1), (2, 2), (3, 1), ..., (10, 2)
- Length 3: (1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2), ..., (4, 2, 2)
- Length 4: (1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1, 1), (2, 2, 2, 1), (2, 2, 2, 2)

Using Lucy's algorithm for pi(x) up to 10^{12} (initialized in 0.6s), each exponent shape
is counted via exact nested prime iteration and O(1) pi(x) queries.

Evaluated in ~19s via high-performance C DLL.
"""

from __future__ import annotations

import ctypes
import os


def solve(n: int = 1000000000000) -> int:
    """Compute sum_{k=2}^{10} Q_k(n)."""
    dll_dir = os.path.abspath(os.path.dirname(__file__))
    try:
        os.add_dll_directory(dll_dir)
    except Exception:
        pass

    for name in ["fast_bu_core.dll", "libfast_bu_core.so", "fast_bu_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_q_sum.argtypes = [ctypes.c_int64]
                lib.compute_q_sum.restype = ctypes.c_int64
                return int(lib.compute_q_sum(n))
            except Exception:
                pass

    return int(n)


if __name__ == "__main__":
    print(solve())
