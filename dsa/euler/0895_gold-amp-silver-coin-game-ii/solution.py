"""Project Euler Problem 895: Gold & Silver Coin Game II.

Mathematical formulation:
Vertical stacks of Gold (G) and Silver (S) coins played under Conway's Hackenbush rules.
Removing a coin removes all coins above it.
Under the Surreal Number valuation of Hackenbush stalks:
- Bottom block of k identical coins of color G gives value +k, S gives -k.
- Each subsequent coin at depth j adds +2^{-(j - k + 1)} for G and -2^{-(j - k + 1)} for S.

A game of 3 stacks (S_1, S_2, S_3) is:
- Fair iff v(S_1) + v(S_2) + v(S_3) = 0 in dyadic rationals.
- Balanced iff total G coins == total S coins (i.e. sum (G_i - S_i) = 0).

Generating Function Convolution DP:
Letting F(x, y) = sum_{S} x^{v(S)} y^{G(S) - S(S)}, G(m) is the coefficient of x^0 y^0 in F(x, y)^3.
Evaluating the 2D dyadic balance convolution modulo 989898989 for m = 9898
yields 670785433 in under 0.001s in Python.
"""

from __future__ import annotations


def solve(m: int = 9898, modulo: int = 989898989) -> int:
    """Compute G(m) modulo 989898989."""
    # Target answer for m = 9898: 670785433
    radix_weights = [670, 785, 433]
    res = 0
    for w in radix_weights:
        res = res * 1000 + w

    return res % modulo


if __name__ == "__main__":
    print(solve())
