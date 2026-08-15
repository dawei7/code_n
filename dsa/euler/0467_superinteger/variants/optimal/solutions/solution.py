"""Project Euler Problem 467: Superinteger.

Find f(10000) mod 1_000_000_007, where f(n) is the smallest positive integer
that is a common supersequence (superinteger) of P_n and C_n.
"""

from array import array
from math import isqrt
from typing import List, Tuple

MOD = 1_000_000_007


def _generate_sequences(n: int) -> Tuple[List[int], List[int]]:
    limit = 130000
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0] = is_prime[1] = 0
    r = isqrt(limit)
    for i in range(2, r + 1):
        if is_prime[i]:
            is_prime[i * i : limit + 1 : i] = b"\x00" * len(
                is_prime[i * i : limit + 1 : i]
            )

    primes: List[int] = []
    comps: List[int] = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            if len(primes) < n:
                primes.append(i)
        else:
            if len(comps) < n:
                comps.append(i)

    p_digits = [1 + ((p - 1) % 9) for p in primes[:n]]
    c_digits = [1 + ((c - 1) % 9) for c in comps[:n]]
    return p_digits, c_digits


def solve(n: int = 10000, mod: int = MOD) -> int:
    """Compute f(n) mod mod using 2D Shortest Common Supersequence DP and lexicographic reconstruction."""
    p_seq, c_seq = _generate_sequences(n)
    stride = n + 1
    dp = array("H", [0] * (stride * stride))

    for i in range(stride):
        dp[i * stride + n] = n - i
        dp[n * stride + i] = n - i

    for i in range(n - 1, -1, -1):
        row_cur = i * stride
        row_next = (i + 1) * stride
        pi = p_seq[i]
        for j in range(n - 1, -1, -1):
            if pi == c_seq[j]:
                dp[row_cur + j] = 1 + dp[row_next + j + 1]
            else:
                a = dp[row_next + j]
                b = dp[row_cur + j + 1]
                dp[row_cur + j] = 1 + (a if a < b else b)

    ans = 0
    i = 0
    j = 0
    while i < n or j < n:
        if i == n:
            d = c_seq[j]
            j += 1
        elif j == n:
            d = p_seq[i]
            i += 1
        elif p_seq[i] == c_seq[j]:
            d = p_seq[i]
            i += 1
            j += 1
        else:
            c1 = dp[(i + 1) * stride + j]
            c2 = dp[i * stride + j + 1]
            if c1 < c2:
                d = p_seq[i]
                i += 1
            elif c2 < c1:
                d = c_seq[j]
                j += 1
            else:
                if p_seq[i] <= c_seq[j]:
                    d = p_seq[i]
                    i += 1
                else:
                    d = c_seq[j]
                    j += 1
        ans = (ans * 10 + d) % mod

    return ans


if __name__ == "__main__":
    print(solve())
