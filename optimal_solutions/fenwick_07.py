"""Optimal solution for fenwick_07: K-th Smallest (Order-Statistic BIT).

Given a frequency array freq[1..n] (how many times
"""


def solve(freq, n, k):
    """K-th smallest via order-statistic BIT (binary lifting)."""
    total = sum(freq)
    if k < 1 or k > total:
        return -1
    if n == 0:
        return -1
    # Build BIT.
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = freq[i - 1]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]
    # Binary lifting: find largest idx with BIT.prefix(idx) < k.
    # The k-th smallest value is then idx + 1 (since the BIT
    # is 1-indexed and BIT[i] represents the count of value i).
    # The descent uses STRICT less-than: we take a step only
    # if bit[pos + bitmask] < (k - bit.prefix(pos)), so that
    # bit.prefix(pos) stays strictly less than k. The k-th
    # value is the smallest idx with prefix >= k, which is
    # (largest pos with prefix < k) + 1.
    idx = 0
    bitmask = 1
    while bitmask << 1 <= n:
        bitmask <<= 1
    remaining = k
    while bitmask > 0:
        nxt = idx + bitmask
        if nxt <= n and bit[nxt] < remaining:
            remaining -= bit[nxt]
            idx = nxt
        bitmask >>= 1
    return idx + 1
