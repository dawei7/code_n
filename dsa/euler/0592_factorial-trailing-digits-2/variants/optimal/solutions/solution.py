"""Project Euler Problem 592: Factorial Trailing Digits 2.

Find f(20!), where f(N) is the last twelve hexadecimal digits before the
trailing zeroes in N!, formatted in uppercase.
"""

from typing import Dict, List

_MOD_BITS = 48
_MOD = 1 << _MOD_BITS
_PERIOD = 1 << (_MOD_BITS - 1)
_MAX_LOG = 24
_MAX_EXP = 60


def _v2_int(x: int) -> int:
    return (x & -x).bit_length() - 1


def _comb_small(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    res = 1
    for i in range(1, k + 1):
        res = res * (n - k + i) // i
    return res


def _precompute_stirling2(max_n: int) -> List[List[int]]:
    s = [[0] * (max_n + 1) for _ in range(max_n + 1)]
    s[0][0] = 1
    for n in range(1, max_n + 1):
        for k in range(1, n + 1):
            s[n][k] = s[n - 1][k - 1] + k * s[n - 1][k]
    return s


_STIRLING2 = _precompute_stirling2(_MAX_LOG)

_FACT = [1] * (_MAX_LOG + 1)
for i in range(1, _MAX_LOG + 1):
    _FACT[i] = _FACT[i - 1] * i

_BINOM = [[0] * (_MAX_LOG + 1) for _ in range(_MAX_LOG + 1)]
for n in range(_MAX_LOG + 1):
    _BINOM[n][0] = _BINOM[n][n] = 1
    for k in range(1, n):
        _BINOM[n][k] = _BINOM[n - 1][k - 1] + _BINOM[n - 1][k]

_FACT_V2 = [0] * (_MAX_EXP + 1)
_FACT_ODD_MOD = [1] * (_MAX_EXP + 1)
for n in range(1, _MAX_EXP + 1):
    t = _v2_int(n)
    _FACT_V2[n] = _FACT_V2[n - 1] + t
    _FACT_ODD_MOD[n] = (_FACT_ODD_MOD[n - 1] * (n >> t)) % _MOD

_FACT_ODD_INV = [0] * (_MAX_EXP + 1)
for n in range(0, _MAX_EXP + 1):
    _FACT_ODD_INV[n] = pow(_FACT_ODD_MOD[n], -1, _MOD)


def _power_sums_upto(n: int, max_p: int = _MAX_LOG) -> List[int]:
    comb_mod = [0] * (max_p + 2)
    for k in range(1, max_p + 2):
        comb_mod[k] = _comb_small(n, k) % _MOD

    sums = [0] * (max_p + 1)
    sums[0] = n % _MOD
    for p in range(1, max_p + 1):
        total = 0
        for t in range(0, p + 1):
            if _STIRLING2[p][t]:
                total = (
                    total
                    + (_STIRLING2[p][t] * _FACT[t] % _MOD) * comb_mod[t + 1]
                ) % _MOD
        sums[p] = total
    return sums


def _exp_principal_unit(x: int) -> int:
    x %= _MOD
    res = 1
    pow_x = 1

    for n in range(1, _MAX_EXP + 1):
        pow_x *= x
        v = _FACT_V2[n]
        shifted = (pow_x >> v) % _MOD
        term = (shifted * _FACT_ODD_INV[n]) % _MOD
        res = (res + term) % _MOD
        if term == 0:
            break

    return res


def _prod_first_r_odds(r: int, cache: Dict[int, int]) -> int:
    r %= _PERIOD
    if r in cache:
        return cache[r]

    sign_flip = (r // 2) & 1
    even_count = (r + 1) // 2
    odd_count = r // 2

    sums_even = _power_sums_upto(even_count, _MAX_LOG)
    sums_odd = _power_sums_upto(odd_count, _MAX_LOG)

    a_const = (1 << (_MOD_BITS - 2)) - 1
    a_pows = [1] * (_MAX_LOG + 1)
    a_mod = a_const % _MOD
    for i in range(1, _MAX_LOG + 1):
        a_pows[i] = (a_pows[i - 1] * a_mod) % _MOD

    log_sum = 0
    for m in range(1, _MAX_LOG + 1):
        sum_even = sums_even[m]
        sum_odd = 0
        for t in range(0, m + 1):
            c = _BINOM[m][t]
            term = c * a_pows[m - t]
            if t & 1:
                term = -term
            sum_odd = (sum_odd + term * sums_odd[t]) % _MOD

        sum_t = (sum_even + sum_odd) % _MOD

        twos = _v2_int(m)
        odd_m = m >> twos
        coef = (1 << (2 * m - twos)) % _MOD
        coef = (coef * pow(odd_m, -1, _MOD)) % _MOD
        if m % 2 == 0:
            coef = (-coef) % _MOD

        log_sum = (log_sum + coef * sum_t) % _MOD

    prod_u = _exp_principal_unit(log_sum)
    if sign_flip:
        prod_u = (-prod_u) % _MOD

    cache[r] = prod_u
    return prod_u


def _odd_part_factorial_mod(n: int, cache: Dict[int, int]) -> int:
    res = 1
    while n > 0:
        r = (n + 1) // 2
        res = (res * _prod_first_r_odds(r, cache)) % _MOD
        n //= 2
    return res


def solve(n_val: int = 20) -> str:
    """Compute f(n_val!) as 12 uppercase hexadecimal digits using 2-adic exp/log series."""
    # Compute n = n_val!
    n = 1
    for i in range(2, n_val + 1):
        n *= i

    cache: Dict[int, int] = {0: 1}
    odd_part = _odd_part_factorial_mod(n, cache)
    v2_mod4 = (n - n.bit_count()) & 3
    val = (odd_part * (1 << v2_mod4)) % _MOD
    return f"{val:012X}"


if __name__ == "__main__":
    print(solve())
