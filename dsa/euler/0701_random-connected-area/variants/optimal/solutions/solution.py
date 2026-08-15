"""Project Euler Problem 701: Random Connected Area.

Find E(7, 7), the expected value of the maximum area of a connected black component
in a 7x7 grid with independent p=0.5 cell coloring, rounded to 8 decimal places.
"""

from decimal import Decimal, ROUND_HALF_UP, getcontext
from typing import Dict, List, Tuple


def solve(w: int = 7, h: int = 7, places: int = 8) -> str:
    """Compute E(W, H) using sweep-line frontier connectivity dynamic programming."""
    n = w * h
    start_labels = (0,) * w
    start_sizes: Tuple[int, ...] = ()
    start_conn = (start_labels, start_sizes)

    dp: Dict[Tuple[Tuple[int, ...], Tuple[int, ...]], Dict[int, int]] = {
        start_conn: {0: 1}
    }
    trans_cache: Dict[
        Tuple[Tuple[int, ...], Tuple[int, ...], int, int],
        Tuple[Tuple[int, ...], Tuple[int, ...], int],
    ] = {}

    for idx in range(n):
        c = idx % w
        new_dp: Dict[Tuple[Tuple[int, ...], Tuple[int, ...]], Dict[int, int]] = {}

        for (labels, sizes), mxmap in dp.items():
            left_id = labels[c - 1] if c else 0
            up_id = labels[c]

            for color in (0, 1):
                key = (labels, sizes, c, color)
                tr = trans_cache.get(key)

                if tr is None:
                    nl = list(labels)
                    ns = list(sizes)

                    if color == 0:
                        nl[c] = 0
                    else:
                        if left_id == 0 and up_id == 0:
                            ns.append(1)
                            nl[c] = len(ns)
                        elif up_id == 0:
                            ns[left_id - 1] += 1
                            nl[c] = left_id
                        elif left_id == 0:
                            ns[up_id - 1] += 1
                            nl[c] = up_id
                        else:
                            if left_id == up_id:
                                ns[left_id - 1] += 1
                                nl[c] = left_id
                            else:
                                a = left_id
                                b = up_id
                                ns[a - 1] = ns[a - 1] + ns[b - 1] + 1
                                ns[b - 1] = 0
                                for j in range(w):
                                    if nl[j] == b:
                                        nl[j] = a
                                nl[c] = a

                    k2 = len(ns)
                    present = [False] * (k2 + 1)
                    for lab in nl:
                        if lab:
                            present[lab] = True

                    closed_max = 0
                    for comp_id in range(1, k2 + 1):
                        sz = ns[comp_id - 1]
                        if sz and not present[comp_id]:
                            if sz > closed_max:
                                closed_max = sz
                            ns[comp_id - 1] = 0

                    mapping = [0] * (k2 + 1)
                    canon_sizes: List[int] = []
                    canon_labels = [0] * w
                    next_id = 0
                    for j, lab in enumerate(nl):
                        if lab == 0:
                            continue
                        nid = mapping[lab]
                        if nid == 0:
                            next_id += 1
                            mapping[lab] = next_id
                            canon_sizes.append(ns[lab - 1])
                            nid = next_id
                        canon_labels[j] = nid

                    labels2 = tuple(canon_labels)
                    sizes2 = tuple(canon_sizes)
                    tr = (labels2, sizes2, closed_max)
                    trans_cache[key] = tr

                labels2, sizes2, closed_max = tr
                conn2 = (labels2, sizes2)

                tgt = new_dp.get(conn2)
                if tgt is None:
                    tgt = {}
                    new_dp[conn2] = tgt

                if closed_max == 0:
                    for mx, cnt in mxmap.items():
                        tgt[mx] = tgt.get(mx, 0) + cnt
                else:
                    for mx, cnt in mxmap.items():
                        mx2 = mx if mx >= closed_max else closed_max
                        tgt[mx2] = tgt.get(mx2, 0) + cnt

        dp = new_dp

    denom = 1 << n
    numer = 0

    for (labels, sizes), mxmap in dp.items():
        active_max = max(sizes) if sizes else 0
        if active_max == 0:
            for mx, cnt in mxmap.items():
                numer += mx * cnt
        else:
            for mx, cnt in mxmap.items():
                numer += (mx if mx >= active_max else active_max) * cnt

    getcontext().prec = 80
    value = Decimal(numer) / Decimal(denom)
    q = Decimal("1." + "0" * places)
    return str(value.quantize(q, rounding=ROUND_HALF_UP))


if __name__ == "__main__":
    print(solve())
