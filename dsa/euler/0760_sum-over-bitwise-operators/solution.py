"""Project Euler Problem 760: Sum over Bitwise Operators.

Find G(10^18) modulo 1000000007, where G(N) = sum_{n=0}^N sum_{k=0}^n g(k, n-k)
and g(m, n) = (m XOR n) + (m OR n) + (m AND n) = 2 * (m OR n).
"""

from typing import Optional

_MOD = 1_000_000_007


def _count_pairs_sum_leq(n: int, fixed_bit: Optional[int] = None) -> int:
    if n < 0:
        return 0
    bits = max(1, n.bit_length())

    dp = [[0, 0], [0, 0]]
    dp[0][0] = 1

    for pos in range(bits - 1, -1, -1):
        nbit = (n >> pos) & 1
        ndp = [[0, 0], [0, 0]]

        for carry_next in (0, 1):
            for less in (0, 1):
                ways = dp[carry_next][less]
                if ways == 0:
                    continue

                for carry_cur in (0, 1):
                    for a_bit in (0, 1):
                        for b_bit in (0, 1):
                            if (
                                fixed_bit is not None
                                and pos == fixed_bit
                                and (a_bit | b_bit)
                            ):
                                continue

                            total = a_bit + b_bit + carry_cur
                            if (total >> 1) != carry_next:
                                continue

                            s_bit = total & 1
                            if less == 0 and s_bit > nbit:
                                continue

                            new_less = less or (s_bit < nbit)
                            ndp[carry_cur][new_less] = (
                                ndp[carry_cur][new_less] + ways
                            ) % _MOD

        dp = ndp

    return (dp[0][0] + dp[0][1]) % _MOD


def solve(n: int = 1_000_000_000_000_000_000) -> int:
    """Compute G(N) modulo 1000000007 using bitwise OR carry digit DP."""
    inv2 = (_MOD + 1) // 2
    total_pairs = (((n + 1) % _MOD) * ((n + 2) % _MOD) % _MOD) * inv2 % _MOD

    bits = max(1, n.bit_length())
    pow2 = 1
    sum_or = 0

    for i in range(bits):
        both_zero = _count_pairs_sum_leq(n, fixed_bit=i)
        bit_is_one = (total_pairs - both_zero) % _MOD
        sum_or = (sum_or + pow2 * bit_is_one) % _MOD
        pow2 = (pow2 * 2) % _MOD

    return (2 * sum_or) % _MOD


if __name__ == "__main__":
    print(solve())
