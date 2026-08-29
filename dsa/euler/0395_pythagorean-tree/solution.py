"""Project Euler Problem 395: Pythagorean Tree.

Find the smallest area possible for an axis-aligned bounding rectangle enclosing the entire infinite
Pythagorean tree, rounded to 10 decimal places.
"""

import heapq
import math
from typing import List, Tuple

Vec = Tuple[float, float]
Node = Tuple[Vec, Vec, Vec, float]

K_U = 16.0 / 25.0
K_V = 12.0 / 25.0
RADIUS_UNIT_TREE = 5.0 * math.sqrt(13.0 / 10.0)


def _add(a: Vec, b: Vec) -> Vec:
    return (a[0] + b[0], a[1] + b[1])


def _sub(a: Vec, b: Vec) -> Vec:
    return (a[0] - b[0], a[1] - b[1])


def _mul(a: Vec, k: float) -> Vec:
    return (a[0] * k, a[1] * k)


def _cross(a: Vec, b: Vec) -> float:
    return a[0] * b[1] - a[1] * b[0]


def _norm(a: Vec) -> float:
    return math.hypot(a[0], a[1])


def _rotate_ccw(a: Vec) -> Vec:
    return (-a[1], a[0])


def _square_corners(p: Vec, u: Vec, v: Vec) -> List[Vec]:
    return [p, _add(p, u), _add(_add(p, u), v), _add(p, v)]


def _make_child(p_pt: Vec, q_pt: Vec, r_pt: Vec) -> Node:
    u = _sub(q_pt, p_pt)
    if _cross(u, _sub(r_pt, p_pt)) > 0.0:
        p_pt, q_pt = q_pt, p_pt
        u = (-u[0], -u[1])
    v = _rotate_ccw(u)
    s = _norm(u)
    return (p_pt, u, v, s)


def _children(node: Node) -> Tuple[Node, Node]:
    p, u, v, _ = node
    pt_a = _add(p, v)
    pt_b = _add(_add(p, u), v)
    pt_c = _add(pt_a, _add(_mul(u, K_U), _mul(v, K_V)))
    left = _make_child(pt_a, pt_c, pt_b)
    right = _make_child(pt_b, pt_c, pt_a)
    return left, right


def solve(eps: float = 1e-12) -> str:
    """Compute minimal bounding box area using branch-and-bound disk pruning."""
    root: Node = ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0), 1.0)

    corners = _square_corners(root[0], root[1], root[2])
    xmin = min(c[0] for c in corners)
    xmax = max(c[0] for c in corners)
    ymin = min(c[1] for c in corners)
    ymax = max(c[1] for c in corners)

    pq: List[Tuple[float, Node]] = []
    for ch in _children(root):
        heapq.heappush(pq, (-ch[3], ch))

    while pq:
        _, node = heapq.heappop(pq)
        p, u, v, s = node

        cx = p[0] + 0.5 * (u[0] + v[0])
        cy = p[1] + 0.5 * (u[1] + v[1])
        rad = s * RADIUS_UNIT_TREE

        # Branch-and-bound pruning check
        if (
            cx + rad <= xmax + eps
            and cx - rad >= xmin - eps
            and cy + rad <= ymax + eps
            and cy - rad >= ymin - eps
        ):
            continue

        # Update bounding box
        for x, y in _square_corners(p, u, v):
            if x < xmin:
                xmin = x
            elif x > xmax:
                xmax = x
            if y < ymin:
                ymin = y
            elif y > ymax:
                ymax = y

        for ch in _children(node):
            heapq.heappush(pq, (-ch[3], ch))

    area = (xmax - xmin) * (ymax - ymin)
    return f"{area:.10f}"


if __name__ == "__main__":
    print(solve())
