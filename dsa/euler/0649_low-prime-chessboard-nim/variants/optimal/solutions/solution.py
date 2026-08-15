"""Project Euler Problem 649: Low-Prime Chessboard Nim.

Find the last 9 digits of M(10000019, 100), where M(n, c) is the number of winning starting
arrangements for Alice in an n x n board with c distinct coins under 2, 3, 5, 7 moves.
"""

from typing import List

_MOD = 1_000_000_000


def _fwht_int(arr: List[int]) -> List[int]:
    res = arr[:]
    h = 1
    while h < 8:
        for i in range(0, 8, 2 * h):
            for j in range(i, i + h):
                x = res[j]
                y = res[j + h]
                res[j] = x + y
                res[j + h] = x - y
        h *= 2
    return res


def solve(n: int = 10_000_019, c: int = 100) -> int:
    """Compute M(n, c) mod 10^9 using 1D Grundy period-9 symmetry and 8-point Fast Walsh-Hadamard Transform."""
    pattern = [0, 0, 1, 1, 2, 2, 3, 3, 4]
    cnt = [0] * 8
    full_periods = n // 9
    rem = n % 9
    for v in pattern:
        cnt[v] += full_periods
    for i in range(rem):
        cnt[pattern[i]] += 1

    c_2d = [0] * 8
    for g1 in range(8):
        for g2 in range(8):
            c_2d[g1 ^ g2] += cnt[g1] * cnt[g2]

    c_hat = _fwht_int(c_2d)

    p0_sum = sum(pow(val, c, 8 * _MOD) for val in c_hat)
    p0 = (p0_sum // 8) % _MOD

    total_positions = pow(n * n, c, _MOD)
    ans = (total_positions - p0) % _MOD
    return ans


if __name__ == "__main__":
    print(solve())
