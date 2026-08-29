"""Project Euler Problem 599: Distinct Colourings of a Rubik's Cube.

Find the number of essentially distinct colourings of a 2x2x2 Rubik's cube with 10 colours.
"""

from math import comb, factorial
from typing import List


def _unsigned_stirling_first_kind(n: int) -> List[int]:
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            dp[i][k] = dp[i - 1][k - 1] + (i - 1) * dp[i - 1][k]
    return dp[n]


def _count_sequences_12_sum0(max_len: int) -> List[int]:
    dp = [[0, 0, 0] for _ in range(max_len + 1)]
    dp[0][0] = 1
    for r in range(max_len):
        for s in range(3):
            dp[r + 1][(s + 1) % 3] += dp[r][s]
            dp[r + 1][(s + 2) % 3] += dp[r][s]
    return [dp[r][0] for r in range(max_len + 1)]


def solve(n: int = 10) -> int:
    """Compute number of distinct colourings using Burnside's Lemma on wreath product S_8 wr Z_3."""
    c8 = _unsigned_stirling_first_kind(8)
    b_arr = _count_sequences_12_sum0(8)

    numerator = 0
    for m in range(1, 9):
        factor = 3 ** (8 - m)
        term_m = 0
        for z in range(m + 1):
            r = m - z
            count_vectors = comb(m, z) * b_arr[r]
            cycles_on_stickers = m + 2 * z
            term_m += count_vectors * (n**cycles_on_stickers)
        numerator += c8[m] * factor * term_m

    denom = factorial(8) * (3**7)
    return numerator // denom


if __name__ == "__main__":
    print(solve())
