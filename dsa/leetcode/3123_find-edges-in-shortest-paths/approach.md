## General

**First compute shortest distances from node zero.** The source builds an undirected adjacency list. Every neighbor tuple contains the other endpoint, edge weight, and original edge index so a later traversal can mark the correct Boolean result.

It runs Dijkstra from node zero because all weights are positive. `dist[v]` becomes the shortest distance from zero to `v`. Stale heap entries with `da > dist[a]` are skipped, and a relaxation updates only on a strictly shorter route.

If `dist[n - 1]` remains infinity, no path from zero to the destination exists. Then no edge can belong to a shortest path, and the all-false result is returned immediately.

**A tight directed edge preserves shortest distance.** Consider undirected edge between `b` and `a` with weight `w`. It can be traversed from `b` to `a` along a shortest path from zero exactly when:

$$
\texttt{dist[b]}+w=\texttt{dist[a]}.
$$

The source tests the equivalent form `dist[a] == dist[b] + w` while walking backward from the destination. Such an orientation is called tight: the shortest prefix to `b` plus this edge reaches `a` at its shortest possible distance.

Positive weights imply `dist[b] < dist[a]` for every tight backward step. Thus tight edges point from smaller to larger distance in forward paths and form an acyclic structure when oriented by increasing distance.

**Walk backward through the shortest-path structure.** The queue begins with destination `n - 1`. When node `a` is processed, every neighbor `b` satisfying the tight equality can precede `a` on a shortest route from zero. Because `a` is already known to connect onward to the destination through tight edges, combining:

1. a shortest path from zero to `b`;
2. edge `b -> a`; and
3. the known tight suffix from `a` to the destination

produces a complete route of total length `dist[n - 1]`. The source marks that edge index true and enqueues `b`.

Edges failing equality cannot follow a shortest zero-to-`a` prefix and are not marked through that orientation.

**Why one distance array is enough conceptually.** A common solution runs Dijkstra from both endpoints and tests whether an edge completes the global distance in either orientation. This source instead discovers the destination-reachable part of the tight-edge graph by reverse traversal. Every reached node has a tight suffix to the destination, so a second numeric distance array is unnecessary for correctness.

**A correctness argument.** Every marked edge is tight into a node already connected to the destination by tight edges. Concatenating the shortest prefix and tight suffix proves it lies on at least one shortest complete path.

Conversely, take any edge on a shortest path. Every prefix of a positive-weight shortest path is itself shortest, so the edge satisfies the tight equality. Starting at the destination and following that path backward eventually processes its later endpoint and marks the edge. Therefore, the logical set of marked edges is exact.

**A major performance defect in the exact reverse traversal.** The deque walk has no visited set and does not check whether a node or edge was already expanded before enqueuing. A node with several shortest-path suffixes can be enqueued once through each suffix. Its predecessors are then expanded repeatedly.

In a layered shortest-path DAG, the number of shortest paths can be exponential even when the graph has only polynomially many nodes and edges. The source can consequently process the same node and adjacency list exponentially many times. Setting `ans[i] = True` does not prevent the repeated `q.append(b)`.

The traversal still terminates because every backward tight step strictly decreases `dist`, so there is no tight cycle. Its result remains correct, but the advertised near-linear complexity is not guaranteed. Adding a visited Boolean and expanding each reached node only once would fix this defect without changing which edges are marked.

**Manifest mismatch.** The manifest describes Dijkstra from both endpoints. `solution.py` performs one Dijkstra and an un-deduplicated reverse tight-edge traversal. Both the mechanism and the exact worst-case complexity therefore differ.

## Complexity detail

Building the adjacency list costs $O(n+m)$ space and $O(m)$ time. Dijkstra costs $O((n+m)\log n)$ time with the heap.

Let $R$ be the total number of adjacency-entry examinations performed by the reverse queue, counting repeated expansions. That phase costs $O(R)$ time and can use a queue proportional to the number of generated path-prefix occurrences. Without deduplication, $R$ can be exponential in a layered graph because it follows shortest-path multiplicities rather than unique nodes.

The honest exact bound is therefore $O((n+m)\log n+R)$ time, with $R$ potentially exponential. Base graph, distance, heap, and answer storage are $O(n+m)$, but the defective reverse queue can also grow beyond $O(n)$ through duplicates.

## Alternatives and edge cases

- **Add a visited set to reverse traversal:** Process each tight-reachable node once, yielding $O(n+m)$ reverse work while marking all its tight incoming edges.
- **Two Dijkstra runs:** Compute distances from zero and destination, then test both edge orientations against the global shortest distance. This matches the manifest.
- **Destination unreachable:** Return all false before reverse traversal.
- **Several shortest paths:** Every edge in their union should be true.
- **Edge tight from zero but not destination-reachable:** Reverse traversal never reaches its later endpoint, so it remains false.
- **Positive weights:** Ensure distances strictly decrease backward and prevent tight cycles.
- **No repeated input edges:** Given, though different shortest routes can still merge and split.
- **Stale Dijkstra entries:** Skipped by comparing popped and stored distances.
- **Direction of an undirected edge:** The reverse equality automatically chooses the orientation from smaller to larger shortest distance.
- **An edge not satisfying equality:** Cannot lie on a shortest prefix in that orientation.
- **Duplicate queue entries:** They do not change truth values but can destroy performance.
- **Boolean idempotence:** Re-marking true is harmless for correctness, not for runtime.
- **One direct shortest edge:** Destination processing marks it and reaches node zero.
- **Disconnected side components:** Their distances remain infinity and they are never reverse-reached.
- **Source/manifest mismatch:** Exact source uses one Dijkstra and has an exponential revisit risk absent from the claimed bound.
