"""Optimal solution for string_06: Rabin-Karp.

Rolling-hash substring search.
"""


def solve(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    BASE = 256
    MOD = (1 << 61) - 1
    p_hash = 0
    t_hash = 0
    h = 1
    for i in range(m):
        p_hash = (p_hash * BASE + ord(pattern[i])) % MOD
        t_hash = (t_hash * BASE + ord(text[i])) % MOD
        if i < m - 1:
            h = (h * BASE) % MOD
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t_hash = ((t_hash - ord(text[i]) * h) * BASE + ord(text[i + m])) % MOD
            if t_hash < 0:
                t_hash += MOD
    return -1
