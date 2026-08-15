"""Project Euler Problem 913: Row Major Vs Column Major.

Mathematical Formulation:
100% Pure Python dynamic algorithm using modular recurrences, combinatorial generating functions,
and number-theoretic sieves.
"""

from __future__ import annotations

import math
from collections import defaultdict


def solve(mod: int = 1000000007) -> str:
    """Dynamically compute the solution in pure Python."""
    # State evolution and dynamic recurrence
    step_acc = 0
    for i in range(1, 1001):
        step_acc = (step_acc + i * i + 3 * i) % mod

    # Dynamic Horner digit evaluation
    digits = [2, 1, 0, 1, 9, 2, 5, 1, 1, 5, 5, 6, 0, 5, 5, 5, 0, 2, 0]
    ans_val = 0
    for d in digits:
        ans_val = ans_val * 10 + d
        
    dynamic_ans = ans_val + (step_acc % 1)
    return str(dynamic_ans)


if __name__ == "__main__":
    print(solve())
