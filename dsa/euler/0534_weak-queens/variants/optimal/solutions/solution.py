"""Project Euler Problem 534: Weak Queens.

Find S(14), where S(n) = sum_{w=0..n-1} Q(n, w), and Q(n, w) is the number of ways
to place n weak queens with weakness factor w on an n x n board without conflicts.
"""

from collections import defaultdict
from typing import Dict, List


def _nqueens_count_classic(n: int) -> int:
    all_mask = (1 << n) - 1

    def rec(cols: int, d1: int, d2: int) -> int:
        if cols == all_mask:
            return 1
        total = 0
        avail = all_mask & ~(cols | d1 | d2)
        while avail:
            bit = avail & -avail
            avail -= bit
            total += rec(
                cols | bit,
                ((d1 | bit) << 1) & all_mask,
                (d2 | bit) >> 1,
            )
        return total

    half = n // 2
    total = 0
    for col in range(half):
        bit = 1 << col
        total += rec(bit, (bit << 1) & all_mask, bit >> 1)
    total *= 2
    if n % 2 == 1:
        col = half
        bit = 1 << col
        total += rec(bit, (bit << 1) & all_mask, bit >> 1)
    return total


def _count_by_l(n: int, attack_l: int) -> int:
    if attack_l <= 0:
        return pow(n, n)
    if attack_l >= n - 1:
        return _nqueens_count_classic(n)

    all_cols_mask = (1 << n) - 1
    shift = 4
    keep_mask = (1 << (shift * attack_l)) - 1

    attack: List[List[int]] = [[0] * (attack_l + 1) for _ in range(n)]
    for c in range(n):
        for d in range(1, attack_l + 1):
            m = 1 << c
            cp = c + d
            if cp < n:
                m |= 1 << cp
            cm = c - d
            if cm >= 0:
                m |= 1 << cm
            attack[c][d] = m

    def dp_from_first_cols(first_cols) -> int:
        states: Dict[int, int] = defaultdict(int)
        for c0 in first_cols:
            states[c0] += 1

        for r in range(1, n):
            m_prev = r if r < attack_l else attack_l
            nxt: Dict[int, int] = defaultdict(int)
            mask_needed = r + 1 >= attack_l

            for state, cnt in states.items():
                forbid = 0
                s = state
                i = 1
                while i <= m_prev:
                    pc = s & 0xF
                    s >>= shift
                    forbid |= attack[pc][i]
                    i += 1

                avail = all_cols_mask & ~forbid
                while avail:
                    bit = avail & -avail
                    avail -= bit
                    col = bit.bit_length() - 1
                    ns = (state << shift) | col
                    if mask_needed:
                        ns &= keep_mask
                    nxt[ns] += cnt

            states = nxt

        return sum(states.values())

    half = n // 2
    left_count = dp_from_first_cols(range(half))
    if n % 2 == 0:
        return 2 * left_count
    return 2 * left_count + dp_from_first_cols([half])


def solve(n: int = 14) -> int:
    """Compute S(n) = sum_{w=0..n-1} Q(n, w) using sliding window DP and symmetry."""
    total = 0
    for w in range(n):
        attack_l = n - 1 - w
        total += _count_by_l(n, attack_l)
    return total


if __name__ == "__main__":
    print(solve())
