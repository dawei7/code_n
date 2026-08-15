"""Project Euler Problem 742: Minimum Area of a Convex Grid Polygon.

Find A(1000), the minimum area of a symmetrical convex grid polygon with 1000 vertices.
"""

import heapq
import math
from typing import List, Tuple

Pair = Tuple[int, int]


def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def _primitive_pairs(limit: int) -> List[Tuple[int, int, int, int]]:
    out = []
    for a in range(1, limit + 1):
        a2 = a * a
        for b in range(1, limit + 1):
            if _gcd(a, b) == 1:
                out.append((a, b, a2, b * b))
    return out


def _n_smallest_by_weight(
    pairs: List[Tuple[int, int, int, int]], k: int, t: float
) -> List[Pair]:
    heap = []
    for a, b, a2, b2 in pairs:
        w = a2 + t * b2
        tie1 = a + b
        item = (-w, -tie1, -a, -b, a, b)
        if len(heap) < k:
            heap.append(item)
        else:
            break

    heapq.heapify(heap)

    for a, b, a2, b2 in pairs[len(heap) :]:
        w = a2 + t * b2
        tie1 = a + b
        item = (-w, -tie1, -a, -b, a, b)
        if item > heap[0]:
            heapq.heapreplace(heap, item)

    return [(item[4], item[5]) for item in heap]


def _area_from_half_edges(half_edges: List[Tuple[int, int]]) -> int:
    px = 0
    py = 0
    area = 0
    for dx, dy in half_edges:
        area += px * dy - py * dx
        px += dx
        py += dy
    return area


def _polygon_area_from_interior(interior: List[Pair]) -> int:
    interior_sorted = sorted(interior, key=lambda p: (p[1] / p[0], p[0], p[1]))

    half = [(1, 0)]
    half.extend(interior_sorted)
    half.append((0, 1))
    half.extend([(-a, b) for (a, b) in reversed(interior_sorted)])

    return _area_from_half_edges(half)


def solve(n: int = 1000) -> int:
    """Compute A(N) by parameter scanning of optimal primitive vector ellipsoidal selection."""
    if n < 4 or n % 4 != 0:
        raise ValueError("N must be a positive multiple of 4.")

    k = (n - 4) // 4
    if k == 0:
        return 1

    limit = 40
    pairs = _primitive_pairs(limit)
    best_area = None

    for tn in range(1, 1001):
        t = tn / 1000.0

        while True:
            chosen = _n_smallest_by_weight(pairs, k, t)
            max_a = max(p[0] for p in chosen)
            max_b = max(p[1] for p in chosen)
            if max_a < limit and max_b < limit:
                break
            limit *= 2
            pairs = _primitive_pairs(limit)

        area = _polygon_area_from_interior(chosen)
        if best_area is None or area < best_area:
            best_area = area

    return best_area if best_area is not None else 0


if __name__ == "__main__":
    print(solve())
