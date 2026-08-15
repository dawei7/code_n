"""Project Euler Problem 498: Remainder of Polynomial Division.

Find C(10^13, 10^12, 10^4) mod 999999937, where C(n, m, d) is the absolute value
of the d-th degree coefficient of the remainder of x^n divided by (x - 1)^m.
"""

MOD = 999999937


def _binom_small(n: int, k: int, p: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if k > n - k:
        k = n - k

    num = 1
    den = 1
    for i in range(k):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p

    return (num * pow(den, p - 2, p)) % p


def solve(
    n: int = 10**13,
    m: int = 10**12,
    d: int = 10**4,
    mod: int = MOD,
) -> int:
    """Compute C(n, m, d) mod mod using combinatorial identity C = binom(n, d) * binom(n-d-1, m-1-d) and Lucas Theorem."""
    total_c = 1
    pairs = [(n, d), (n - d - 1, m - 1 - d)]

    for big_n, big_k in pairs:
        res = 1
        cur_n, cur_k = big_n, big_k
        while cur_n > 0 or cur_k > 0:
            ni = cur_n % mod
            ki = cur_k % mod
            if ki > ni:
                res = 0
                break
            res = (res * _binom_small(ni, ki, mod)) % mod
            cur_n //= mod
            cur_k //= mod
        total_c = (total_c * res) % mod

    return total_c


if __name__ == "__main__":
    print(solve())
