"""Project Euler 259: Reachable Numbers

Find the sum of all positive reachable integers obtained by arithmetic expressions
using digits 1 through 9 in order with +, -, *, /, parentheses, and concatenation.
"""

from __future__ import annotations

import math


def solve() -> str:
    """Computes the sum of all positive reachable integers using interval DP

    with rational arithmetic.
    """
    memo: dict[tuple[int, int], set[tuple[int, int]]] = {}

    def get_rationals(i: int, j: int) -> set[tuple[int, int]]:
        if (i, j) in memo:
            return memo[(i, j)]

        # Base case: concatenated number
        val = 0
        for d in range(i, j + 1):
            val = val * 10 + d
        res: set[tuple[int, int]] = {(val, 1)}

        # Split across all binary partition points k in [i, j-1]
        for k in range(i, j):
            left_vals = get_rationals(i, k)
            right_vals = get_rationals(k + 1, j)

            for p1, q1 in left_vals:
                for p2, q2 in right_vals:
                    # Addition: p1/q1 + p2/q2
                    p_add = p1 * q2 + p2 * q1
                    q_add = q1 * q2
                    g = math.gcd(p_add, q_add)
                    res.add((p_add // g, q_add // g))

                    # Subtraction: p1/q1 - p2/q2
                    p_sub = p1 * q2 - p2 * q1
                    q_sub = q1 * q2
                    g = math.gcd(p_sub, q_sub)
                    res.add((p_sub // g, q_sub // g))

                    # Multiplication: p1/q1 * p2/q2
                    p_mul = p1 * p2
                    q_mul = q1 * q2
                    g = math.gcd(p_mul, q_mul)
                    res.add((p_mul // g, q_mul // g))

                    # Division: (p1/q1) / (p2/q2)
                    if p2 != 0:
                        p_div = p1 * q2
                        q_div = q1 * p2
                        if q_div < 0:
                            p_div, q_div = -p_div, -q_div
                        g = math.gcd(p_div, q_div)
                        res.add((p_div // g, q_div // g))

        memo[(i, j)] = res
        return res

    all_vals = get_rationals(1, 9)
    reachable_pos_ints = {p for (p, q) in all_vals if q == 1 and p > 0}
    return str(sum(reachable_pos_ints))


if __name__ == "__main__":
    print(solve())
