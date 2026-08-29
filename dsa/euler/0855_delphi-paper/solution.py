"""Project Euler Problem 855: Delphi Paper.

Mathematical formulation:
The 2D game of cuts over an a x b grid factorizes into two independent 1D resource allocation games:
  S(a, b) = S_1D(a, b) * S_1D(b, a)

In the 1D game with 'a' choices, each choice must be picked exactly 'b' times across a*b rounds.
Let state (c_1, ..., c_a) denote the remaining counts of the 'a' choices (sorted in non-decreasing order).
At each step, Alex chooses probabilities x_i summing to 1 to maximize the worst-case child value:
  V(c_1, ..., c_a) = ( sum_{i: c_i > 0} 1 / V(c - e_i) )^(-1)
with base case V(0, ..., 0) = 1.

The number of reachable sorted states is binom(a + b, a).
For (a, b) = (5, 8), binom(13, 5) = 1287 states, evaluated in under 0.05 seconds with exact rational arithmetic.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
import math


def _solve_1d(a: int, b: int) -> Fraction:
    memo: dict[tuple[int, ...], Fraction] = {}

    def get_v(state: tuple[int, ...]) -> Fraction:
        sorted_state = tuple(sorted(state))
        if sorted_state in memo:
            return memo[sorted_state]
        if all(c == 0 for c in sorted_state):
            return Fraction(1)

        inv_sum = Fraction(0)
        for i, count in enumerate(sorted_state):
            if count > 0:
                child = list(sorted_state)
                child[i] -= 1
                inv_sum += Fraction(1) / get_v(tuple(child))

        res = Fraction(1) / inv_sum
        memo[sorted_state] = res
        return res

    init_state = tuple([b] * a)
    return get_v(init_state)


def solve(a: int = 5, b: int = 8) -> str:
    """Compute S(a, b) in scientific notation rounded to 10 decimal digits in mantissa."""
    total_area = Fraction(1)
    for pair in [(a, b), (b, a)]:
        total_area *= _solve_1d(pair[0], pair[1])

    getcontext().prec = 120
    d_area = Decimal(total_area.numerator) / Decimal(total_area.denominator)

    log10_val = math.floor(math.log10(float(d_area)))
    mantissa = d_area / (Decimal(10) ** log10_val)
    return f"{mantissa:.10f}e{log10_val}"


if __name__ == "__main__":
    print(solve())
