"""Project Euler Problem 380: Amazing Mazes!

Find C(100, 500), the number of distinct 100x500 mazes (spanning trees on grid graphs),
in scientific notation rounded to 5 significant digits.
"""

from math import floor, log10, pi, sin
from typing import List


def solve(m: int = 100, n: int = 500) -> str:
    """Compute the number of spanning trees on the m x n grid graph via Laplacian eigenvalues."""
    # Precompute sin^2 components for 1D Laplacian eigenvalues
    sin_m: List[float] = [sin(j * pi / (2 * m)) ** 2 for j in range(m)]
    sin_n: List[float] = [sin(k * pi / (2 * n)) ** 2 for k in range(n)]

    # Kirchhoff's theorem log10 sum:
    # log10(C) = (m*n - 1)*log10(4) - log10(m*n) + sum_{(j,k)!=(0,0)} log10(sin^2(j*pi/2m) + sin^2(k*pi/2n))
    log10_total = (m * n - 1) * log10(4.0) - log10(m * n)

    for j in range(m):
        sj = sin_m[j]
        for k in range(n):
            if j == 0 and k == 0:
                continue
            log10_total += log10(sj + sin_n[k])

    exponent = int(floor(log10_total))
    mantissa = 10.0 ** (log10_total - exponent)

    mantissa_str = f"{mantissa:.4f}"
    if float(mantissa_str) >= 10.0:
        mantissa /= 10.0
        exponent += 1
        mantissa_str = f"{mantissa:.4f}"

    return f"{mantissa_str}e{exponent}"


if __name__ == "__main__":
    print(solve())
