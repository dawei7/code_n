"""Project Euler Problem 762: Amoebas in a 2D Grid.

Find the last 9 digits of C(100000), where C(N) is the number of distinct configurations
of N+1 amoebas on a 4-row grid reachable after N divisions starting from (0,0).
"""

from typing import Dict, List, Tuple

_MOD = 1_000_000_000


def _popcount4(mask: int) -> int:
    return (mask & 1) + ((mask >> 1) & 1) + ((mask >> 2) & 1) + ((mask >> 3) & 1)


def _expand(prev: Tuple[int, int, int, int]) -> Tuple[int, int, int, int]:
    a0, a1, a2, a3 = prev
    return (a0 + a3, a1 + a0, a2 + a1, a3 + a2)


def _build_states() -> Tuple[List[Tuple[int, int, int, int]], Dict[Tuple[int, int, int, int], int]]:
    states = []
    idx = {}
    for a0 in range(4):
        for a1 in range(4 - a0):
            for a2 in range(4 - a0 - a1):
                for a3 in range(4 - a0 - a1 - a2):
                    t = (a0, a1, a2, a3)
                    idx[t] = len(states)
                    states.append(t)
    return states, idx


def _build_transitions(
    states: List[Tuple[int, int, int, int]],
    idx: Dict[Tuple[int, int, int, int], int],
):
    s_count = len(states)
    terminal = idx[(0, 0, 0, 0)]
    pop = [_popcount4(m) for m in range(16)]

    to_nonterm = [[] for _ in range(s_count)]
    to_term_w = [[] for _ in range(s_count)]

    for u, s in enumerate(states):
        if u == terminal:
            continue
        t = _expand(s)
        for mask in range(16):
            b0 = mask & 1
            b1 = (mask >> 1) & 1
            b2 = (mask >> 2) & 1
            b3 = (mask >> 3) & 1
            n0 = t[0] - b0
            n1 = t[1] - b1
            n2 = t[2] - b2
            n3 = t[3] - b3
            if n0 < 0 or n1 < 0 or n2 < 0 or n3 < 0:
                continue
            if n0 + n1 + n2 + n3 > 3:
                continue
            v = idx.get((n0, n1, n2, n3))
            if v is None:
                continue
            w = pop[mask]
            if v == terminal:
                to_term_w[u].append(w)
            else:
                to_nonterm[u].append((v, w))

    return terminal, to_nonterm, to_term_w


def solve(target_n: int = 100_000) -> str:
    """Compute C(target_n) mod 10^9 using column shot-vector dynamic programming."""
    states, idx = _build_states()
    terminal, to_nonterm, to_term_w = _build_transitions(states, idx)
    order = sorted(range(len(states)), key=lambda i: (sum(states[i]), states[i]))
    start = idx[(1, 0, 0, 0)]

    mmax = target_n + 1
    end = [0] * (mmax + 1)

    layers = [[0] * len(states) for _ in range(5)]
    layers[0][start] = 1

    for m in range(mmax + 1):
        cur = layers[0]
        for u in order:
            val = cur[u]
            if not val:
                continue

            for w in to_term_w[u]:
                nm = m + w
                if nm <= mmax:
                    end[nm] = (end[nm] + val) % _MOD

            for v, w in to_nonterm[u]:
                nm = m + w
                if nm > mmax:
                    continue
                if w == 0:
                    cur[v] = (cur[v] + val) % _MOD
                else:
                    layers[w][v] = (layers[w][v] + val) % _MOD

        layers.pop(0)
        layers.append([0] * len(states))

    ans = end[target_n + 1] % _MOD if target_n > 0 else 1
    return f"{ans:09d}"


if __name__ == "__main__":
    print(solve())
