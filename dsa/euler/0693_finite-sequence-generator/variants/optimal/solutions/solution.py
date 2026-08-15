"""Project Euler Problem 693: Finite Sequence Generator.

Find f(3000000), where a_{z+1} = a_z^2 mod z, l(x, y) is the sequence length until reaching 0 or 1,
g(x) = max_{y < x} l(x, y), and f(n) = max_{x <= n} g(x).
"""

import heapq
import math
from typing import Dict, List


def _initial_active_after_first_step(x: int) -> List[int]:
    if x <= 2:
        return []

    mark = bytearray(x)
    active: List[int] = []

    y = 2
    sq = (y * y) % x
    delta = 2 * y + 1
    limit = x // 2

    while y <= limit:
        if sq > 1 and not mark[sq]:
            mark[sq] = 1
            active.append(sq)

        sq += delta
        if sq >= x:
            sq -= x
            if sq >= x:
                sq -= x
        delta += 2
        y += 1

    return active


def _step_active_mark(active: List[int], mod: int) -> List[int]:
    mark = bytearray(mod)
    nxt: List[int] = []
    for a in active:
        v = (a * a) % mod
        if v > 1 and not mark[v]:
            mark[v] = 1
            nxt.append(v)
    return nxt


def _step_active_set(active: List[int], mod: int) -> List[int]:
    s = set()
    for a in active:
        v = (a * a) % mod
        if v > 1:
            s.add(v)
    return list(s)


def _g(x: int, big_threshold: int = 100_000) -> int:
    if x < 2:
        return 0
    if x == 2:
        return 1

    active = _initial_active_after_first_step(x)
    length = 2
    mod = x + 1

    while len(active) > 1:
        if len(active) >= big_threshold:
            active = _step_active_mark(active, mod)
        else:
            active = _step_active_set(active, mod)

        length += 1
        mod += 1

        if not active:
            return length

    if not active:
        return length

    v = active[0]
    while v > 1:
        v = (v * v) % mod
        length += 1
        mod += 1

    return length


def solve(n: int = 3_000_000, target_points: int = 16) -> int:
    """Compute f(n) = max_{2 <= x <= n} g(x) via best-first branch-and-bound search."""
    if n < 2:
        return 0

    cache: Dict[int, int] = {}

    def get_g(x: int) -> int:
        val = cache.get(x)
        if val is None:
            val = _g(x)
            cache[x] = val
        return val

    grid = max(1, (n - 2) // (target_points - 1))
    if grid > 1:
        p = 10 ** int(math.log10(grid))
        for m in (1, 2, 5, 10):
            if m * p >= grid:
                grid = m * p
                break

    points = list(range(2, n + 1, grid))
    if points[-1] != n:
        points.append(n)

    best = 0
    g_at_right: Dict[int, int] = {}
    for x in points:
        gx = get_g(x)
        g_at_right[x] = gx
        if gx > best:
            best = gx

    heap = []
    for i in range(1, len(points)):
        l = points[i - 1]
        r = points[i]
        gr = g_at_right[r]
        ub = gr + (r - l)
        heapq.heappush(heap, (-ub, l, r, gr))

    while heap:
        ub = -heap[0][0]
        if ub <= best:
            break

        _, l, r, gr = heapq.heappop(heap)
        if r - l <= 1:
            continue

        m = (l + r) // 2
        gm = get_g(m)
        if gm > best:
            best = gm

        if m - l > 1:
            ub_left = gm + (m - l)
            if ub_left > best:
                heapq.heappush(heap, (-ub_left, l, m, gm))

        if r - m > 1:
            ub_right = gr + (r - m)
            if ub_right > best:
                heapq.heappush(heap, (-ub_right, m, r, gr))

    return best


if __name__ == "__main__":
    print(solve())
