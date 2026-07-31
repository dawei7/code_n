## General

Treat each cell as a graph vertex whose distance is the earliest time at which that cell can be occupied. Moving across a grid edge costs one second, but the destination cell may impose a later release time. Since reaching a cell earlier can never reduce the choices available afterward, these time-dependent transitions preserve the ordering needed by Dijkstra's algorithm.

**Why the first move is exceptional:** Once at least one move has been made, the path contains an accessible neighboring cell. Traversing that edge in both directions consumes two seconds, so it can be used to pass time without remaining stationary. At `(0, 0)`, no such edge exists yet. If both `(0, 1)` and `(1, 0)` require a time greater than $1$, no legal move can be made at time $1$, and the answer is `-1`.

**Deriving the parity adjustment:** Suppose a cell is finalized at time $t$. A neighboring cell can ordinarily be reached at `t + 1`. If its requirement $g$ is larger, moving back and forth permits arrival times `t + 1`, `t + 3`, `t + 5`, and so on. Therefore the earliest legal delayed arrival is

$$
g + ((g-(t+1)) \bmod 2).
$$

It is $g$ when $g$ has the reachable parity and $g+1$ otherwise. This is not permission to wait in place; it summarizes the two-step oscillations that precede the move.

Maintain an `earliest` matrix and a min-heap of `(time, row, col)`. Relax each cardinal neighbor with the parity-adjusted arrival time. Ignore stale heap entries whose time no longer matches `earliest`. When the destination is removed from the heap, its time is minimal: every unsettled state has an equal or later heap key, and every transition from a finalized state uses the earliest legal traversal time. Dijkstra's standard cut argument therefore applies.

## Complexity detail

There are $mn$ vertices and fewer than $4mn$ directed neighbor transitions. Each successful relaxation adds a heap entry, so the running time is $O(mn \log(mn))$. The distance matrix and heap use $O(mn)$ space.

## Alternatives and edge cases

- **Queue-only breadth-first search:** Unit movement time does not make ordinary BFS sufficient because cell release times create different effective arrival times; a min-heap must select the globally earliest state.
- **Quadratic Dijkstra scan:** Repeatedly scanning every unsettled cell for the smallest distance is correct, but costs $O((mn)^2)$ time and is too slow for as many as $10^5$ cells.
- **Visited on insertion:** Marking a cell final when it is first pushed can discard a later-discovered earlier route. A cell becomes final only when its current minimum time is popped.
- **Blocked start:** If both neighbors of `(0, 0)` exceed $1$, returning `-1` immediately is necessary because no oscillation edge has been established.
- **Exact versus mismatched parity:** A release time can be used exactly only when it differs from `t + 1` by an even number; otherwise the earliest arrival is one second later.
