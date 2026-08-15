"""Project Euler Problem 746: A Messy Dinner.

Find S(2021) modulo 1000000007, where S(n) = sum_{k=2}^n M(k) and M(k) is the number
of ways to seat k families of 4 around a circular table of 4k seats alternating gender
such that no family sits together.
"""

_MOD = 1_000_000_007


def _build_factorials(n_max: int):
    fact = [1] * (n_max + 1)
    for i in range(1, n_max + 1):
        fact[i] = (fact[i - 1] * i) % _MOD
    invfact = [1] * (n_max + 1)
    invfact[n_max] = pow(fact[n_max], _MOD - 2, _MOD)
    for i in range(n_max, 0, -1):
        invfact[i - 1] = (invfact[i] * i) % _MOD
    return fact, invfact


def _nck(n: int, k: int, fact, invfact) -> int:
    if k < 0 or k > n:
        return 0
    return fact[n] * invfact[k] % _MOD * invfact[n - k] % _MOD


def _precompute_inverses(n_max: int):
    inv = [0] * (n_max + 1)
    inv[1] = 1
    for i in range(2, n_max + 1):
        inv[i] = _MOD - (_MOD // i) * inv[_MOD % i] % _MOD
    return inv


def _m_func(n: int, fact, invfact, inv, pow4) -> int:
    if n <= 1:
        return 0

    total = 0
    npk = 1

    for k in range(0, n + 1):
        if k > 0:
            npk = (npk * (n - (k - 1))) % _MOD

        if k == 0:
            d_val = 1
        else:
            d_val = (4 * n) % _MOD
            d_val = (d_val * inv[k]) % _MOD
            d_val = (d_val * _nck(4 * n - 3 * k - 1, k - 1, fact, invfact)) % _MOD

        rem = 2 * (n - k)
        ways_rest = fact[rem] * fact[rem] % _MOD
        term = npk
        term = (term * d_val) % _MOD
        term = (term * pow4[k]) % _MOD
        term = (term * ways_rest) % _MOD

        if k & 1:
            total = (total - term) % _MOD
        else:
            total = (total + term) % _MOD

    return (2 * total) % _MOD


def solve(target: int = 2021) -> int:
    """Compute S(target) modulo 1000000007 using circular interval inclusion-exclusion."""
    max_n = max(target, 10)
    fact, invfact = _build_factorials(4 * max_n)
    inv = _precompute_inverses(max_n)
    pow4 = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        pow4[i] = (pow4[i - 1] * 4) % _MOD

    acc = 0
    for k in range(2, target + 1):
        acc = (acc + _m_func(k, fact, invfact, inv, pow4)) % _MOD

    return acc


if __name__ == "__main__":
    print(solve())
