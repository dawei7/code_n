"""Project Euler Problem 462: Permutation of 3-smooth Numbers.

Find F(10^18), the number of permutations of 3-smooth numbers <= 10^18
in which each element comes after all of its proper divisors,
given in scientific notation rounded to 10 decimal places.
"""

from decimal import Decimal, getcontext
from math import factorial
from typing import List

getcontext().prec = 100


def _format_scientific(val: int) -> str:
    s_val = str(val)
    exp = len(s_val) - 1
    d_val = Decimal(val)
    mantissa = d_val / (Decimal(10) ** exp)
    rounded = round(mantissa, 10)
    if rounded >= 10:
        rounded = round(rounded / 10, 10)
        exp += 1
    return f"{rounded:.10f}e{exp}"


def solve(n_limit: int = 10**18) -> str:
    """Compute F(n_limit) via the Frame-Robinson-Thrall Hook Length Formula on Young diagrams."""
    row_lens: List[int] = []
    a = 0
    while (1 << a) <= n_limit:
        rem = n_limit // (1 << a)
        b = 0
        p3 = 1
        while p3 <= rem:
            b += 1
            p3 *= 3
        row_lens.append(b)
        a += 1

    max_b = max(row_lens) if row_lens else 0
    col_lens = [0] * max_b
    for b in range(max_b):
        col_lens[b] = sum(1 for r in row_lens if r > b)

    total_cells = sum(row_lens)
    num = factorial(total_cells)
    den = 1

    for row_idx in range(len(row_lens)):
        for col_idx in range(row_lens[row_idx]):
            hook = (
                (row_lens[row_idx] - col_idx)
                + (col_lens[col_idx] - row_idx)
                - 1
            )
            den *= hook

    ans_int = num // den
    return _format_scientific(ans_int)


if __name__ == "__main__":
    print(solve())
