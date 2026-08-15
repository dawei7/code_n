"""Project Euler Problem 652: Distinct Values of a Proto-logarithmic Function.

Find the last 9 digits of D(10^18), where D(N) is the number of distinct values
that any proto-logarithmic function attains over 2 <= m, n <= N.
"""

from math import gcd
from typing import List

_MOD = 1_000_000_000


def _integer_kth_root(n: int, k: int) -> int:
    if k <= 1:
        return n
    if n < 2:
        return n
    high = 1 << ((n.bit_length() + k - 1) // k)
    low = 1
    while low + 1 < high:
        mid = (low + high) // 2
        if pow(mid, k) <= n:
            low = mid
        else:
            high = mid
    return low


def _mobius_upto(n: int) -> List[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes = []
    is_comp = [False] * (n + 1)
    for i in range(2, n + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            v = i * p
            if v > n:
                break
            is_comp[v] = True
            if i % p == 0:
                mu[v] = 0
                break
            mu[v] = -mu[i]
    return mu


def _totients_prefix(n: int) -> List[int]:
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + phi[i]
    return pref


def _primitive_count(x: int, mu: List[int]) -> int:
    if x < 2:
        return 0
    k_max = x.bit_length() - 1
    s = 0
    for d in range(1, k_max + 1):
        md = mu[d]
        if md != 0:
            s += md * (_integer_kth_root(x, d) - 1)
    return s


def solve(n: int = 10**18) -> int:
    """Compute D(N) mod 10^9 using primitive root Mobius inversion and coprime rational/irrational decomposition."""
    if n < 2:
        return 0

    l_max = n.bit_length() - 1
    mu = _mobius_upto(l_max)
    phisum = _totients_prefix(l_max)

    rational = 2 * phisum[l_max] - 1

    root_n = [0] * (l_max + 2)
    for e in range(1, l_max + 2):
        root_n[e] = _integer_kth_root(n, e)

    p_arr = [0] * (l_max + 2)
    for e in range(1, l_max + 2):
        p_arr[e] = _primitive_count(root_n[e], mu)

    count = [0] * (l_max + 1)
    for e in range(1, l_max + 1):
        count[e] = p_arr[e]

    t_total = 0
    for e in range(1, l_max + 1):
        ce = count[e]
        if ce == 0:
            continue
        for f in range(1, l_max + 1):
            if gcd(e, f) == 1:
                t_total += ce * count[f]

    s_diag = 0
    for k in range(1, l_max + 1):
        num_roots_with_k = p_arr[k] - p_arr[k + 1]
        coprime_pairs_upto_k = 2 * phisum[k] - 1
        s_diag += num_roots_with_k * coprime_pairs_upto_k

    irrational = t_total - s_diag
    ans = (rational + irrational) % _MOD
    return ans


if __name__ == "__main__":
    print(solve())
