## General

All edge weights are positive, so Dijkstra's algorithm discovers nodes in non-decreasing order of their true shortest distance from `s`. Build the directed adjacency list, initialize the source distance to zero, and place `(0, s)` in a min-heap.

**Stop at the first marked node.** Remove the smallest-distance entry from the heap and ignore it when a newer, smaller distance for the same node is already known. Otherwise the popped distance is final. If that node is marked, no unprocessed path can reach it or any other marked node more cheaply, so return immediately.

For an unmarked node, relax every outgoing edge. Whenever traveling through that node improves a neighbor's known distance, record the new value and push it into the heap. If the heap becomes empty before a marked node is finalized, none is reachable and the required result is `-1`.

## Complexity detail

Let $e$ be the number of directed edges. Constructing the adjacency list takes $O(n+e)$ time. With a binary heap, Dijkstra's relaxations and heap operations take $O((n+e)\log n)$ time. The adjacency list, distance array, marked-node set, and heap use $O(n+e)$ auxiliary space.

## Alternatives and edge cases

- **Bellman-Ford:** Repeatedly relaxing every edge handles negative weights too, but those are absent here and its $O(ne)$ time is unnecessarily slow.
- **Run Dijkstra to completion:** Computing every reachable distance and then taking the minimum over `marked` has the same worst-case bound, but misses the safe early exit at the first finalized marked node.
- **Floyd-Warshall:** All-pairs shortest paths take $O(n^3)$ time and $O(n^2)$ space even though only one source is queried.
- Edge direction matters; an edge from `u` to `v` does not permit travel from `v` to `u`.
- Parallel edges are legal, and ordinary relaxation naturally keeps whichever route produces the smaller distance.
- A marked node discovered by relaxation is not necessarily optimal yet; return only when it is removed from the heap with its current best distance.
- Positive path sums can exceed one edge's $10^6$ bound, so fixed-width languages need a sufficiently wide integer type.
- If every marked node lies outside the source's reachable component, the heap empties and the answer is `-1`.
