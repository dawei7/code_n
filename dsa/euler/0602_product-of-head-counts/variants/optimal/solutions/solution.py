"""Project Euler Problem 602: Product of Head Counts.

Find c(10^7, 4*10^6) mod 1000000007, where c(n, k) is the coefficient of p^k
in the expected value polynomial e(n, p) of the head-count product.
"""

_MOD = 1000000007


def solve(n: int = 10_000_000, k: int = 4_000_000) -> int:
    """Compute c(n, k) modulo 1000000007 using the explicit Eulerian number formula."""
    inv = [0] * (k + 2)
    inv[1] = 1
    for i in range(2, k + 2):
        inv[i] = (_MOD - (_MOD // i)) * inv[_MOD % i] % _MOD

    total = 0
    binom = 1
    for j in range(k + 1):
        term = (binom * pow(k - j, n, _MOD)) % _MOD
        if j & 1:
            total = (total - term) % _MOD
        else:
            total = (total + term) % _MOD
        if j < k:
            binom = (binom * (n + 1 - j) % _MOD) * inv[j + 1] % _MOD

    return total


if __name__ == "__main__":
    print(solve())
