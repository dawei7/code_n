## General

**This is a shortest-path problem with a deadline at every destination.** Every edge length is positive, so Dijkstra's algorithm is the natural basis. The added rule is strict: node `v` can be visited only at a time smaller than `disappear[v]`. Arriving exactly when it disappears is too late.

The source builds an undirected adjacency list `g`. For edge `[u,v,w]` it stores `(v,w)` under `u` and `(u,w)` under `v`. Multiple edges are retained independently, and disconnected components cause no special construction issue.

**Distance state and priority queue.** `dist[v]` is the best valid arrival time discovered for node `v`. All entries begin at infinity except `dist[0]=0`. The queue starts with `(0,0)` and orders pairs by arrival time, so the smallest tentative distance is processed first.

The contract guarantees `disappear[0] >= 1`, so time zero is a valid visit to the starting node.

**Skip stale heap entries.** Dijkstra may push a node more than once when successively shorter routes are found. When pair `(du,u)` is popped, `du > dist[u]` means a newer, better entry has already been recorded. Expanding the stale route cannot improve anything, so the source continues.

If `du == dist[u]`, the popped route is current. Every stored finite distance was admitted only after passing its node's disappearance check, so `u` is known to have been reached while it existed.

**Relax an edge only when both improvements hold.** For neighbor `v` through edge weight `w`, candidate arrival is:

`dist[u] + w`.

The source accepts it only if:

1. it is smaller than the best known `dist[v]`; and
2. it is strictly smaller than `disappear[v]`.

The second condition must use `<`, not `<=`. The examples explicitly show that arrival exactly at the disappearance time is invalid.

When both tests pass, the candidate becomes `dist[v]` and is pushed. A route arriving after a node disappears cannot use that node as a waypoint either, so discarding it at relaxation is safe and necessary.

**Why ordinary Dijkstra correctness still applies.** Removing invalid arrivals leaves a graph of feasible time-respecting route prefixes. Edge weights remain positive. When a current minimum-distance queue entry for `u` is processed, no unprocessed route can later reach `u` earlier: any such route would have a prefix with at least that queue priority and a positive final edge. Deadline checks only remove routes; they do not create a negative or time-reducing transition.

Thus, the usual greedy settlement reasoning holds for every finite `dist`. If the algorithm never records a valid arrival for a node, no path from zero reaches it before its deadline.

**A trace for the second example.** From node zero, the edge to one gives time two, which is below `disappear[1]=3`, so it is accepted. The direct edge to two gives four, below five, and is also accepted. Popping node one at time two offers node two at time three. Three improves four and is below five, so `dist[2]` becomes three.

In the first example, the same arrival time two for node one is not below its disappearance time one, so it is rejected. Node two remains reachable directly at time four.

**Why waiting never helps.** Edge lengths are positive and node availability only decreases over time. Waiting makes every later arrival equal or worse and cannot cause a disappeared node to reappear. Therefore, shortest travel-time paths cover every optimal possibility without an explicit wait operation.

**Final conversion to -1.** The list comprehension pairs each `dist` value with its disappearance time. It returns the distance only when `a < b`; otherwise it returns -1. All finite nonzero-node distances should already satisfy that condition because of relaxation filtering. The final check also converts infinity and defensively reasserts the deadline contract.

## Complexity detail

Let $m$ be the number of undirected edges. The adjacency list stores $2m$ neighbor entries and takes $O(n+m)$ space. Distance and heap state add $O(n)$ to $O(m)$ entries depending on successful improvements.

Each relaxation can cause a heap push, and heap operations cost $O(\log n)$ under the standard bound. Building and scanning the graph costs $O(n+m)$. Overall time is $O((n+m)\log n)$, commonly also written $O(m\log n)$ for a connected graph.

Auxiliary space is $O(n+m)$ for the adjacency list, distance array, and priority queue. The answer comprehension creates the required $O(n)$ output list.

## Alternatives and edge cases

- **Bellman-Ford:** It supports negative edges, which this problem does not have, and would be far slower.
- **BFS:** Correct only if all edge lengths are equal; arbitrary positive lengths require a priority queue.
- **Deadline-expanded state graph:** Unnecessary because arriving earlier always dominates arriving later at the same node.
- **Arrival exactly at disappearance:** Invalid; the check is strictly `candidate < disappear[v]`.
- **Starting node:** Time zero is valid because all disappearance values are at least one.
- **Disconnected node:** Its distance stays infinity and becomes -1.
- **Multiple edges:** Each is relaxed; the faster useful one can win.
- **Stale queue entry:** `du > dist[u]` prevents redundant expansion.
- **A later but still valid arrival:** It is ignored when a shorter valid arrival already exists because earlier dominates it for all future deadlines.
- **No waiting:** Waiting cannot improve a deadline-constrained positive-weight route.
- **Destination usable as a waypoint:** Only if it was reached before disappearing, which every finite stored distance guarantees.
- **Large path sums:** Python integers avoid overflow; fixed-width implementations should use 64-bit distances.
- **Node zero in final conversion:** `0 < disappear[0]`, so it remains zero.
- **Graph with no edges:** Only node zero is reachable.
- **Final defensive comparison:** It converts infinity and protects the stated strict boundary even though relaxations already enforce it.
