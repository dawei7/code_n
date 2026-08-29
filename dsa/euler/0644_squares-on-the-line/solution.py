"""Project Euler Problem 644: Squares on the Line.

Find f(200, 500) rounded to 8 digits after the decimal point, where f(a, b) is the maximum
of the expected gain e(L) for L in [a, b] in the impartial square covering game.
"""

from bisect import bisect_right
import math
from typing import List, Tuple

_SQRT2 = math.sqrt(2.0)
_EPS = 1e-12


def _generate_ring(max_l: float) -> List[float]:
    vals = [0.0]
    max_b = int(max_l / _SQRT2) + 1
    for b in range(max_b + 1):
        base = b * _SQRT2
        max_a = int(max_l - base + 1e-12)
        for a in range(max_a + 1):
            vals.append(a + base)
    return sorted(set(vals))


def _compute_grundy_intervals(
    max_l: float,
) -> Tuple[List[float], List[float], List[int]]:
    vals = _generate_ring(max_l)
    n = len(vals) - 1
    starts: List[float] = []
    ends: List[float] = []
    grundy: List[int] = []
    moves = [False] * 256
    max_g = 0

    for idx in range(n):
        a = vals[idx]
        b = vals[idx + 1]
        mid_l = (a + b) * 0.5
        for i in range(max_g + 1):
            moves[i] = False

        for x in (1.0, _SQRT2):
            if mid_l < x or not starts:
                continue
            s_val = mid_l - x
            u_idx = bisect_right(starts, s_val) - 1
            t_idx = 0
            while t_idx <= u_idx:
                t_start = starts[t_idx]
                if t_start >= s_val:
                    break
                t_end = min(ends[t_idx], s_val)
                u_start = starts[u_idx]
                u_end = min(ends[u_idx], s_val)

                left = max(t_start, s_val - u_end)
                right = min(t_end, s_val - u_start)
                if left < right:
                    g = grundy[t_idx] ^ grundy[u_idx]
                    if g >= len(moves):
                        moves.extend([False] * len(moves))
                    moves[g] = True
                    if g > max_g:
                        max_g = g
                if t_end < s_val - u_start:
                    t_idx += 1
                else:
                    u_idx -= 1

        g = 0
        while g < len(moves) and moves[g]:
            g += 1
        if g >= len(moves):
            moves.extend([False] * len(moves))

        if grundy and grundy[-1] == g and abs(ends[-1] - a) < _EPS:
            ends[-1] = b
        else:
            starts.append(a)
            ends.append(b)
            grundy.append(g)

    return starts, ends, grundy


def _build_w_segments(
    starts: List[float],
    ends: List[float],
    grundy: List[int],
    max_s: float,
) -> Tuple[List[float], List[float], List[float], List[float]]:
    max_g = max(grundy) if grundy else 0
    groups: List[List[Tuple[float, float]]] = [[] for _ in range(max_g + 1)]
    for a, b, g in zip(starts, ends, grundy):
        groups[g].append((a, b))

    events: List[Tuple[float, int]] = []
    for intervals in groups:
        m = len(intervals)
        for i in range(m):
            a1, b1 = intervals[i]
            for j in range(i, m):
                a2, b2 = intervals[j]
                w = 1 if i == j else 2
                p0 = a1 + a2
                p1 = a1 + b2
                p2 = b1 + a2
                p3 = b1 + b2
                if p0 > max_s + _EPS:
                    break
                if p3 < 0.0:
                    continue
                p0 = max(p0, 0.0)
                p3 = min(p3, max_s)
                q1 = min(p1, p2)
                q2 = max(p1, p2)
                events.append((p0, w))
                events.append((q1, -w))
                events.append((q2, -w))
                events.append((p3, w))

    events.sort()
    merged: List[Tuple[float, int]] = []
    if events:
        cur_pos, cur_delta = events[0]
        for pos, delta in events[1:]:
            if abs(pos - cur_pos) < _EPS:
                cur_delta += delta
            else:
                merged.append((cur_pos, cur_delta))
                cur_pos, cur_delta = pos, delta
        merged.append((cur_pos, cur_delta))

    seg_starts: List[float] = []
    seg_ends: List[float] = []
    seg_slopes: List[float] = []
    seg_vals: List[float] = []
    slope = 0.0
    val = 0.0
    prev = 0.0
    for pos, delta in merged:
        if pos > max_s:
            break
        if pos > prev:
            seg_starts.append(prev)
            seg_ends.append(pos)
            seg_slopes.append(slope)
            seg_vals.append(val)
            val += slope * (pos - prev)
            prev = pos
        slope += delta
    if prev < max_s:
        seg_starts.append(prev)
        seg_ends.append(max_s)
        seg_slopes.append(slope)
        seg_vals.append(val)
    return seg_starts, seg_ends, seg_slopes, seg_vals


