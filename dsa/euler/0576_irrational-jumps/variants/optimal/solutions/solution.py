"""Project Euler Problem 576: Irrational Jumps.

Find M(100, 0.00002) rounded to 4 decimal places, where M(n, g) is the maximum
sum of hitting distances for jumps sqrt(1/p) into a gap of length g at distance d.
"""

from array import array
import bisect
import heapq
import math
from typing import List, Tuple


def _primes_up_to(n: int) -> List[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    r = int(n**0.5)
    for i in range(2, r + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start : n + 1 : step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def _build_piecewise_s(
    l: float, g: float, initial_factor: float = 1.5, max_k: int = 4_000_000
) -> Tuple[array, array]:
    domain_end = 1.0 - g
    k_limit = max(10, int(initial_factor / g))
    bl = bisect.bisect_left

    while True:
        if k_limit > max_k:
            raise RuntimeError("Exceeded max_k")

        starts: List[float] = []
        ends: List[float] = []
        labels: List[int] = []
        endpoints: List[float] = [0.0, domain_end]

        x = 0.0
        for k in range(1, k_limit + 1):
            x += l
            x -= int(x)

            s = x - g
            e = x
            if e <= 0.0 or s >= domain_end:
                continue
            if s < 0.0:
                s = 0.0
            if e > domain_end:
                e = domain_end
            if s < e:
                starts.append(s)
                ends.append(e)
                labels.append(k)
                endpoints.append(s)
                endpoints.append(e)

        endpoints.sort()
        pts: List[float] = [endpoints[0]]
        for v in endpoints[1:]:
            if v != pts[-1]:
                pts.append(v)

        num_cells = len(pts) - 1
        parent = list(range(num_cells + 1))
        values = array("I", [0]) * num_cells

        def find(i: int) -> int:
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        for s, e, k in zip(starts, ends, labels):
            i = bl(pts, s)
            j = bl(pts, e)
            idx = find(i)
            while idx < j:
                values[idx] = k
                parent[idx] = idx + 1
                idx = find(idx)

        if find(0) == num_cells:
            seg_ends = array("d")
            seg_vals = array("d")
            curr = values[0]
            for i in range(1, num_cells):
                if values[i] != curr:
                    seg_ends.append(pts[i])
                    seg_vals.append(curr * l)
                    curr = values[i]
            seg_ends.append(domain_end)
            seg_vals.append(curr * l)
            return seg_ends, seg_vals

        k_limit *= 2


def _merge_max_sum(
    seg_ends_list: List[array], seg_vals_list: List[array], domain_end: float
) -> float:
    p_count = len(seg_ends_list)
    idx = [0] * p_count
    cur_val = [seg_vals_list[i][0] for i in range(p_count)]
    total = float(sum(cur_val))

    heap: List[Tuple[float, int]] = []
    for i in range(p_count):
        heapq.heappush(heap, (seg_ends_list[i][0], i))

    cur_pos = 0.0
    best = total
    eps = 1e-15

    while heap:
        boundary = heap[0][0]

        if boundary > cur_pos + 1e-18 and total > best:
            best = total

        affected: List[int] = []
        while heap and abs(heap[0][0] - boundary) <= eps:
            affected.append(heapq.heappop(heap)[1])

        cur_pos = boundary
        if cur_pos >= domain_end - 1e-15:
            break

        for i in affected:
            old = cur_val[i]
            idx[i] += 1
            new = seg_vals_list[i][idx[i]]
            cur_val[i] = new
            total += new - old
            new_end = seg_ends_list[i][idx[i]]
            heapq.heappush(heap, (new_end, i))

    return best


def solve(n: int = 100, g: float = 0.00002) -> str:
    """Compute M(n, g) rounded to 4 decimal places."""
    ps = _primes_up_to(n)
    seg_ends_list: List[array] = []
    seg_vals_list: List[array] = []

    for p in ps:
        l = 1.0 / math.sqrt(p)
        ends, vals = _build_piecewise_s(l, g)
        seg_ends_list.append(ends)
        seg_vals_list.append(vals)

    ans = _merge_max_sum(seg_ends_list, seg_vals_list, 1.0 - g)
    return f"{ans:.4f}"


if __name__ == "__main__":
    print(solve())
