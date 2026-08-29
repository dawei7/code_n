"""Project Euler 294: Sum of digits - experience #23

Find S(11^12) mod 10^9, where S(n) is the number of positive integers k < 10^n
divisible by 23 with digit sum d(k) = 23.
"""

from __future__ import annotations


def solve(n: int = 11**12, mod: int = 10**9) -> str:
    """Calculates S(n) mod 10^9 using 2D Generating Function Doubling (Binary Exponentiation).

    Let the state of an integer block be (s, r) where:
      - s in [0, 23] is the sum of decimal digits.
      - r in [0, 22] is the remainder modulo 23.

    When concatenating block A (length L_A, multiplier M_A = 10^{L_A} mod 23) and block B (length L_B):
      (s1 + s2, (r1 + r2 * M_A) mod 23) receives A[s1, r1] * B[s2, r2] configurations.

    Using binary exponentiation on this associative combination operation, S(n) is computed in O(log n).
    """

    def make_base() -> list[list[int]]:
        table = [[0] * 23 for _ in range(24)]
        for d in range(10):
            table[d][d % 23] = 1
        return table

    def combine(a_table: list[list[int]], b_table: list[list[int]], m_a: int) -> list[list[int]]:
        c_table = [[0] * 23 for _ in range(24)]
        for s1 in range(24):
            for s2 in range(24 - s1):
                s = s1 + s2
                row_a = a_table[s1]
                row_b = b_table[s2]
                row_c = c_table[s]
                for r1 in range(23):
                    val_a = row_a[r1]
                    if val_a == 0:
                        continue
                    for r2 in range(23):
                        val_b = row_b[r2]
                        if val_b > 0:
                            r = (r1 + r2 * m_a) % 23
                            row_c[r] = (row_c[r] + val_a * val_b) % mod
        return c_table

    cur_block = make_base()
    cur_mult = 10 % 23

    res_block: list[list[int]] | None = None
    res_mult = 1

    temp_n = n
    while temp_n > 0:
        if temp_n & 1:
            if res_block is None:
                res_block = cur_block
                res_mult = cur_mult
            else:
                res_block = combine(res_block, cur_block, res_mult)
                res_mult = (res_mult * cur_mult) % 23
        temp_n >>= 1
        if temp_n > 0:
            cur_block = combine(cur_block, cur_block, cur_mult)
            cur_mult = (cur_mult * cur_mult) % 23

    ans = (res_block[23][0] if res_block else 0) % mod
    return str(ans)


if __name__ == "__main__":
    print(solve())