def _w_value(
    seg_starts: List[float],
    seg_ends: List[float],
    seg_slopes: List[float],
    seg_vals: List[float],
    x: float,
) -> Tuple[float, float]:
    lo = bisect_right(seg_ends, x)
    if lo >= len(seg_starts):
        return 0.0, 0.0
    start = seg_starts[lo]
    slope = seg_slopes[lo]
    val = seg_vals[lo] + slope * (x - start)
    return val, slope


def solve(a: float = 200.0, b: float = 500.0) -> str:
    """Compute f(a, b) using continuous Sprague-Grundy interval integration and derivative bisection."""
    max_l = b
    starts, ends, grundy = _compute_grundy_intervals(max_l)
    seg_data = _build_w_segments(starts, ends, grundy, max_l)
    seg_starts, seg_ends, seg_slopes, seg_vals = seg_data

    points = [a, b]
    for p in seg_starts:
        for offset in (1.0, _SQRT2):
            v = p + offset
            if a < v < b:
                points.append(v)
    for p in seg_ends:
        for offset in (1.0, _SQRT2):
            v = p + offset
            if a < v < b:
                points.append(v)
    points = sorted(set(points))

    best = -1.0

    def term_deriv(m: float, b0: float, c: float, l_val: float) -> float:
        return (m * l_val * l_val - 2.0 * m * c * l_val - b0 * c) / (
            (l_val - c) * (l_val - c)
        )

    for i in range(len(points) - 1):
        l0 = points[i]
        l1 = points[i + 1]
        if l1 - l0 < 1e-12:
            continue
        mid = (l0 + l1) * 0.5

        w1, m1 = _w_value(seg_starts, seg_ends, seg_slopes, seg_vals, mid - 1.0)
        w2, m2 = _w_value(
            seg_starts, seg_ends, seg_slopes, seg_vals, mid - _SQRT2
        )
        b1 = w1 - m1 * mid
        b2 = w2 - m2 * mid

        def e_local(l_val: float) -> float:
            return (
                0.5
                * l_val
                * (
                    (m1 * l_val + b1) / (l_val - 1.0)
                    + (m2 * l_val + b2) / (l_val - _SQRT2)
                )
            )

        def de_local(l_val: float) -> float:
            return 0.5 * (
                term_deriv(m1, b1, 1.0, l_val)
                + term_deriv(m2, b2, _SQRT2, l_val)
            )

        for l_pt in (l0, mid, l1):
            val = e_local(l_pt)
            if val > best:
                best = val

        left = l0 + 1e-10
        right = l1 - 1e-10
        if left < right:
            dl = de_local(left)
            dm = de_local(mid)
            dr = de_local(right)

            def bisect_root(
                lo: float, hi: float, dlo: float, _dhi: float
            ) -> float:
                for _ in range(60):
                    m = (lo + hi) * 0.5
                    dm_local = de_local(m)
                    if dm_local == 0.0:
                        return m
                    if dm_local * dlo > 0.0:
                        lo = m
                        dlo = dm_local
                    else:
                        hi = m
                return (lo + hi) * 0.5

            if dl * dm < 0.0:
                root = bisect_root(left, mid, dl, dm)
                val = e_local(root)
                if val > best:
                    best = val
            if dm * dr < 0.0:
                root = bisect_root(mid, right, dm, dr)
                val = e_local(root)
                if val > best:
                    best = val

    return f"{best:.8f}"


if __name__ == "__main__":
    print(solve())
