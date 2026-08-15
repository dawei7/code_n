"""Project Euler 289: Eulerian Cycles

Find the number of non-crossing Eulerian paths L(6, 10) mod 10^10 on the grid of circles E(6, 10).
"""

from __future__ import annotations


def catalan_pairings(items: list[tuple[str, int, int]]) -> list[tuple[tuple[tuple[str, int, int], tuple[str, int, int]], ...]]:
    """Generates all Catalan non-crossing pairings of 2k items on a circle."""
    if not items:
        return [()]
    first = items[0]
    res: list[tuple] = []
    for i in range(1, len(items), 2):
        paired = items[i]
        left = items[1:i]
        right = items[i + 1:]
        for l_p in catalan_pairings(left):
            for r_p in catalan_pairings(right):
                res.append(((first, paired),) + l_p + r_p)
    return res


def canonicalize(comp_labels: list[int]) -> tuple[int, ...]:
    """Relabels component IDs in standard canonical 1-based order from left to right."""
    mapping: dict[int, int] = {}
    res: list[int] = []
    for x in comp_labels:
        if x not in mapping:
            mapping[x] = len(mapping) + 1
        res.append(mapping[x])
    return tuple(res)


def is_ending(arc: tuple[str, int, int], v: tuple[int, int]) -> bool:
    """Checks whether the given arc terminates at vertex v in sweep order."""
    name, x, y = arc
    if name == "B":
        return v == (x + 1, y)
    if name == "R":
        return v == (x + 1, y + 1)
    if name == "T":
        return v == (x + 1, y + 1)
    if name == "L":
        return v == (x, y + 1)
    return False


def solve(m: int = 6, n: int = 10, mod: int = 10**10) -> str:
    """Calculates L(m, n) mod 10^10 using Frontier / Profile Dynamic Programming.

    At each of the (m + 1) * (n + 1) lattice vertices in lexicographic order (vy, vx),
    the incident arcs must be paired into a non-crossing Catalan chord matching.
    The DP state maintains the planar connectivity equivalence classes of active open arcs
    crossing the sweep frontier.
    """
    if m > n:
        m, n = n, m

    vertices = [(vx, vy) for vy in range(n + 1) for vx in range(m + 1)]

    vertex_arcs: dict[tuple[int, int], list[tuple[str, int, int]]] = {}
    for vx, vy in vertices:
        arcs: list[tuple[str, int, int]] = []
        if vx < m and vy < n:
            arcs.append(("L", vx, vy))
        if vx > 0 and vy < n:
            arcs.append(("R", vx - 1, vy))
        if vx > 0 and vy < n:
            arcs.append(("B", vx - 1, vy))
        if vx > 0 and vy > 0:
            arcs.append(("T", vx - 1, vy - 1))
        if vx > 0 and vy > 0:
            arcs.append(("R", vx - 1, vy - 1))
        if vx < m and vy > 0:
            arcs.append(("L", vx, vy - 1))
        if vx < m and vy > 0:
            arcs.append(("T", vx, vy - 1))
        if vx < m and vy < n:
            arcs.append(("B", vx, vy))
        vertex_arcs[(vx, vy)] = arcs

    active_arcs_at_step: list[list[tuple[str, int, int]]] = []
    current_active: list[tuple[str, int, int]] = []

    for vx, vy in vertices:
        active_arcs_at_step.append(list(current_active))
        arcs = vertex_arcs[(vx, vy)]
        for a in arcs:
            if is_ending(a, (vx, vy)):
                current_active.remove(a)
            else:
                current_active.append(a)

    dp: dict[tuple[int, ...], int] = {(): 1}
    total_vertices = len(vertices)

    for v_idx, (vx, vy) in enumerate(vertices):
        cur_active = active_arcs_at_step[v_idx]
        arcs = vertex_arcs[(vx, vy)]
        pairings = catalan_pairings(arcs)

        ending_arcs = set(a for a in arcs if is_ending(a, (vx, vy)))
        starting_arcs = [a for a in arcs if not is_ending(a, (vx, vy))]
        next_active = [a for a in cur_active if a not in ending_arcs] + starting_arcs

        next_dp: dict[tuple[int, ...], int] = {}
        is_last_vertex = v_idx == total_vertices - 1

        for state, count in dp.items():
            arc_to_comp = {cur_active[i]: state[i] for i in range(len(cur_active))}

            for p in pairings:
                parent: dict[int, int] = {}

                def find(i: int) -> int:
                    path: list[int] = []
                    while parent.get(i, i) != i:
                        path.append(i)
                        i = parent[i]
                    for node in path:
                        parent[node] = i
                    return i

                def union(i: int, j: int) -> bool:
                    ri = find(i)
                    rj = find(j)
                    if ri != rj:
                        parent[ri] = rj
                        return True
                    return False

                local_new_id = 1000
                local_arc_comp: dict[tuple[str, int, int], int] = {}
                for a in arcs:
                    if a in arc_to_comp:
                        local_arc_comp[a] = arc_to_comp[a]
                    else:
                        local_arc_comp[a] = local_new_id
                        local_new_id += 1

                early_cycle = False
                for a1, a2 in p:
                    c1 = local_arc_comp[a1]
                    c2 = local_arc_comp[a2]
                    if not union(c1, c2):
                        early_cycle = True

                if is_last_vertex:
                    if len(next_active) == 0:
                        roots = {find(c) for c in local_arc_comp.values()}
                        if len(roots) == 1:
                            next_dp[()] = (next_dp.get((), 0) + count) % mod
                else:
                    if early_cycle:
                        continue

                    next_state_raw: list[int] = []
                    for a in next_active:
                        comp_val = local_arc_comp[a] if a in local_arc_comp else arc_to_comp[a]
                        next_state_raw.append(find(comp_val))
                    next_state = canonicalize(next_state_raw)
                    next_dp[next_state] = (next_dp.get(next_state, 0) + count) % mod

        dp = next_dp

    ans = dp.get((), 0)
    return str(ans)


if __name__ == "__main__":
    print(solve())
