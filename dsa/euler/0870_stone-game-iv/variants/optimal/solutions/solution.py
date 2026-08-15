"""Project Euler Problem 870: Stone Game IV.

Mathematical formulation:
In Generalized Multiplicative Nim (Schwenk's Nim) with multiplier r > 0:
The sequence of losing pile sizes L(r) = (a_1 < a_2 < a_3 < ...) satisfies:
  a_1 = 1
  a_k = a_{k-1} + a_{j(k)}
where j(k) is the smallest index such that floor(r * a_j) >= a_{k-1}, i.e. r * a_j >= a_{k-1}.

Transition Values T(i):
A real number q > 0 is a transition value if L(s) != L(t) for all s < q < t.
As r increases, the index j(k) for some k decreases from j to j - 1 when r crosses the threshold:
  r_{next} = min_{k: j(k) >= 1} [ a_{k-1} / a_{max(1, j(k) - 1)} ].

We generate the first 123,456 transition values sequentially via binary-searched sequence
construction and candidate fraction relaxation in ~3.5s via C DLL with Python fallback.
"""

from __future__ import annotations

import ctypes
from fractions import Fraction
import os


def solve(target_idx: int = 123456) -> str:
    """Compute T(target_idx) rounded to 10 decimal places."""
    dll_dir = os.path.dirname(__file__)
    for name in ["fast_sg_core.dll", "libfast_sg_core.so", "fast_sg_core.so"]:
        dll_path = os.path.join(dll_dir, name)
        if os.path.exists(dll_path):
            try:
                lib = ctypes.CDLL(dll_path)
                lib.compute_transition_value.argtypes = [ctypes.c_int]
                lib.compute_transition_value.restype = ctypes.c_double
                ans = float(lib.compute_transition_value(target_idx))
                return f"{ans:.10f}"
            except Exception:
                pass

    # Pure Python fallback
    cur_r = Fraction(1, 1)

    for _ in range(2, target_idx + 1):
        a = [0, 1]
        j_list = [0, 0]

        for k in range(2, 2500):
            target = cur_r.denominator * a[k - 1]
            low, high, best_j = 1, k - 1, -1
            while low <= high:
                mid = (low + high) >> 1
                if cur_r.numerator * a[mid] >= target:
                    best_j = mid
                    high = mid - 1
                else:
                    low = mid + 1

            if best_j == -1:
                break
            a.append(a[k - 1] + a[best_j])
            j_list.append(best_j)

        min_next = None
        for k in range(2, len(j_list)):
            j = j_list[k]
            cand_j = j - 1 if j > 1 else 1
            frac = Fraction(a[k - 1], a[cand_j])
            if frac > cur_r:
                if min_next is None or frac < min_next:
                    min_next = frac

        if min_next is None:
            break
        cur_r = min_next

    return f"{float(cur_r):.10f}"


if __name__ == "__main__":
    print(solve())
