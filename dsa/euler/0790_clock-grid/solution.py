"""Project Euler Problem 790: Clock Grid.

Find C(10^5), the sum of all clock hours across a 50515093 x 50515093 grid
after 10^5 rectangular hour-increment updates modulo 12.
"""

from array import array
import sys

_M = 50515093
_S0 = 290797


def _compute_C(t: int) -> int:
    if t == 0:
        return 12 * _M * _M

    s = _S0
    x_set = {0, _M}
    y_set = {0, _M}
    events = []

    for _ in range(t):
        x1 = s
        s = (s * s) % _M
        x2 = s
        s = (s * s) % _M
        y1 = s
        s = (s * s) % _M
        y2 = s
        s = (s * s) % _M

        if x1 <= x2:
            xl, xh = x1, x2
        else:
            xl, xh = x2, x1

        if y1 <= y2:
            yl, yh = y1, y2
        else:
            yl, yh = y2, y1

        xh1 = xh + 1
        yh1 = yh + 1

        x_set.add(xl)
        x_set.add(xh1)
        y_set.add(yl)
        y_set.add(yh1)

        events.append((xl, 1, yl, yh1))
        events.append((xh1, 11, yl, yh1))

    x_vals = sorted(x_set)
    y_vals = sorted(y_set)
    del x_set, y_set

    y_index = {v: i for i, v in enumerate(y_vals)}
    events_idx = [(x, sh, y_index[yl], y_index[yh1]) for (x, sh, yl, yh1) in events]
    del events, y_index
    events_idx.sort(key=lambda e: e[0])

    m = len(y_vals) - 1
    size = 4 * m + 5

    seg = array("Q", [0]) * (12 * size)
    lazy = bytearray(size)

    sys.setrecursionlimit(1_000_000)

    def build(node: int, l: int, r: int) -> None:
        base = node * 12
        if r - l == 1:
            seg[base] = y_vals[l + 1] - y_vals[l]
            return
        mid = (l + r) >> 1
        left = node << 1
        build(left, l, mid)
        build(left + 1, mid, r)
        seg[base] = seg[left * 12] + seg[(left + 1) * 12]

    build(1, 0, m)

    buf = [0] * 12
    a = seg
    lz = lazy

    def _apply(node: int, shift: int) -> None:
        if shift == 0:
            return
        shift %= 12
        base = node * 12

        if shift == 1:
            tmp = a[base + 11]
            a[base + 11] = a[base + 10]
            a[base + 10] = a[base + 9]
            a[base + 9] = a[base + 8]
            a[base + 8] = a[base + 7]
            a[base + 7] = a[base + 6]
            a[base + 6] = a[base + 5]
            a[base + 5] = a[base + 4]
            a[base + 4] = a[base + 3]
            a[base + 3] = a[base + 2]
            a[base + 2] = a[base + 1]
            a[base + 1] = a[base]
            a[base] = tmp
        elif shift == 11:
            tmp = a[base]
            a[base] = a[base + 1]
            a[base + 1] = a[base + 2]
            a[base + 2] = a[base + 3]
            a[base + 3] = a[base + 4]
            a[base + 4] = a[base + 5]
            a[base + 5] = a[base + 6]
            a[base + 6] = a[base + 7]
            a[base + 7] = a[base + 8]
            a[base + 8] = a[base + 9]
            a[base + 9] = a[base + 10]
            a[base + 10] = a[base + 11]
            a[base + 11] = tmp
        else:
            for i in range(12):
                buf[i] = a[base + ((i - shift) % 12)]
            for i in range(12):
                a[base + i] = buf[i]

        lz[node] = (lz[node] + shift) % 12

    def _push(node: int) -> None:
        s = lz[node]
        if s:
            left = node << 1
            _apply(left, s)
            _apply(left + 1, s)
            lz[node] = 0

    def _pull(node: int) -> None:
        base = node * 12
        left_base = (node << 1) * 12
        right_base = ((node << 1) + 1) * 12
        for i in range(12):
            a[base + i] = a[left_base + i] + a[right_base + i]

    def update(node: int, l: int, r: int, ql: int, qr: int, shift: int) -> None:
        if ql <= l and r <= qr:
            _apply(node, shift)
            return
        _push(node)
        mid = (l + r) >> 1
        left = node << 1
        if ql < mid:
            update(left, l, mid, ql, qr, shift)
        if qr > mid:
            update(left + 1, mid, r, ql, qr, shift)
        _pull(node)

    hist = [0] * 12
    prev_x = 0
    num_events = len(events_idx)
    idx = 0

    while idx < num_events:
        cur_x = events_idx[idx][0]
        if cur_x > prev_x:
            dx = cur_x - prev_x
            root_base = 12
            for r in range(12):
                hist[r] += dx * a[root_base + r]
            prev_x = cur_x

        while idx < num_events and events_idx[idx][0] == cur_x:
            _, sh, ql, qr = events_idx[idx]
            update(1, 0, m, ql, qr, sh)
            idx += 1

    if prev_x < _M:
        dx = _M - prev_x
        root_base = 12
        for r in range(12):
            hist[r] += dx * a[root_base + r]

    ans = 12 * hist[0]
    for r in range(1, 12):
        ans += r * hist[r]

    return ans


def solve(t: int = 100_000) -> int:
    """Compute C(t) using sweep-line segment tree with residue bucket rotation mod 12."""
    ans = 0
    for _iter in range(1):
        ans = _compute_C(t)
    return ans


if __name__ == "__main__":
    print(solve())
