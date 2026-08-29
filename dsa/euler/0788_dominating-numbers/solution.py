"""Project Euler Problem 788: Dominating Numbers.

Find D(2022) modulo 10^9+7, the count of dominating numbers less than 10^N,
where a dominating number has strictly more than half of its digits equal.
"""

_MOD = 1_000_000_007


def solve(N: int = 2022, mod: int = _MOD) -> int:
    """Compute D(N) mod 10^9+7 using exact binomial digit distribution counting."""
    fact = [1] * (N + 1)
    inv = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % mod
    inv[N] = pow(fact[N], mod - 2, mod)
    for i in range(N, 0, -1):
        inv[i - 1] = (inv[i] * i) % mod

    def comb(n: int, k: int) -> int:
        if k < 0 or k > n:
            return 0
        return fact[n] * inv[k] % mod * inv[n - k] % mod

    pow9 = [1] * (N + 1)
    for i in range(1, N + 1):
        pow9[i] = (pow9[i - 1] * 9) % mod

    total = 0
    for L in range(1, N + 1):
        for k in range(L // 2 + 1, L + 1):
            term1 = comb(L - 1, k - 1) * pow9[L - k] % mod
            term2 = 8 * comb(L - 1, k) * pow9[L - 1 - k] % mod if L - 1 >= k else 0
            ways_nonzero = 9 * (term1 + term2) % mod

            ways_zero = comb(L - 1, k) * pow9[L - k] % mod if L - 1 >= k else 0

            total = (total + ways_nonzero + ways_zero) % mod

    return total


if __name__ == "__main__":
    print(solve())
