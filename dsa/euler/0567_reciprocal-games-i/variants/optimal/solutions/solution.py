"""Project Euler Problem 567: Reciprocal Games I.

Find S(123456789) rounded to 8 decimal places, where S(m) = sum_{n=1..m} (J_A(n) + J_B(n)),
and J_A(n), J_B(n) are expected wins in the reciprocal light bulb games.
"""

import math

_EULER_GAMMA = 0.57721566490153286060651209008240243104215933593992


def _harmonic(n: int) -> float:
    if n < 100_000:
        return sum(1.0 / k for k in range(1, n + 1))

    x = float(n)
    inv = 1.0 / x
    inv2 = inv * inv
    return (
        math.log(x)
        + _EULER_GAMMA
        + 0.5 * inv
        - inv2 / 12.0
        + (inv2 * inv2) / 120.0
        - (inv2 * inv2 * inv2) / 252.0
        + (inv2 * inv2 * inv2 * inv2) / 240.0
    )


def _j_a(n: int) -> float:
    if n <= 200:
        p = math.ldexp(1.0, -n)
        s = 0.0
        for k in range(1, n + 1):
            s += (math.comb(n, k) * p) / k
        return s

    s = 0.0
    for j in range(0, 81):
        s += math.ldexp(1.0, -j) / (n - j)
    h = _harmonic(n)
    s -= math.ldexp(h, -n)
    return s


def _j_b(n: int) -> float:
    if n <= 200:
        s = 0.0
        for k in range(1, n + 1):
            s += 1.0 / (k * math.comb(n, k))
        return s

    big_n = n - 1
    inv = 1.0
    edge_sum = inv
    for j in range(1, 26):
        inv *= j / (big_n - j + 1)
        edge_sum += inv
    return (2.0 * edge_sum) / n


def solve(m: int = 123_456_789) -> str:
    """Compute S(m) in O(1) time using harmonic telescope reduction and Euler-Maclaurin expansion."""
    h = _harmonic(m)

    # sum_{i=1..m} 2^{-i} / i
    pow2_sum = 0.0
    for i in range(1, min(m, 60) + 1):
        pow2_sum += math.ldexp(1.0, -i) / i

    ans = 4.0 * h - 2.0 * pow2_sum - (_j_a(m) + _j_b(m))
    return f"{ans:.8f}"


if __name__ == "__main__":
    print(solve())
