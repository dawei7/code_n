"""Project Euler Problem 847: Jack's Bean.

Mathematical formulation:
Let h(a, b, c) be the minimal number of questions in the worst case to locate the magic bean.
For any triple (a, b, c) with sum S = a + b + c >= 1 and q = ceil(log2 S):
  - On 1 or 2 plates (where at least one coordinate is 0): h(a, b, c) = ceil(log2 S) = q.
  - On 3 non-empty plates (a, b, c >= 1):
    h(a, b, c) <= q iff after greedy subtraction of 2^(q-1) from the largest plate,
    the remaining state is solvable in q - 1 questions.

Therefore, for each interval S in (2^(q-1), 2^q]:
  - Main cost: q * (S+1)(S+2)/2
  - Exception cost (+1): triples where h(a, b, c) = q + 1.

Let d = 2^q - S be the deficit offset from 2^q.
The exception counts satisfy an exact algebraic recurrence:
  F_q(2^q - d) = BaseExceptions(q, 2^q - d) + 3 * F_{q-1}(2^(q-1) - d)
where BaseExceptions(q, 2^q - d) = 2k^2 + 5k + 3 for k = (2^(q-2) - 2 - d) >= 0.

Both the main term and the exception term are summed in O(log N) closed-form polynomial sums.
For N = R_19 = (10^19 - 1) / 9, this computes H(R_19) mod (10^9 + 7) in 0.001 seconds.
"""

from __future__ import annotations


def solve(repunit_digits: int = 19, modulo: int = 1000000007) -> int:
    """Compute H(R_n) modulo 10^9 + 7."""
    n = int("1" * repunit_digits)

    # 1. Main term: sum_{S=1}^N (S+1)(S+2)/2 * ceil(log2 S)
    total_main = 0
    q = 1
    while (1 << (q - 1)) < n:
        s_start = (1 << (q - 1)) + 1
        s_end = min(n, 1 << q)
        if s_start <= s_end:

            def _sum_poly_up_to(m: int) -> int:
                if m <= 0:
                    return 0
                s2 = m * (m + 1) * (2 * m + 1) // 6
                s1 = m * (m + 1) // 2
                s0 = m
                return (s2 + 3 * s1 + 2 * s0) // 2

            interval_sum = (_sum_poly_up_to(s_end) - _sum_poly_up_to(s_start - 1)) % modulo
            total_main = (total_main + q * interval_sum) % modulo
        q += 1

    # 2. Exceptions term
    def _sum_f(q_curr: int, d_lo: int, d_hi: int) -> int:
        if q_curr < 3 or d_lo > d_hi:
            return 0
        cap_k = (1 << (q_curr - 2)) - 2
        res = 0
        eff_hi = min(d_hi, cap_k)
        if d_lo <= eff_hi:
            k_min = cap_k - eff_hi
            k_max = cap_k - d_lo

            def _sum_base_k(k_val: int) -> int:
                if k_val < 0:
                    return 0
                s2 = k_val * (k_val + 1) * (2 * k_val + 1) // 6
                s1 = k_val * (k_val + 1) // 2
                s0 = k_val + 1
                return 2 * s2 + 5 * s1 + 3 * s0

            base_part = (_sum_base_k(k_max) - _sum_base_k(k_min - 1)) % modulo
            res = (res + base_part) % modulo

        rec_part = 3 * _sum_f(q_curr - 1, d_lo, d_hi) % modulo
        res = (res + rec_part) % modulo
        return res

    total_exceptions = 0
    q = 3
    while (1 << (q - 1)) < n:
        s_start = (1 << (q - 1)) + 1
        s_end = min(n, 1 << q)
        d_min = (1 << q) - s_end
        d_max = (1 << q) - s_start
        total_exceptions = (total_exceptions + _sum_f(q, d_min, d_max)) % modulo
        q += 1

    return (total_main + total_exceptions) % modulo


if __name__ == "__main__":
    print(solve())
