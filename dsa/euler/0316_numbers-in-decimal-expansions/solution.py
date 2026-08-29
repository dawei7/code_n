"""Project Euler 316: Numbers in Decimal Expansions

Find sum_{n=2}^{999999} g(floor(10^16 / n)), where g(N) is the expected starting index of N
in an infinite sequence of uniform random decimal digits.
"""

from __future__ import annotations


def solve(limit_n: int = 999_999, exp: int = 16) -> str:
    """Calculates sum_{n=2}^{limit_n} g(floor(10^exp / n)) using the Martingale stopping theorem /

    Guibas-Odlyzko border formula: g(S) = sum_{i in Borders(S)} 10^i - len(S) + 1.
    """
    m = 10**exp
    pow10 = [10**i for i in range(25)]

    total_g = 0
    for n in range(2, limit_n + 1):
        val = m // n
        s = str(val)
        d = len(s)

        # Full length border i = d is always present: contributes 10^d - d + 1
        total_g += pow10[d] - d + 1

        # Check proper borders 1 <= i < d
        for i in range(1, d):
            if s[:i] == s[d - i :]:
                total_g += pow10[i]

    return str(total_g)


if __name__ == "__main__":
    print(solve())
