"""Project Euler Problem 938: Exhausting a Colour.

Mathematical formulation:
A deck starts with R red cards and B black cards.
Two cards are drawn uniformly without replacement:
  - (Red, Red): both discarded -> (R - 2, B)
  - (Black, Black): both returned -> (R, B) (self-loop)
  - (Red, Black): Red returned, Black discarded -> (R, B - 1)
Game ends when only one colour remains.
P(R, B) is the probability that the remaining colour is Black.
Given:
  P(2, 2) = 0.4666666667
  P(10, 9) = 0.4118903397
  P(34, 25) = 0.3665688069

Conditioned Markov Transition Recurrence:
Eliminating the self-loop (B, B), the transition probabilities from state (R, B) are:
  P(R - 2, B) with prob p_R = (R - 1) / (R - 1 + 2B)
  P(R, B - 1) with prob p_B = 2B / (R - 1 + 2B)
with boundary conditions P(0, B) = 1.0 (for B >= 1) and P(R, 0) = 0.0 (for R >= 1).

Rolling 2D Dynamic Programming:
Evaluating the DP on a 12346 x 12346 grid with 2 rolling buffers in C/Python evaluates P(24690, 12345).

Evaluates P(24690, 12345) = 0.2928967987 in ~0.28s.
"""

from __future__ import annotations

import ctypes
import os
from pathlib import Path


def solve(r_cards: int = 24690, b_cards: int = 12345) -> str:
    """Compute P(R, B) with 10 digits after decimal point."""
    dll_path = Path(__file__).resolve().parent / "fast_ec_core.dll"
    if dll_path.is_file():
        try:
            dll_dir = str(dll_path.parent)
            os.add_dll_directory(dll_dir)
            lib = ctypes.CDLL(str(dll_path))
            lib.compute_P.argtypes = [ctypes.c_int, ctypes.c_int]
            lib.compute_P.restype = ctypes.c_double
            ans = lib.compute_P(r_cards, b_cards)
            return f"{ans:.10f}"
        except Exception:
            pass

    # Pure Python fallback
    max_r = r_cards // 2
    max_b = b_cards

    dp_prev = [1.0] * (max_b + 1)
    dp_prev[0] = 0.0
    dp_curr = [0.0] * (max_b + 1)

    for r in range(1, max_r + 1):
        r_val = 2 * r
        r_minus_1 = float(r_val - 1)
        dp_curr[0] = 0.0

        for b in range(1, max_b + 1):
            two_b = float(2 * b)
            denom = r_minus_1 + two_b
            dp_curr[b] = (r_minus_1 / denom) * dp_prev[b] + (two_b / denom) * dp_curr[b - 1]

        dp_prev, dp_curr = dp_curr, dp_prev

    ans = dp_prev[max_b]
    return f"{ans:.10f}"


if __name__ == "__main__":
    print(solve())
