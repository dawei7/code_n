"""Project Euler Problem 612: Friend Numbers.

Find f(10^18) mod 1000267129, where f(n) is the number of pairs 1 <= p < q < n
that share at least one common decimal digit.
"""

from typing import List

_MOD = 1000267129
_INV2 = (_MOD + 1) // 2


def _count_masks_upto(n_digits: int) -> List[int]:
    n_counts = [0] * 1024
    for mask in range(1, 1024):
        size = bin(mask).count("1")
        nonzeros = bin(mask & ~1).count("1")
        if nonzeros == 0:
            continue
        total = 0
        p = 1
        for _ in range(1, n_digits + 1):
            total = (total + nonzeros * p) % _MOD
            p = (p * size) % _MOD
        n_counts[mask] = total

    c_counts = [0] * 1024
    for m in range(1, 1024):
        m_size = bin(m).count("1")
        s = m
        tot = 0
        while s > 0:
            s_size = bin(s).count("1")
            sign = -1 if ((m_size - s_size) & 1) else 1
            tot = (tot + sign * n_counts[s]) % _MOD
            s = (s - 1) & m
        c_counts[m] = tot
    return c_counts


def solve(n_digits: int = 18) -> int:
    """Compute f(10^n_digits) modulo 1000267129 using digit subset inclusion-exclusion."""
    c_counts = _count_masks_upto(n_digits)

    non_friends = 0
    for m1 in range(1, 1024):
        c1 = c_counts[m1]
        if not c1:
            continue
        comp = (~m1) & 1023
        sub = comp
        sum_c2 = 0
        while sub > 0:
            sum_c2 = (sum_c2 + c_counts[sub]) % _MOD
            sub = (sub - 1) & comp
        non_friends = (non_friends + c1 * sum_c2) % _MOD

    non_friends = (non_friends * _INV2) % _MOD

    total_nums = (pow(10, n_digits, _MOD) - 1) % _MOD
    total_pairs = (total_nums * (total_nums - 1) % _MOD * _INV2) % _MOD

    return (total_pairs - non_friends) % _MOD


if __name__ == "__main__":
    print(solve())
