"""Project Euler Problem 584: Birthday Problem Revisited.

Find the expected number of people entering a room in a 365-day year until
4 people have birthdays within 7 days of each other, rounded to 8 decimal places.
"""

from typing import Dict, List, Tuple


def _gauss_laguerre(n: int, eps: float = 1e-14) -> Tuple[List[float], List[float]]:
    xs = [0.0] * n
    ws = [0.0] * n
    z = 0.0

    for i in range(1, n + 1):
        if i == 1:
            z = 3.0 / (1.0 + 2.4 * n)
        elif i == 2:
            z += 15.0 / (1.0 + 2.5 * n)
        else:
            ai = i - 2
            z += ((1.0 + 2.55 * ai) / (1.9 * ai)) * (z - xs[i - 3])

        for _ in range(100):
            l0 = 1.0
            l1 = 1.0 - z
            if n == 1:
                ln = l1
                lnm1 = l0
            else:
                for k in range(2, n + 1):
                    l2 = ((2 * k - 1 - z) * l1 - (k - 1) * l0) / k
                    l0, l1 = l1, l2
                ln = l1
                lnm1 = l0

            dln = n * (ln - lnm1) / z
            dz = ln / dln
            z -= dz
            if abs(dz) < eps:
                break

        xs[i - 1] = z

        l0 = 1.0
        l1 = 1.0 - z
        for k in range(2, n + 2):
            l2 = ((2 * k - 1 - z) * l1 - (k - 1) * l0) / k
            l0, l1 = l1, l2
        ln1 = l1
        ws[i - 1] = z / ((n + 1) * (n + 1) * ln1 * ln1)

    return xs, ws


def _enumerate_states(
    window_len: int, max_total: int
) -> Tuple[List[Tuple[int, ...]], Dict[Tuple[int, ...], int]]:
    state_len = window_len - 1
    states: List[Tuple[int, ...]] = []
    index: Dict[Tuple[int, ...], int] = {}

    def rec(pos: int, remaining: int, cur: List[int]) -> None:
        if pos == state_len:
            t = tuple(cur)
            index[t] = len(states)
            states.append(t)
            return
        for v in range(remaining + 1):
            cur.append(v)
            rec(pos + 1, remaining - v, cur)
            cur.pop()

    rec(0, max_total, [])
    return states, index


def _build_transitions(
    states: List[Tuple[int, ...]],
    index: Dict[Tuple[int, ...], int],
    max_total: int,
) -> List[List[Tuple[int, int]]]:
    trans: List[List[Tuple[int, int]]] = []
    for s in states:
        ssum = sum(s)
        opts: List[Tuple[int, int]] = []
        for c in range(max_total - ssum + 1):
            ns = s[1:] + (c,)
            opts.append((index[ns], c))
        trans.append(opts)
    return trans


def _trace_power_weighted(
    n_days: int,
    trans: List[List[Tuple[int, int]]],
    max_total: int,
    t: float,
) -> float:
    ratio = t / n_days
    w0 = 1.0
    w1 = ratio
    w2 = (ratio * ratio) * 0.5 if max_total >= 2 else 0.0
    w3 = (ratio * ratio * ratio) / 6.0 if max_total >= 3 else 0.0
    w = (w0, w1, w2, w3)

    num_states = len(trans)
    total = 0.0

    for start in range(num_states):
        v = [0.0] * num_states
        v[start] = 1.0
        for _ in range(n_days):
            nv = [0.0] * num_states
            for i in range(num_states):
                val = v[i]
                if val:
                    for j, c in trans[i]:
                        nv[j] += val * w[c]
            v = nv
        total += v[start]

    return total


def solve(
    n_days: int = 365,
    within_days: int = 7,
    target_people: int = 4,
    quad_n: int = 28,
) -> str:
    """Compute expected people until birthday collision using transfer matrix and Gauss-Laguerre."""
    window_len = within_days + 1
    max_total = target_people - 1

    states, index = _enumerate_states(window_len, max_total)
    trans = _build_transitions(states, index, max_total)

    xs, ws = _gauss_laguerre(quad_n)
    acc = 0.0
    for x, wgt in zip(xs, ws):
        acc += wgt * _trace_power_weighted(n_days, trans, max_total, x)

    return f"{acc:.8f}"


if __name__ == "__main__":
    print(solve())
