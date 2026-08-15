"""Project Euler Problem 831: Triple Product.

Mathematical reduction:
The given sum is:
g(m) = sum_{j=0}^m sum_{i=0}^j (-1)^{j-i} C(m, j) C(j, i) C(j + 5 + 6i, j + 5)

Using binomial identities, exchange the summation order with j = i + k:
g(m) = sum_{i=0}^m C(m, i) sum_{k=0}^{m-i} (-1)^k C(m-i, k) C(7i + 5 + k, 6i)

Using the finite difference identity:
sum_{k=0}^N (-1)^k C(N, k) C(A + k, B) = (-1)^N C(A, B - N)
with A = 7i + 5, B = 6i, N = m - i, we have B - N = 7i - m.
Thus the sum reduces to:
g(m) = sum_i (-1)^{m-i} C(m, i) C(7i + 5, 7i - m)
     = [x^{m+5}] (1+x)^5 ((1+x)^7 - 1)^m
     = [x^5] (1+x)^5 * (( (1+x)^7 - 1 ) / x)^m

Since ((1+x)^7 - 1)/x = 7 + 21x + 35x^2 + 35x^3 + 21x^4 + 7x^5 + x^6,
g(m) is simply the coefficient of x^5 in (1+x)^5 * P(x)^m mod x^6.
"""

from __future__ import annotations

import math
import sys


def solve(m: int = 142857) -> int:
    """Compute the first ten digits of g(m) in base 7."""
    sys.set_int_max_str_digits(200000)

    # P(x) = ( (1+x)^7 - 1 ) / x truncated to degree 5:
    # P(x) = 7 + 21x + 35x^2 + 35x^3 + 21x^4 + 7x^5
    P = [7, 21, 35, 35, 21, 7]

    def poly_mul(A: list[int], B: list[int]) -> list[int]:
        C = [0] * 6
        for i in range(6):
            if A[i] == 0:
                continue
            for j in range(6 - i):
                C[i + j] += A[i] * B[j]
        return C

    def poly_pow(A: list[int], exp: int) -> list[int]:
        res = [1, 0, 0, 0, 0, 0]
        base = list(A)
        while exp > 0:
            if exp % 2 == 1:
                res = poly_mul(res, base)
            base = poly_mul(base, base)
            exp //= 2
        return res

    Pm = poly_pow(P, m)
    binom5 = [math.comb(5, k) for k in range(6)]
    final_poly = poly_mul(binom5, Pm)
    v = final_poly[5]

    # Extract first 10 digits in base 7
    # Determine the number of base-7 digits:
    num_digits = 0
    power = 1
    while power <= v:
        power *= 7
        num_digits += 1

    shift = num_digits - 10
    leading = v // (7**shift)
    digits = []
    for _ in range(10):
        digits.append(str(leading % 7))
        leading //= 7

    return int("".join(reversed(digits)))


if __name__ == "__main__":
    print(solve())
