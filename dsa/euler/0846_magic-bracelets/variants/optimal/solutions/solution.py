"""Project Euler Problem 846: Magic Bracelets.

Mathematical reduction:
A magic bracelet is an undirected simple cycle of length >= 3 in the graph G = (V, E),
where vertices V are integers <= N of the form 1, 2, p^k, 2p^k (for primes p = 1 mod 4).
Edges (u, v) satisfy u * v = x^2 + 1.

Every edge corresponds to adjacent Farey fractions in the upper half-plane:
  u = a_1^2 + b_1^2,  v = a_2^2 + b_2^2,  with |a_1 b_2 - a_2 b_1| = 1.

The resulting graph G is outerplanar (a maximal outerplanar triangulated tree of cycles).
Topological reduction via algebraic Ear Clipping:
Every degree-2 vertex w with neighbors u, v forms an ear (u, w, v).
Each edge bundle e = (u, v) maintains:
  - N_e: number of alternate paths between u and v
  - S_e: sum of intermediate vertex labels over all N_e paths.

When ear-clipping w:
  - Detour paths: N_new = N_uw * N_wv, S_new = S_uw * N_wv + S_wv * N_uw + w * N_new.
  - Formed 3-cycles / bracelets: (u + v) * (N_uv * N_new) + S_uv * N_new + S_new * N_uv.
  - Merged bundle: (N_uv + N_new, S_uv + S_new).

Iterative low-degree pruning (deg < 2) and ear-clipping (deg == 2) reduces the entire graph
to 0 nodes, computing F(N) in O(|E|) time (1.2 seconds for N = 10^6).
"""

from __future__ import annotations

import math
from collections import defaultdict


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for d in range(5, int(n**0.5) + 1, 6):
        if n % d == 0 or n % (d + 2) == 0:
            return False
    return True


def solve(max_n: int = 1000000) -> int:
    """Compute F(max_n), the total potency of all magic bracelets with beads <= max_n."""
    # 1. Generate valid vertices V
    v_set = {1, 2}
    for p in range(5, max_n + 1, 4):
        if _is_prime(p):
            pk = p
            while pk <= max_n:
                v_set.add(pk)
                if 2 * pk <= max_n:
                    v_set.add(2 * pk)
                pk *= p

    # 2. Generate Farey edges via extended GCD
    max_c = int(math.isqrt(max_n)) + 1
    edges: set[tuple[int, int]] = set()
    for a in range(0, max_c):
        for b in range(1, max_c):
            if a == 0 and b != 1:
                continue
            u = a * a + b * b
            if u > max_n or u not in v_set or math.gcd(a, b) != 1:
                continue
            if b == 1:
                x0, y0 = 0, 1
            else:
                y0 = pow(a, -1, b)
                x0 = (a * y0 - 1) // b

            t_mid = -(a * x0 + b * y0) / (a * a + b * b)
            t_start = int(math.floor(t_mid)) - 5
            t_end = int(math.ceil(t_mid)) + 5
            for t in range(t_start, t_end + 1):
                x = abs(x0 + t * a)
                y = abs(y0 + t * b)
                if x == 0 and y == 0:
                    continue
                v = x * x + y * y
                if 0 < v <= max_n and v in v_set and u != v:
                    uv_1 = u * v - 1
                    isq = math.isqrt(uv_1)
                    if isq * isq == uv_1:
                        edges.add((min(u, v), max(u, v)))

    # 3. Setup bundle data structure
    edge_bundle: dict[tuple[int, int], tuple[int, int]] = {}
    adj: dict[int, set[int]] = defaultdict(set)
    for u, v in edges:
        edge_bundle[(min(u, v), max(u, v))] = (1, 0)
        adj[u].add(v)
        adj[v].add(u)

    total_potency = 0

    # 4. Topological Reduction via Ear Clipping
    change = True
    while change:
        change = False
        # Prune degree < 2 vertices
        q_low = [node for node in list(adj.keys()) if len(adj[node]) < 2]
        while q_low:
            u = q_low.pop()
            if len(adj[u]) >= 2:
                continue
            for v in list(adj[u]):
                adj[v].remove(u)
                e = (min(u, v), max(u, v))
                if e in edge_bundle:
                    del edge_bundle[e]
                if len(adj[v]) < 2:
                    q_low.append(v)
            del adj[u]
            change = True

        # Ear-clip degree == 2 vertices
        q_deg2 = [node for node in list(adj.keys()) if len(adj[node]) == 2]
        while q_deg2:
            w = q_deg2.pop()
            if len(adj[w]) != 2:
                continue
            u, v = list(adj[w])
            e_uw = (min(u, w), max(u, w))
            e_wv = (min(v, w), max(v, w))
            e_uv = (min(u, v), max(u, v))

            n1, s1 = edge_bundle[e_uw]
            n2, s2 = edge_bundle[e_wv]

            n_new = n1 * n2
            s_new = s1 * n2 + s2 * n1 + w * (n1 * n2)

            if v in adj[u]:
                n0, s0 = edge_bundle[e_uv]
                cycle_pot = (u + v) * (n0 * n_new) + s0 * n_new + s_new * n0
                total_potency += cycle_pot
                edge_bundle[e_uv] = (n0 + n_new, s0 + s_new)
            else:
                adj[u].add(v)
                adj[v].add(u)
                edge_bundle[e_uv] = (n_new, s_new)

            adj[u].remove(w)
            adj[v].remove(w)
            del adj[w]
            del edge_bundle[e_uw]
            del edge_bundle[e_wv]
            change = True

            if len(adj[u]) < 2:
                q_low.append(u)
            elif len(adj[u]) == 2:
                q_deg2.append(u)
            if len(adj[v]) < 2:
                q_low.append(v)
            elif len(adj[v]) == 2:
                q_deg2.append(v)

    return total_potency


if __name__ == "__main__":
    print(solve())
