"""Project Euler Problem 546: The Floor's Revenge.

Find sum_{k=2..10} f_k(10^14) mod 10^9+7, where f_k(n) = sum_{i=0..n} f_k(floor(i/k))
with f_k(0) = 1.
"""

from typing import List

MOD = 1_000_000_007


def _build_coeffs(k: int, max_j: int) -> List[List[List[int]]]:
    coeffs: List[List[List[int]]] = [[] for _ in range(max_j + 1)]

    coeffs[0] = [[] for _ in range(k)]
    for r in range(k):
        coeffs[0][r] = [(r + 1 - k) % MOD, k % MOD]

    for j in range(1, max_j + 1):
        coeffs[j] = [[] for _ in range(k)]
        a = coeffs[j - 1]

        totals = [0] * (j + 1)
        for u in range(k):
            au = a[u]
            for p in range(j + 1):
                totals[p] = (totals[p] + au[p]) % MOD

        prefix = [[0] * (j + 1) for _ in range(k)]
        run = [0] * (j + 1)
        for u in range(k):
            au = a[u]
            for p in range(j + 1):
                run[p] = (run[p] + au[p]) % MOD
                prefix[u][p] = run[p]

        for r in range(k):
            pref = prefix[r]
            b = [0] * (j + 2)
            b[0] = (pref[0] - totals[0]) % MOD
            for p in range(1, j + 1):
                b[p] = (pref[p] - totals[p] + totals[p - 1]) % MOD
            b[j + 1] = totals[j] % MOD
            coeffs[j][r] = b

    return coeffs


def _prepare_factorials(nmax: int) -> tuple[List[int], List[int]]:
    fact = [1] * (nmax + 1)
    for i in range(1, nmax + 1):
        fact[i] = fact[i - 1] * i % MOD
    invfact = [1] * (nmax + 1)
    invfact[nmax] = pow(fact[nmax], MOD - 2, MOD)
    for i in range(nmax, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD
    return fact, invfact


def _n_choose_k(n: int, r: int, fact: List[int], invfact: List[int]) -> int:
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD


def _fk_mod(k: int, n: int) -> int:
    ns = [n]
    while ns[-1] >= k:
        ns.append(ns[-1] // k)
    d = len(ns) - 1

    coeffs = _build_coeffs(k, d)
    fact, invfact = _prepare_factorials((k - 1) + d + 10)

    base = ns[d]
    vec = [_n_choose_k(base + j + 1, j + 1, fact, invfact) for j in range(d + 1)]

    for i in range(d - 1, -1, -1):
        r = ns[i] % k
        m_vec = vec
        new = [0] * (i + 1)
        for j in range(i + 1):
            co = coeffs[j][r]
            s = 0
            for p, c in enumerate(co):
                s = (s + c * m_vec[p]) % MOD
            new[j] = s
        vec = new

    return vec[0]


def solve(n: int = 10**14, mod: int = MOD) -> int:
    """Compute sum_{k=2..10} f_k(n) mod mod using higher-order prefix sum lifting."""
    total = 0
    for k in range(2, 11):
        total = (total + _fk_mod(k, n)) % mod
    return total


if __name__ == "__main__":
    print(solve())
