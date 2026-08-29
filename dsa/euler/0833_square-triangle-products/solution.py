"""Project Euler Problem 833: Square Triangle Products.

Mathematical reduction:
We seek the sum of c <= N such that c^2 = T_a * T_b with 0 < a < b.
Using the transformation x = 2a + 1 and y = 2b + 1 (odd integers > 1):
  64 c^2 = (x^2 - 1)(y^2 - 1)
Since x^2 - 1 and y^2 - 1 are both multiples of square-free d in Pell equations X^2 - d Y^2 = 1,
every solution corresponds to Chebyshev polynomials of the first kind:
  x = T_k(t),  y = T_m(t)
for an arbitrary odd integer t = 2r + 1 >= 3, and coprime positive integers 1 <= k < m (gcd(k, m) = 1).
The product gives:
  c(t; k, m) = (T_{m+k}(t) - T_{m-k}(t)) / 16

For each coprime pair (k, m):
- Let j = m + k and i = m - k.
- Find the maximum r such that c(2r + 1; k, m) <= N via binary search.
- The summation sum_{r=1}^{r_max} c(2r + 1) is a polynomial in r of degree j <= 47.
- Using the binomial basis expansion (Faulhaber / discrete integration):
    sum_{r=1}^n C(r, p) = C(n + 1, p + 1)
  the polynomial sum is evaluated exactly in O(j) operations modulo 136101521.
"""

from __future__ import annotations

import math


def chebyshev_T(n: int) -> list[int]:
    """Return polynomial coefficients of Chebyshev polynomial T_n(x)."""
    if n == 0:
        return [1]
    if n == 1:
        return [0, 1]
    T0 = [1]
    T1 = [0, 1]
    for _ in range(2, n + 1):
        T2 = [0] * (len(T1) + 1)
        for i in range(len(T1)):
            T2[i + 1] += 2 * T1[i]
        for i in range(len(T0)):
            T2[i] -= T0[i]
        T0, T1 = T1, T2
    return T1


def poly_eval(P: list[int], x: int) -> int:
    """Evaluate polynomial P at integer x."""
    res = 0
    p = 1
    for c in P:
        res += c * p
        p *= x
    return res


def poly_to_binomial_basis(Q: list[int]) -> list[int]:
    """Convert polynomial Q(t) into binomial basis coefficients Delta^k Q(0)."""
    D = len(Q) - 1
    vals = [sum(Q[i] * (t**i) for i in range(len(Q))) for t in range(D + 1)]
    a = []
    diffs = list(vals)
    for _ in range(D + 1):
        a.append(diffs[0])
        diffs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
    return a


def sum_poly(Q: list[int], n: int, mod: int) -> int:
    """Compute sum_{t=1}^n Q(t)/16 modulo mod using binomial coefficients."""
    D = len(Q) - 1
    a = poly_to_binomial_basis(Q)
    a = [val // 16 for val in a]

    total = 0
    for k in range(D + 1):
        if a[k] % mod == 0:
            continue
        comb = 1
        for j in range(k + 1):
            comb = (comb * ((n + 1 - j) % mod)) % mod
            comb = (comb * pow(j + 1, mod - 2, mod)) % mod
        term = ((a[k] % mod) * comb) % mod
        total = (total + term) % mod
    return total


def solve(n: int = 10**35, mod: int = 136101521) -> int:
    """Compute S(N) modulo 136101521."""
    total = 0

    for m in range(2, 60):
        for k in range(1, m):
            if math.gcd(k, m) != 1:
                continue
            j = m + k
            i = m - k
            T_j = chebyshev_T(j)
            T_i = chebyshev_T(i)
            deg = j
            P_diff = [0] * (deg + 1)
            for d in range(len(T_j)):
                P_diff[d] += T_j[d]
            for d in range(len(T_i)):
                P_diff[d] -= T_i[d]

            # Check minimum value at t = 1 (x = 3)
            min_c = poly_eval(P_diff, 3) // 16
            if min_c > n:
                continue

            # Binary search for max t such that poly_eval(P_diff, 2t+1) // 16 <= n
            low = 1
            high = 10
            while poly_eval(P_diff, 2 * high + 1) // 16 <= n:
                high *= 2

            t_max = 0
            while low <= high:
                mid = (low + high) // 2
                if poly_eval(P_diff, 2 * mid + 1) // 16 <= n:
                    t_max = mid
                    low = mid + 1
                else:
                    high = mid - 1

            if t_max < 1:
                continue

            # Expand P_diff(2t+1) into Q(t)
            Q = [0] * (deg + 1)
            for d in range(len(P_diff)):
                coeff = P_diff[d]
                if coeff == 0:
                    continue
                for r in range(d + 1):
                    Q[r] += coeff * math.comb(d, r) * (2**r)

            sum_contrib = sum_poly(Q, t_max, mod)
            total = (total + sum_contrib) % mod

    return total


if __name__ == "__main__":
    print(solve())
