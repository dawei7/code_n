"""Project Euler Problem 488: Unbalanced Nim.

Find the last 9 digits of F(10^18), where F(N) is the sum of a + b + c for all losing positions
(0 < a < b < c < N) in 3-heap Unbalanced Nim (no two heaps of equal size).
"""

from typing import Tuple

MOD = 10**9


def _dp_count_sum(a_lim: int, b_lim: int, c_lim: int) -> Tuple[int, int]:
    if a_lim < 0 or b_lim < 0 or c_lim < 0:
        return 0, 0

    maxbits = max(a_lim, b_lim, c_lim).bit_length()
    if maxbits == 0:
        maxbits = 1

    counts = [0] * 8
    sum_a = [0] * 8
    sum_b = [0] * 8
    sum_c = [0] * 8
    counts[7] = 1

    for p in range(maxbits - 1, -1, -1):
        bita = (a_lim >> p) & 1
        bitb = (b_lim >> p) & 1
        bitc = (c_lim >> p) & 1
        val = 1 << p

        ncounts = [0] * 8
        nsum_a = [0] * 8
        nsum_b = [0] * 8
        nsum_c = [0] * 8

        for state in range(8):
            cnt = counts[state]
            if cnt == 0:
                continue
            sa = sum_a[state]
            sb = sum_b[state]
            sc = sum_c[state]

            ta = (state >> 2) & 1
            tb = (state >> 1) & 1
            tc = state & 1

            for abit in (0, 1):
                if ta and abit > bita:
                    continue
                nta = 1 if (ta and abit == bita) else 0

                for bbit in (0, 1):
                    if tb and bbit > bitb:
                        continue
                    ntb = 1 if (tb and bbit == bitb) else 0

                    cbit = abit ^ bbit
                    if tc and cbit > bitc:
                        continue
                    ntc = 1 if (tc and cbit == bitc) else 0

                    nstate = (nta << 2) | (ntb << 1) | ntc

                    ncounts[nstate] += cnt
                    nsum_a[nstate] += sa + cnt * abit * val
                    nsum_b[nstate] += sb + cnt * bbit * val
                    nsum_c[nstate] += sc + cnt * cbit * val

        counts, sum_a, sum_b, sum_c = ncounts, nsum_a, nsum_b, nsum_c

    total_count = sum(counts)
    total_sum = sum(sum_a) + sum(sum_b) + sum(sum_c)
    return total_count, total_sum


def solve(limit_n: int = 10**18, mod: int = MOD) -> int:
    """Compute F(N) mod mod using shifted XOR game state reduction and 3-variable digit DP."""
    ordered_count = 0
    ordered_sum_xyz = 0

    for mask in range(8):
        a_lim = 1 if (mask & 1) else limit_n
        b_lim = 1 if (mask & 2) else limit_n
        c_lim = 1 if (mask & 4) else limit_n
        cnt, sm = _dp_count_sum(a_lim, b_lim, c_lim)
        if (mask.bit_count() & 1) == 0:
            ordered_count += cnt
            ordered_sum_xyz += sm
        else:
            ordered_count -= cnt
            ordered_sum_xyz -= sm

    total_val = (ordered_sum_xyz - 3 * ordered_count) // 6
    return total_val % mod


if __name__ == "__main__":
    print(solve())
