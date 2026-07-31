## General

**Disappearance times filter otherwise ordinary paths.** All edge lengths are positive, so reaching a node earlier is never worse than reaching it later: an earlier arrival satisfies every disappearance deadline that a later arrival could satisfy and leaves at least as much time for subsequent edges. This preserves the greedy condition needed by Dijkstra's algorithm.

Build an adjacency list for the undirected graph. Store the best known arrival time for every node and place candidate pairs `(time, node)` in a min-heap, beginning with `(0, 0)`. When a pair is popped, ignore it if its time no longer equals the node's best known distance; a shorter relaxation has already superseded it.

**Relax only valid arrivals.** For an edge of length `length` from a node reached at `time`, the proposed arrival is `time + length`. Update the neighbor only when this value is smaller than its recorded distance and strictly smaller than `disappear[neighbor]`. The strict comparison enforces that arrival at the disappearance instant is invalid.

When a current pair is removed from the min-heap, every unprocessed candidate arrival is no smaller. Because all lengths are positive, any alternative route to that node through an unprocessed vertex would arrive no earlier. Invalid arrivals cannot become valid by adding more positive-length edges. Thus the popped distance is final, exactly as in Dijkstra's algorithm, and every reachable node receives its minimum valid arrival time. Nodes left at infinity have no valid route and become $-1$ in the result.

## Complexity detail

Let $n$ be the number of nodes and $m$ the number of edges defined in the function contract. Building the adjacency list takes $O(n+m)$ space. Each successful relaxation adds a heap entry, and stale entries are discarded when popped, giving $O((n+m) \log n)$ time and $O(n+m)$ auxiliary space.

## Alternatives and edge cases

- **Bellman-Ford relaxation:** Repeatedly scanning every edge can enforce the same disappearance condition, but it takes $O(nm)$ time and is unnecessary because every edge length is positive.
- **Array-based Dijkstra:** Selecting the smallest unsettled distance with a linear scan avoids a heap but takes $O(n^2+m)$ time.
- **Breadth-first search:** BFS minimizes edge count, not total traversal time, so it fails when edge lengths differ.
- **Arrival at the deadline:** The condition is `arrival < disappear[node]`; equality means the node has already disappeared.
- **Disconnected graph:** Nodes outside node $0$'s component remain unreachable and are returned as $-1$.
- **Parallel edges:** Keep every edge in the adjacency list; Dijkstra naturally chooses whichever yields the earliest valid arrival.
- **Self-loops:** Positive self-loops cannot improve a distance and are harmless.
- **Source node:** Node $0$ is occupied at time $0$, which is valid because every disappearance time is at least $1$.
- **Stale heap entries:** A node may be queued more than once, so compare each popped time with the current best distance before scanning its edges.
