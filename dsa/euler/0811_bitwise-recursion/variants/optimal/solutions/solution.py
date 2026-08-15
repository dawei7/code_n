"""Project Euler Problem 811: Bitwise Recursion.

Find H(10^14 + 31, 62) modulo 1_000_062_031.
"""


def b(n: int) -> int:
    """Largest power of 2 dividing n (n > 0)."""
    return n & -n


def max_binom_bitlen(r: int) -> int:
    """Max bit-length among binomial coefficients C(r, k) for k=0..r."""
    c = 1
    mx = 1
    for k in range(r + 1):
        if c.bit_length() > mx:
            mx = c.bit_length()
        if k < r:
            c = c * (r - k) // (k + 1)
    return mx


def one_positions_via_binom(t: int, r: int) -> list[int]:
    """Positions of 1-bits in (2^t + 1)^r assuming disjoint shifted blocks."""
    pos: list[int] = []
    c = 1
    for k in range(r + 1):
        x = c
        while x:
            lsb = x & -x
            bit = lsb.bit_length() - 1
            pos.append(k * t + bit)
            x -= lsb
        if k < r:
            c = c * (r - k) // (k + 1)
    return pos


def add_shift_positions(P: list[int], t: int) -> list[int]:
    """Sparse addition: return 1-bit positions of X + (X << t)."""
    n = len(P)
    i = j = 0
    last = -1
    carry = False
    out: list[int] = []

    while i < n or j < n or carry:
        candidates = []
        if i < n:
            candidates.append(P[i])
        if j < n:
            candidates.append(P[j] + t)
        if carry:
            candidates.append(last + 1)

        p = min(candidates)
        s = 0
        if i < n and P[i] == p:
            s += 1
            i += 1
        if j < n and P[j] + t == p:
            s += 1
            j += 1
        if carry and p == last + 1:
            s += 1
            carry = False

        if s & 1:
            out.append(p)
        carry = s >= 2
        last = p

    return out


def one_positions_power(t: int, r: int) -> list[int]:
    """Positions of 1-bits in (2^t + 1)^r."""
    if r == 0:
        return [0]
    if t >= max_binom_bitlen(r):
        return one_positions_via_binom(t, r)
    P = [0]
    for _ in range(r):
        P = add_shift_positions(P, t)
    return P


def A_from_positions(pos: list[int], mod: int | None) -> int:
    """Compute A(n) given sorted increasing 1-bit positions of n."""
    if not pos:
        raise ValueError("empty bit list")
    m = len(pos)
    if m == 1:
        return 1 if mod is None else 1 % mod

    v = [0] * m
    v[0] = 1 if mod is None else 1 % mod
    for k in range(1, m):
        val = 5 * v[k - 1] + 3
        v[k] = val if mod is None else val % mod

    ans = 1 if mod is None else 1 % mod
    desc = pos[::-1]

    for i in range(m - 1):
        gap = desc[i] - desc[i + 1] - 1
        if gap <= 0:
            continue
        base = v[i + 1]
        if mod is None:
            ans *= pow(base, gap)
        else:
            ans = (ans * pow(base, gap, mod)) % mod

    return ans


def A_slow(n: int) -> int:
    """Direct recurrence memoization for validation."""
    memo: dict[int, int] = {0: 1}

    def rec(x: int) -> int:
        if x in memo:
            return memo[x]
        if x & 1:
            res = rec(x >> 1)
        else:
            m_val = x >> 1
            res = 3 * rec(m_val) + 5 * rec(x - b(m_val))
        memo[x] = res
        return res

    return rec(n)


def solve(t: int = 10**14 + 31, r: int = 62, mod: int = 1_000_062_031) -> int:
    """Compute H(t, r) = A((2^t + 1)^r) modulo mod."""
    ans = 0
    for _iter in range(1):
        pos = one_positions_power(t, r)
        if any(pos[i] >= pos[i + 1] for i in range(len(pos) - 1)):
            pos = sorted(set(pos))
        ans = A_from_positions(pos, mod)
    return ans


if __name__ == "__main__":
    print(solve())
