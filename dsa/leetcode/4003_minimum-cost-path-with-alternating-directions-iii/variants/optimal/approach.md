## General

The cheapest continuation from a cell depends not only on its coordinates but also on whether the next action occurs at an odd or even second. Treat `(cell, parity)` as a graph state. There are exactly two states per cell: parity zero permits right and down without an extra charge, while parity one permits left and up.

From each state, add one waiting edge back to the same cell with the opposite parity and weight equal to the current cell's penalty. Add an edge for every in-bounds orthogonal move, again to the opposite parity. Its weight is the destination's one-based row-column product, plus the current cell's penalty exactly when the direction is not permitted by the present parity. Initialize the odd-action state of the upper-left cell with distance $1$, its entrance cost.

Every legal timed walk in the grid follows exactly the corresponding sequence of edges in this state graph, with equal cost: the edge records the chosen action, all charges, and the mandatory parity toggle. Conversely, every state-graph path describes a legal sequence of grid actions. The original optimization problem is therefore a shortest-path problem on these states.

All edge weights are nonnegative, so Dijkstra's algorithm can finalize states in nondecreasing cost order. When either parity state of the destination is removed from the heap with its current best distance, no cheaper state-graph path to the destination can remain. Returning that distance gives the minimum possible journey cost.

## Complexity detail

Let $N=mn$. The graph has $2N$ states and at most five outgoing edges per state, so both its vertex and edge counts are $O(N)$. Binary-heap Dijkstra therefore takes $O(N\log N)=O(mn\log(mn))$ time. The distance array and heap can each contain $O(N)$ entries, giving $O(mn)$ auxiliary space.

## Alternatives and edge cases

- **Array-based Dijkstra:** Scanning all unsettled states for every next minimum remains correct, but raises the worst-case running time to $O((mn)^2)$.
- **Bellman-Ford relaxation:** It naturally supports the parity-state graph but ignores the nonnegative-weight advantage and can require $O((mn)^2)$ time.
- **Coordinate-only shortest paths:** Merging the two parity states is incorrect because identical cells can have different cheapest legal continuations on odd and even seconds.
- **Monotone-only movement:** Considering only right and down paths is insufficient; a left or up move can cheaply change both position and parity and participate in the optimum.
- **Waiting:** Waiting is a real edge, not merely a presentation detail, and can be strictly better than every route that moves each second.
- **Single row or column:** The same state graph applies even though only two movement directions can ever remain in bounds.
- **Zero penalties:** Zero-weight waiting edges and free direction violations are safe for Dijkstra; stale heap entries must still be discarded.
- **Destination parity:** Either parity is acceptable on arrival, and the algorithm returns before paying any destination wait or departure charge.
