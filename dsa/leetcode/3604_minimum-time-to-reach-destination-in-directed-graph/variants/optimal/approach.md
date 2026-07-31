## General

Build an outgoing adjacency list from the directed edges. For a node reached at time `time`, an edge `[u, v, start, end]` has only two relevant cases. If `time > end`, its availability has already expired and no amount of waiting can restore it. Otherwise the earliest departure is `max(time, start)`, so the earliest arrival at `v` through that edge is `max(time, start) + 1`.

These time-dependent transitions satisfy the FIFO property: arriving later at the same node can never produce an earlier arrival through an edge, because `max(time, start) + 1` is non-decreasing in `time`. It is therefore sufficient to retain only the earliest known time for each node, and Dijkstra's greedy finalization remains valid.

Initialize node `0` with time `0` and put it in a min-heap. Repeatedly remove the smallest current arrival, skip stale heap entries, and relax every outgoing edge with the formula above. When the destination is removed as a current heap entry, no unsettled path can arrive earlier, so return that time. If the heap empties first, every reachable state has been exhausted and the answer is `-1`.

## Complexity detail

Let $m$ be the number of edges. Constructing and scanning the adjacency lists costs $O(n+m)$. At most one successful improvement per edge enters the heap, and each heap operation costs $O(\log n)$ under the graph bounds, giving $O((n+m)\log n)$ time. The adjacency list, distance array, and heap use $O(n+m)$ space.

The benchmark defines size $S=n$ on reverse-ordered directed chains with $m=n-1$. Dijkstra settles the chain once. A calibrated time-aware Bellman–Ford alternative scans the reverse edge order repeatedly, advances only one hop per pass, and takes $\Theta(nm)=\Theta(S^2)$ work while preserving every expected answer.

## Alternatives and edge cases

- **Time-aware Bellman–Ford:** Repeatedly relaxing all edges is correct because useful paths need no cycle, but it can take $O(nm)$ time.
- **Breadth-first search:** Every traversal lasts one unit, but variable waiting times make the effective transition costs nonuniform, so FIFO order does not guarantee earliest arrival.
- **Time-expanded graph:** Creating a state for every node and time is impossible when endpoints reach $10^9$; waiting should be collapsed into `max(time, start)`.
- **Window opens later:** Waiting until `start` is always optimal when the current time is earlier and the edge has not expired.
- **Inclusive closing time:** An edge may still be entered when `time == end`; reject it only when `time > end`.
- **Expired edge:** Once the earliest arrival at its source exceeds `end`, later arrivals cannot use it either.
- **Parallel edges:** Different windows may make either directed edge instance preferable, so retain and relax all of them.
- **Cycles:** Traversing a cycle only increases time; stale-entry filtering prevents repeated worse arrivals from causing work.
- **Start is destination:** When `n = 1`, the minimum time is `0` without traversing an edge.
- **Unreachable destination:** Exhausting the heap yields `-1`.
