"""Project Euler Problem 353: Risky Moon.

Find sum_{n=1..15} M(2^n - 1) rounded to 10 decimal places.
"""

import math
import heapq

# Precompute smallest prime factors and Gaussian prime representations
MAX_VAL = 65536
spf = list(range(MAX_VAL + 1))
for i in range(2, int(math.isqrt(MAX_VAL)) + 1):
    if spf[i] == i:
        for j in range(i * i, MAX_VAL + 1, i):
            if spf[j] == j:
                spf[j] = i

gaussian_prime = {}
for p in range(2, MAX_VAL + 1):
    if spf[p] == p:
        if p == 2:
            gaussian_prime[2] = (1, 1)
        elif p % 4 == 1:
            for a in range(1, int(math.isqrt(p)) + 1):
                b2 = p - a * a
                b = math.isqrt(b2)
                if b * b == b2:
                    gaussian_prime[p] = (a, b)
                    break


def _mult(c1: tuple[int, int], c2: tuple[int, int]) -> tuple[int, int]:
    return (c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c1[1] * c2[0])


def _solve_r(r: int) -> float:
    pts = []
    valid_z = []
    r2 = r * r
    for z in range(0, r + 1):
        if z == r:
            pts.append((0, 0, r))
            pts.append((0, 0, -r))
            valid_z.append(z)
            continue
        factors = {}
        for val in (r - z, r + z):
            v = val
            while v > 1:
                p = spf[v]
                cnt = 0
                while spf[v] == p:
                    cnt += 1
                    v //= p
                factors[p] = factors.get(p, 0) + cnt

        valid = True
        scale = 1
        for p, e in factors.items():
            if p % 4 == 3:
                if e % 2 != 0:
                    valid = False
                    break
                scale *= (p ** (e // 2))
        if not valid:
            continue

        valid_z.append(z)
        cur = [(scale, 0)]
        for p, e in factors.items():
            if p == 2:
                w = (1, 1)
                p_pow = (1, 0)
                for _ in range(e):
                    p_pow = _mult(p_pow, w)
                cur = [_mult(c, p_pow) for c in cur]
            elif p % 4 == 1:
                a, b = gaussian_prime[p]
                pi = (a, b)
                pibar = (a, -b)
                pi_pows = [(1, 0)]
                for _ in range(e):
                    pi_pows.append(_mult(pi_pows[-1], pi))
                pibar_pows = [(1, 0)]
                for _ in range(e):
                    pibar_pows.append(_mult(pibar_pows[-1], pibar))

                next_cur = []
                for k in range(e + 1):
                    term = _mult(pi_pows[k], pibar_pows[e - k])
                    for c in cur:
                        next_cur.append(_mult(c, term))
                cur = next_cur

        pairs = set()
        for u, v in cur:
            u, v = abs(u), abs(v)
            pairs.add((u, v))
            pairs.add((v, u))

        for u, v in pairs:
            u_signs = (u, -u) if u > 0 else (0,)
            v_signs = (v, -v) if v > 0 else (0,)
            z_signs = (z, -z) if z > 0 else (0,)
            for sx in u_signs:
                for sy in v_signs:
                    for sz in z_signs:
                        pts.append((sx, sy, sz))

    pts = list(set(pts))
    n_pts = len(pts)
    src = pts.index((0, 0, r))
    dst = pts.index((0, 0, -r))

    if n_pts <= 10:
        max_angle = math.pi
    else:
        max_ang_gap = 0.0
        for i in range(len(valid_z) - 1):
            z1, z2 = valid_z[i], valid_z[i + 1]
            dot = (math.isqrt(r2 - z1 * z1) * math.isqrt(r2 - z2 * z2) + z1 * z2) / r2
            dot = max(-1.0, min(1.0, dot))
            ang = math.acos(dot)
            if ang > max_ang_gap:
                max_ang_gap = ang
        max_angle = min(math.pi, max(0.025, max_ang_gap * 2.2))

    cell_size = math.sin(max_angle / 2) * 2.0
    inv_cell_size_r = 1.0 / (r * cell_size)
    grid = {}
    for i, (x, y, z) in enumerate(pts):
        gx = int(x * inv_cell_size_r)
        gy = int(y * inv_cell_size_r)
        gz = int(z * inv_cell_size_r)
        key = (gx, gy, gz)
        if key not in grid:
            grid[key] = []
        grid[key].append(i)

    max_d2 = 2 * r2 * (1 - math.cos(max_angle))
    dist = [float("inf")] * n_pts
    dist[src] = 0.0
    pq = [(0.0, src)]
    pi2 = math.pi * math.pi
    inv_r2 = 1.0 / r2

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == dst:
            return d
        ux, uy, uz = pts[u]
        gx = int(ux * inv_cell_size_r)
        gy = int(uy * inv_cell_size_r)
        gz = int(uz * inv_cell_size_r)

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    neighbor_key = (gx + dx, gy + dy, gz + dz)
                    if neighbor_key in grid:
                        for v in grid[neighbor_key]:
                            if u == v:
                                continue
                            vx, vy, vz = pts[v]
                            ed2 = (ux - vx) * (ux - vx) + (uy - vy) * (uy - vy) + (uz - vz) * (uz - vz)
                            if ed2 <= max_d2:
                                dot = (ux * vx + uy * vy + uz * vz) * inv_r2
                                dot = max(-1.0, min(1.0, dot))
                                th = math.acos(dot)
                                w = (th * th) / pi2
                                if d + w < dist[v]:
                                    dist[v] = d + w
                                    heapq.heappush(pq, (dist[v], v))
    return dist[dst]


def solve(max_n: int = 15, decimals: int = 10) -> str:
    """Find sum_{n=1..max_n} M(2^n - 1) formatted to specified decimal places."""
    total = 0.0
    for n in range(1, max_n + 1):
        r = (1 << n) - 1
        total += _solve_r(r)
    return f"{total:.{decimals}f}"


if __name__ == "__main__":
    print(solve())
