"""Project Euler Problem 400: Fibonacci Tree Game.

Find the last 18 digits of f(10000), the number of winning first-turn moves on a Fibonacci tree T(10000).
"""

from typing import List


def solve(n_val: int = 10000) -> str:
    """Compute f(n_val) mod 10^18 using Sprague-Grundy value dynamic programming."""
    mod = 10**18

    # h[k] = Grundy value of T(k) with removable root
    h = [0] * (n_val + 1)
    h[1] = 1
    h[2] = 2
    for k in range(3, n_val + 1):
        h[k] = (h[k - 1] ^ h[k - 2]) + 1

    limit = 1 << (max(h).bit_length())

    # DP tables: M(k, v) = number of moves yielding Grundy value v
    prev2 = [0] * limit
    prev1 = [0] * limit
    prev1[0] = 1

    result = 0
    for k in range(2, n_val + 1):
        result = (prev1[h[k - 2]] + prev2[h[k - 1]]) % mod

        cur = [0] * limit
        cur[0] = 1
        h1 = h[k - 2]
        h2 = h[k - 1]
        for v in range(1, limit):
            cur[v] = (prev1[(v - 1) ^ h1] + prev2[(v - 1) ^ h2]) % mod

        prev2, prev1 = prev1, cur

    return f"{result:018d}"


if __name__ == "__main__":
    print(solve())
