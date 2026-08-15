"""Project Euler Problem 842: Irregular Star Polygons.

Mathematical reduction:
An n-star polygon is an undirected Hamiltonian cycle on n equally spaced points on a circle.
There are (n - 1)! / 2 such star polygons.

For any potential interior intersection point P of chords in a regular n-gon:
Let k be the number of chords passing through P (the concurrency of P).
A star polygon contains P if and only if it contains at least 2 of these k chords.

By graph theory and inclusion-exclusion:
The number of Hamiltonian cycles containing j fixed disjoint edges is:
  H(n, j) = (n - j - 1)! * 2^{j - 1}  (for n - j >= 2).

The number of star polygons containing at least 2 of the k concurrent chords is:
  N(n, k) = sum_{j=2}^k (-1)^{j - 2} * (j - 1) * C(k, j) * H(n, j)  (mod 10^9 + 7).

By linearity of expectation:
  T(n) = sum_{P} N(n, k(P)) (mod 10^9 + 7).

We determine all interior intersection points and their concurrencies k across all n = 3..60
using complex line intersections clustered via Disjoint Set Union (DSU).
"""

from __future__ import annotations

import ctypes
from pathlib import Path


def solve(n_min: int = 3, n_max: int = 60) -> int:
    """Compute sum_{n=n_min}^{n_max} T(n) modulo 10^9 + 7."""
    dll_path = Path(__file__).resolve().parent / "fast_isp_core.dll"
    if dll_path.is_file():
        try:
            lib = ctypes.CDLL(str(dll_path), winmode=0)
            lib.solve_842.restype = ctypes.c_int64
            lib.solve_842.argtypes = [ctypes.c_int, ctypes.c_int]
            return int(lib.solve_842(n_min, n_max))
        except Exception:
            pass

    # Pure Python fallback
    import cmath
    import math

    mod = 1000000007
    fact = [1] * 100
    pow2 = [1] * 100
    c_table = [[0] * 100 for _ in range(100)]
    for i in range(100):
        c_table[i][0] = 1
        for j in range(1, i + 1):
            c_table[i][j] = (c_table[i - 1][j - 1] + c_table[i - 1][j]) % mod
    for i in range(1, 100):
        fact[i] = (fact[i - 1] * i) % mod
        pow2[i] = (pow2[i - 1] * 2) % mod

    def h_val(n_nodes: int, j_edges: int) -> int:
        if n_nodes - j_edges - 1 < 0:
            return 0
        return (fact[n_nodes - j_edges - 1] * pow2[j_edges - 1]) % mod

    def n_nk(n_nodes: int, k_concur: int) -> int:
        res = 0
        for j in range(2, k_concur + 1):
            c = c_table[k_concur][j]
            term = ((j - 1) * c) % mod * h_val(n_nodes, j) % mod
            if (j - 2) % 2 == 1:
                res = (res - term + mod) % mod
            else:
                res = (res + term) % mod
        return res

    total_sum = 0
    for n in range(n_min, n_max + 1):
        if n < 4:
            continue
        w = [cmath.exp(2j * math.pi * k / n) for k in range(n)]
        chords = []
        for u in range(n):
            for v in range(u + 1, n):
                chords.append((u, v))

        pts: list[tuple[float, float, int]] = []
        for i in range(len(chords)):
            u1, v1 = chords[i]
            w1, w2 = w[u1], w[v1]
            prod1 = w1 * w2
            sum1 = w1 + w2
            for j in range(i + 1, len(chords)):
                u2, v2 = chords[j]
                if len({u1, v1, u2, v2}) < 4:
                    continue
                in1 = (u1 < u2 < v1)
                in2 = (u1 < v2 < v1)
                if in1 == in2:
                    continue

                w3, w4 = w[u2], w[v2]
                prod2 = w3 * w4
                sum2 = w3 + w4
                denom = prod1 - prod2
                if abs(denom) < 1e-12:
                    continue
                z = (prod1 * sum2 - prod2 * sum1) / denom
                pts.append((z.real, z.imag, len(pts)))

        num_pts = len(pts)
        parent = list(range(num_pts))
        sz = [1] * num_pts

        def find(v: int) -> int:
            path = []
            while v != parent[v]:
                path.append(v)
                v = parent[v]
            for node in path:
                parent[node] = v
            return v

        def union(a: int, b: int) -> None:
            ra = find(a)
            rb = find(b)
            if ra != rb:
                if sz[ra] < sz[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                sz[ra] += sz[rb]

        pts.sort(key=lambda item: item[0])
        eps = 1e-7
        eps_sq = eps * eps
        for i in range(num_pts):
            for j in range(i + 1, num_pts):
                if pts[j][0] - pts[i][0] > eps:
                    break
                dy = pts[j][1] - pts[i][1]
                if abs(dy) > eps:
                    continue
                if (pts[j][0] - pts[i][0]) ** 2 + dy * dy < eps_sq:
                    union(pts[i][2], pts[j][2])

        tn = 0
        for i in range(num_pts):
            if parent[i] == i:
                c_pairs = sz[i]
                k = int(round((1.0 + math.sqrt(1.0 + 8.0 * c_pairs)) / 2.0))
                tn = (tn + n_nk(n, k)) % mod
        total_sum = (total_sum + tn) % mod

    return total_sum


if __name__ == "__main__":
    print(solve())
