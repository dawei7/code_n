"""Project Euler Problem 378: Triangle Triples.

Find Tr(60000000) mod 10^18, the number of triples (i, j, k) with 1 <= i < j < k <= N
and dT(i) > dT(j) > dT(k), where dT(n) is the number of divisors of n(n+1)/2.
"""

from array import array


def solve(limit: int = 60000000, mod: int = 10**18) -> str:
    """Compute Tr(limit) mod mod via linear divisor count sieve and Fenwick tree inversion counting."""
    # 1. Sieve smallest prime factor up to limit + 1
    spf = array("I", [0] * (limit + 2))
    limit_sqrt = int((limit + 2) ** 0.5)
    for i in range(2, limit_sqrt + 1):
        if spf[i] == 0:
            for j in range(i * i, limit + 2, i):
                if spf[j] == 0:
                    spf[j] = i

    # 2. Compute divisor count d(x) using linear progression
    div_count = array("H", [1] * (limit + 2))
    cnt = bytearray([0]) * (limit + 2)
    rest = array("I", [0] * (limit + 2))

    for n in range(2, limit + 2):
        p = spf[n]
        if p == 0:
            div_count[n] = 2
            cnt[n] = 1
            rest[n] = 1
        else:
            r = n // p
            if spf[r] == p or (spf[r] == 0 and r == p):
                c = cnt[r] + 1
                cnt[n] = c
                rr = rest[r]
                rest[n] = rr
                div_count[n] = div_count[rr] * (c + 1)
            else:
                cnt[n] = 1
                rest[n] = r
                div_count[n] = div_count[r] * 2

    del spf, cnt, rest

    # 3. Compute dT(n) for triangle numbers T(n) = n(n+1)/2
    d_tri = array("H", [0] * (limit + 1))
    max_val = 0
    for n in range(1, limit + 1):
        if n & 1 == 0:
            val = div_count[n // 2] * div_count[n + 1]
        else:
            val = div_count[n] * div_count[(n + 1) // 2]
        d_tri[n] = val
        if val > max_val:
            max_val = val

    del div_count

    # 4. Binary Indexed Tree forward pass to count left strictly greater elements L[j]
    bit = [0] * (max_val + 2)
    left_greater = array("I", [0] * (limit + 1))

    for j in range(1, limit + 1):
        v = d_tri[j]
        s = 0
        idx = v
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        left_greater[j] = (j - 1) - s

        idx = v
        while idx <= max_val + 1:
            bit[idx] += 1
            idx += idx & (-idx)

    # 5. Binary Indexed Tree backward pass to count right strictly smaller elements and accumulate
    bit = [0] * (max_val + 2)
    total_triples = 0

    for j in range(limit, 0, -1):
        v = d_tri[j]
        s = 0
        idx = v - 1
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)

        total_triples = (total_triples + left_greater[j] * s) % mod

        idx = v
        while idx <= max_val + 1:
            bit[idx] += 1
            idx += idx & (-idx)

    return f"{total_triples:018d}"


if __name__ == "__main__":
    print(solve())
