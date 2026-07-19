## General
**Replace additive distance with a bottleneck distance.** For each cell, store the smallest route effort currently known from the start. Extending a route with an edge of height difference $w$ produces effort `max(current_effort, w)`. This relaxation is monotone: extending a route can never reduce its effort.

**Run Dijkstra with the minimax relaxation.** Put `(0,0)` in a min-heap with effort zero. Repeatedly remove the cell with the least tentative effort and relax its four neighbors using the maximum rule. Ignore stale heap entries whose effort no longer matches the cell's best record. Once the destination is removed, return its effort.

The standard Dijkstra finalization argument still applies. Suppose the removed cell had an undiscovered route with a smaller bottleneck. Along that route, the first not-yet-removed cell follows a removed predecessor whose effort was no greater; relaxing their edge would have inserted a heap candidate no larger than the claimed route effort. That candidate would precede the current removal, a contradiction. Thus the destination's first current heap removal is the optimum.

## Complexity detail
The grid graph has $V=RC$ vertices and fewer than $4V$ directed neighbor edges. Each successful relaxation adds one heap entry, and heap operations cost $O(\log V)$, giving $O(V\log V)$ time. The effort matrix and heap use $O(V)$ space.

## Alternatives and edge cases
- **Binary search plus reachability:** Search an effort threshold and run DFS or BFS using only admissible edges. This takes $O(V\log H)$ time for height range $H$ and is often practical.
- **Kruskal union-find:** Sort adjacent edges by difference and union them until start and destination connect. This also takes $O(V\log V)$ time.
- **Array-based Dijkstra:** Selecting the next cell by scanning every unsettled vertex preserves correctness but takes $O(V^2)$ time.
- A one-cell grid requires no moves and therefore has effort zero.
- A route may use more steps to avoid one large height jump; path length is not the objective.
- Flat connected regions can be traversed at zero effort.
- Movement is four-directional only; diagonal cells are not adjacent.
