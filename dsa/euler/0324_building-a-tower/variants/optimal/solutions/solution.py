"""Project Euler 324: Building a Tower

Find f(10^10000) mod 100000007, where f(n) represents the number of ways
to fill a 3x3xn tower with 2x1x1 domino blocks.
"""

from __future__ import annotations

# Available 2x1 and 1x2 horizontal dominos in a 3x3 cross section (cells 0..8)
HORIZ_DOMINOS: list[tuple[int, int]] = [
    (0, 1),
    (1, 2),
    (3, 4),
    (4, 5),
    (6, 7),
    (7, 8),
    (0, 3),
    (3, 6),
    (1, 4),
    (4, 7),
    (2, 5),
    (5, 8),
]


def count_tilings(mask: int) -> int:
    """Counts the number of ways to tile the active cells in mask with horizontal dominos."""
    if mask.bit_count() % 2 != 0:
        return 0
    if mask == 0:
        return 1
    first_cell = (mask & -mask).bit_length() - 1
    total = 0
    for u, v in HORIZ_DOMINOS:
        if u == first_cell and (mask & (1 << v)):
            total += count_tilings(mask ^ (1 << u) ^ (1 << v))
    return total


def rot90(mask: int) -> int:
    """Rotates a 3x3 bitmask 90 degrees clockwise."""
    perm = [2, 5, 8, 1, 4, 7, 0, 3, 6]
    res = 0
    for i in range(9):
        if mask & (1 << i):
            res |= 1 << perm[i]
    return res


def flip_h(mask: int) -> int:
    """Reflects a 3x3 bitmask horizontally."""
    perm = [2, 1, 0, 5, 4, 3, 8, 7, 6]
    res = 0
    for i in range(9):
        if mask & (1 << i):
            res |= 1 << perm[i]
    return res


def get_orbit(mask: int) -> set[int]:
    """Generates the D4 symmetry orbit of a 3x3 bitmask."""
    cur = mask
    orbit = set()
    for _ in range(4):
        orbit.add(cur)
        orbit.add(flip_h(cur))
        cur = rot90(cur)
    return orbit


def berlekamp_massey(s: list[int], mod: int) -> list[int]:
    """Finds the shortest linear recurrence for the sequence s modulo mod."""
    c = [1]
    b = [1]
    ell = 0
    m = 1
    b_val = 1
    for n, s_val in enumerate(s):
        d = s_val
        for i in range(1, len(c)):
            d = (d + c[i] * s[n - i]) % mod
        if d == 0:
            m += 1
        elif 2 * ell <= n:
            temp = list(c)
            mult = (d * pow(b_val, -1, mod)) % mod
            needed_len = max(len(c), len(b) + m)
            c += [0] * (needed_len - len(c))
            for i, b_elem in enumerate(b):
                c[i + m] = (c[i + m] - mult * b_elem) % mod
            ell = n + 1 - ell
            b = temp
            b_val = d
            m = 1
        else:
            mult = (d * pow(b_val, -1, mod)) % mod
            needed_len = max(len(c), len(b) + m)
            c += [0] * (needed_len - len(c))
            for i, b_elem in enumerate(b):
                c[i + m] = (c[i + m] - mult * b_elem) % mod
            m += 1
    return c


def solve(exp: int = 10_000, mod: int = 100_000_007) -> str:
    """Calculates f(10^exp) mod mod using D4 symmetry reduction of the 3x3 cross-section transfer matrix,

    Berlekamp-Massey minimal polynomial reduction, and polynomial binary exponentiation.
    """
    tiling_ways = [count_tilings(mask) for mask in range(512)]

    # 1. Build adjacency list of reachable transitions
    adj: list[list[tuple[int, int]]] = [[] for _ in range(512)]
    for u in range(512):
        for v in range(512):
            if (u & v) == 0:
                rem = (~u & ~v) & 511
                w = tiling_ways[rem]
                if w > 0:
                    adj[u].append((v, w))

    # BFS reachable states from empty profile (0)
    visited = {0}
    queue = [0]
    for u in queue:
        for v, _ in adj[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)

    # 2. Partition reachable states into D4 symmetry orbits
    seen: set[int] = set()
    orbits: list[list[int]] = []
    orb0 = get_orbit(0)
    orbits.append(sorted(orb0))
    seen.update(orb0)

    for u in sorted(visited):
        if u not in seen:
            orb = get_orbit(u)
            seen.update(orb)
            orbits.append(sorted(orb))

    mask_to_orbit = {mask: i for i, orb in enumerate(orbits) for mask in orb}
    dim = len(orbits)

    # 3. Build orbit transfer matrix
    m_orb = [[0] * dim for _ in range(dim)]
    for i, orb in enumerate(orbits):
        u = orb[0]
        for v, w in adj[u]:
            if v in mask_to_orbit:
                j = mask_to_orbit[v]
                m_orb[i][j] += w

    # 4. Generate initial sequence values s_k = f(k) mod mod
    seq: list[int] = []
    cur_v = [0] * dim
    cur_v[0] = 1
    for _ in range(120):
        seq.append(cur_v[0])
        next_v = [0] * dim
        for i in range(dim):
            vi = cur_v[i]
            if vi:
                for j in range(dim):
                    next_v[j] = (next_v[j] + vi * m_orb[i][j]) % mod
        cur_v = next_v

    # 5. Extract minimal polynomial via Berlekamp-Massey
    rec = berlekamp_massey(seq, mod)
    deg = len(rec) - 1
    poly_mod = [(-c) % mod for c in rec[1:]]

    def poly_mul(p1: list[int], p2: list[int]) -> list[int]:
        res = [0] * (len(p1) + len(p2) - 1)
        for i, a in enumerate(p1):
            for j, b in enumerate(p2):
                res[i + j] = (res[i + j] + a * b) % mod
        for i in range(len(res) - 1, deg - 1, -1):
            c = res[i]
            if c:
                for j in range(deg):
                    res[i - deg + (deg - 1 - j)] = (
                        res[i - deg + (deg - 1 - j)] + c * poly_mod[j]
                    ) % mod
        return res[:deg]

    def poly_pow(n_val: int) -> list[int]:
        res = [0] * deg
        res[0] = 1
        base = [0] * deg
        base[1] = 1
        while n_val > 0:
            if n_val % 2 == 1:
                res = poly_mul(res, base)
            base = poly_mul(base, base)
            n_val //= 2
        return res

    # 6. Evaluate polynomial binary exponentiation for N = 10^exp
    target_n = 10**exp
    c_poly = poly_pow(target_n)
    ans = sum(c_poly[i] * seq[i] for i in range(deg)) % mod

    return str(ans)


if __name__ == "__main__":
    print(solve())
