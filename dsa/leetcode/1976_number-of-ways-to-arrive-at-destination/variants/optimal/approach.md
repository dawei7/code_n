## General

**Solve two tasks together**

The method must find the shortest travel time from intersection 0 to every intersection and count how many paths achieve each shortest time. The source extends Dijkstra's algorithm with a second array of path counts.

`dist[v]` is the best travel time currently known from 0 to `v`. `f[v]` is the number of paths achieving exactly that time. Initially, `dist[0] = 0` and `f[0] = 1` because the empty path reaches the source in one way with zero time. Every other distance starts at infinity and every other count starts at zero.

**Build the exact dense graph representation**

The source allocates an $n$-by-$n$ matrix `g` filled with infinity. For every undirected road `[u, v, t]`, it assigns both `g[u][v]` and `g[v][u]` to `t`. Infinity means that no direct road exists.

It also sets `g[0][0] = 0`, although the relaxation loop explicitly skips `j == t` and therefore does not need a self-edge for correctness.

This matrix gives constant-time road-weight lookup, but it is dense storage even when few roads exist. That detail changes the exact complexity from the sparse adjacency-list version usually associated with heap-based Dijkstra.

**Select the next finalized vertex**

On each of $n$ rounds, the inner selection loop scans every vertex and chooses the unvisited vertex `t` with the smallest current `dist`. It then marks `vis[t] = True`.

All road times are positive. Therefore, once `t` has the smallest tentative distance among unvisited vertices, no route passing through another unvisited vertex can later make `dist[t]` smaller. The distance is finalized exactly as in ordinary Dijkstra.

The graph is guaranteed connected, so some finite-distance unvisited vertex exists on every round. The source would need a guard for `t == -1` on a disconnected graph, but that situation is outside the contract.

**Relax a road and update its count**

For every vertex `j` other than `t`, the code computes

`ne = dist[t] + g[t][j]`.

If a road exists, `ne` is the travel time of reaching `j` through `t`. There are two important cases.

If `ne < dist[j]`, the route through `t` is strictly better than everything known before. The code replaces `dist[j]` with `ne` and assigns `f[j] = f[t]`. Old paths to `j` are longer and must not remain in its shortest-path count. Every shortest path to `t` can be extended by this road, giving exactly `f[t]` newly best paths.

If `ne == dist[j]`, the route has the same optimal time already known. It supplies a disjoint family of shortest paths distinguished by their predecessor `t`, so the code adds `f[t]` to `f[j]`.

If `ne > dist[j]`, the candidate is longer and changes nothing.

**Why counts are complete when a vertex is finalized**

Every road has strictly positive time. On any shortest path ending at `v`, the predecessor `u` satisfies `dist[u] < dist[v]`. Dijkstra therefore finalizes and relaxes `u` before it finalizes `v`. All shortest-path predecessors have contributed their counts to `f[v]` by that time.

Conversely, a count is added only when the candidate time equals the known shortest distance, or becomes the new shortest distance. Thus `f[v]` counts no longer route. Inducting over finalization order proves that finalized distances and counts are both correct.

**An infinity nuance in the exact matrix loop**

The code scans all `j` values, including non-neighbors. For a non-edge, `g[t][j]` is infinity and `ne` becomes infinity. If `dist[j]` is also infinity, the equality branch temporarily adds `f[t]` to `f[j]` even though no road exists.

This looks alarming, but connectedness prevents it from corrupting the final answer. Before any such `j` is selected, a real finite path eventually relaxes it. The strict-improvement branch then overwrites `f[j]` with the valid predecessor count. Once `dist[j]` is finite, a later infinite candidate is no longer equal. Skipping infinite matrix entries explicitly would be cleaner and avoid these meaningless temporary counts.

**Apply the modulus at the requested boundary**

The exact source accumulates path counts as ordinary Python integers and applies modulo $10^9+7$ only to `f[-1]` at return time. This is mathematically valid because reducing after additions gives the same residue as reducing each addition.

It may store larger integers than necessary, but Python integers do not overflow. Applying the modulus after each equal-distance addition would keep intermediate values bounded without changing the result.

**Actual algorithm used by the source**

Although the manifest names $O((V+E)\log V)$ time and $O(V+E)$ space, those are the bounds for adjacency-list Dijkstra with a binary heap. The concrete source uses neither. It uses an adjacency matrix and linear minimum selection, so it is the dense $O(V^2)$ Dijkstra variant. The explanation and exact bounds must follow the code that actually runs.

## Complexity detail

Let $V=n$ and let $E$ be the number of roads. Allocating and initializing `g` costs $O(V^2)$ time and space; inserting roads costs $O(E)$ time.

There are $V$ rounds. Each scans $V$ vertices to select `t` and another $V$ matrix entries to relax candidates, for $O(V^2)$ total time. Overall time is $O(V^2+E)=O(V^2)$ because $E=O(V^2)$.

The matrix uses $O(V^2)$ space. `dist`, `f`, and `vis` add $O(V)$. These exact bounds differ from the manifest's heap-based sparse-graph claims.

## Alternatives and edge cases

- **Heap Dijkstra with adjacency lists:** This achieves $O((V+E)\log V)$ time and $O(V+E)$ space and matches the manifest, especially benefiting sparse graphs.
- **Floyd-Warshall:** It can compute all-pairs distances but costs $O(V^3)$ and is unnecessary for one source.
- **Ordinary BFS:** It is incorrect because road times are positive but not necessarily equal.
- **Strictly shorter relaxation:** Replace both the distance and count; keeping the old count would include nonshortest paths.
- **Equal relaxation:** Add the predecessor count because it represents additional shortest paths.
- **Longer relaxation:** Ignore it completely.
- **Non-edge represented by infinity:** The exact code may temporarily add meaningless counts to still-infinite vertices, but a real finite relaxation overwrites them before finalization in the connected graph.
- **Connected graph:** This guarantee prevents selection from leaving `t` at negative one.
- **Positive weights:** They ensure every shortest-path predecessor is finalized before its successor; zero-weight roads would complicate count finalization.
- **Direct source-to-destination road:** It competes normally with multi-road routes of the same total time.
- **Large path count:** Python avoids overflow, and the result is reduced modulo $10^9+7$.
- **No early exit:** The source processes all vertices even after the destination is finalized; this does not affect correctness.
- **Input preservation:** Road rows are read into a new matrix and are not modified.
