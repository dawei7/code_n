"""Project Euler Problem 531: Chinese Leftovers.

Find sum_{10^6 <= n < m < 10^6 + 5000} f(n, m), where f(n, m) = g(phi(n), n, phi(m), m)
and g(a, n, b, m) is the smallest non-negative solution to x = a (mod n) and x = b (mod m).
"""

from typing import List, Tuple


def _egcd(a: int, b: int) -> Tuple[int, int, int]:
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def _g_crt(a: int, n: int, b: int, m: int) -> int:
    g, u, _ = _egcd(n, m)
    diff = b - a
    if diff % g != 0:
        return 0
    m_div_g = m // g
    k = ((diff // g) * u) % m_div_g
    x = a + n * k
    lcm = n * m_div_g
    return x % lcm


def solve(low: int = 1000000, high: int = 1005000) -> int:
    """Compute sum_{low <= n < m < high} g(phi(n), n, phi(m), m) using extended GCD CRT."""
    phi: List[int] = list(range(high))
    for i in range(2, high):
        if phi[i] == i:
            for j in range(i, high, i):
                phi[j] -= phi[j] // i

    total = 0
    for n in range(low, high):
        phi_n = phi[n]
        for m in range(n + 1, high):
            phi_m = phi[m]
            total += _g_crt(phi_n, n, phi_m, m)

    return total


if __name__ == "__main__":
    print(solve())
