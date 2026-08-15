"""Project Euler Problem 554: Centaurs on a Chess Board.

Find sum_{i=2..90} C(F_i) mod 10^8+7, where C(n) is the number of ways to place
n^2 non-attacking centaurs on a 2n x 2n chess board.
"""

from typing import Dict, List, Set

MOD = 100_000_007  # 10^8 + 7 (prime)


def _fib_upto(n: int) -> List[int]:
    f = [0, 1]
    for _ in range(2, n + 1):
        f.append(f[-1] + f[-2])
    return f


def _gather_needed_factorials(ns: List[int]) -> List[int]:
    need: Set[int] = {0, 1}
    p = MOD

    for n in ns:
        big_n = 2 * n
        big_k = n
        while big_n or big_k:
            ni = big_n % p
            ki = big_k % p
            if ki <= ni:
                need.add(ni)
                need.add(ki)
                need.add(ni - ki)
            big_n //= p
            big_k //= p

    return sorted(need)


def _compute_sparse_factorials(targets: List[int]) -> Dict[int, int]:
    if not targets or targets[0] != 0:
        raise ValueError("targets must include 0")

    p = MOD
    max_idx = targets[-1]
    fact: Dict[int, int] = {0: 1}

    j = 1
    next_t = targets[j] if j < len(targets) else None

    f = 1
    for i in range(1, max_idx + 1):
        f = (f * i) % p
        if next_t is not None and i == next_t:
            fact[i] = f
            j += 1
            next_t = targets[j] if j < len(targets) else None

    return fact


def _small_binom(
    n: int, k: int, fact: Dict[int, int], invfact: Dict[int, int]
) -> int:
    if k < 0 or k > n:
        return 0
    return (fact[n] * invfact[k] % MOD) * invfact[n - k] % MOD


def _lucas_binom(
    big_n: int, big_k: int, fact: Dict[int, int], invfact: Dict[int, int]
) -> int:
    p = MOD
    res = 1
    while big_n or big_k:
        ni = big_n % p
        ki = big_k % p
        if ki > ni:
            return 0
        res = (res * _small_binom(ni, ki, fact, invfact)) % p
        big_n //= p
        big_k //= p
    return res


def _c_mod(n: int, fact: Dict[int, int], invfact: Dict[int, int]) -> int:
    b = _lucas_binom(2 * n, n, fact, invfact)
    nn = n % MOD
    poly = (3 * nn * nn + 2 * nn + 7) % MOD
    return (8 * b - poly) % MOD


def solve(max_i: int = 90) -> int:
    """Compute sum_{i=2..max_i} C(F_i) mod MOD using Lucas' theorem and sparse factorials."""
    fib = _fib_upto(max_i)
    ns = [fib[i] for i in range(2, max_i + 1)]

    targets = _gather_needed_factorials(ns)
    fact = _compute_sparse_factorials(targets)
    invfact = {x: pow(fact[x], MOD - 2, MOD) for x in fact}

    ans = 0
    for i in range(2, max_i + 1):
        ans = (ans + _c_mod(fib[i], fact, invfact)) % MOD

    return ans


if __name__ == "__main__":
    print(solve())
