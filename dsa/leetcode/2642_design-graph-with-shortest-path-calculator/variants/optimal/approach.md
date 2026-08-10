## General

**Store direct edge costs in a matrix**

The graph has at most 100 nodes and receives both edge additions and shortest-path queries.

The constructor allocates an $n\times n$ matrix `g` filled with infinity. For every directed input edge $(f,t,c)$, it stores:

`g[f][t] = c`.

Infinity means no direct edge. Only the forward entry changes because the graph is directed; `g[t][f]` remains unrelated unless that reverse edge is explicitly supplied.

The contract guarantees no repeated edge and no self-loop, so one matrix cell represents at most one direct edge.

**Adding an edge is one assignment**

`addEdge([f,t,c])` simply sets `g[f][t] = c`.

The matrix reserves every possible ordered node pair during construction, so no adjacency list needs resizing and no existing path table needs updating.

Future shortest-path calls read the new edge automatically. Previously returned answers are not cached, so there is no stale result to invalidate.

**Run array-based Dijkstra for each query**

All edge costs are positive. Dijkstra's algorithm can therefore settle nodes in increasing shortest-known distance.

For one `shortestPath(node1, node2)` call:

- `dist` starts as infinity for every node;
- source distance is zero;
- `vis` marks which nodes have been finalized.

The algorithm performs $n$ rounds. In each round, it finds the unvisited node `t` with the smallest `dist[t]` by scanning all nodes.

It marks `t` visited, then tries every possible destination `j`:

`dist[j] = min(dist[j], dist[t] + g[t][j])`.

If no direct edge $t\to j$ exists, `g[t][j]` is infinity and cannot improve a finite distance.

**Why the minimum unvisited node can be finalized**

Suppose `t` has the smallest tentative distance among all unvisited nodes. Any alternative path to `t` through another unvisited node $u$ would first have to reach $u$.

Because edge weights are positive:

$$
\texttt{dist[u]}+\text{positive edge cost}
>
\texttt{dist[u]}
\ge
\texttt{dist[t]}.
$$

So no path passing through an unsettled node can improve `dist[t]`. Marking it visited is safe.

Relaxing outgoing edges then exposes paths whose last newly settled intermediate node is `t`.

**Unreachable nodes do not break the loop**

If all remaining unvisited nodes are unreachable, their distances are infinity. The selection scan still chooses one because `t` begins at `-1` and the first unvisited candidate replaces it.

Marking such a node and evaluating:

`infinity + g[t][j]`

produces infinity, so no distance is improved. Repeating this for the remaining unreachable nodes is unnecessary work but safe.

After $n$ rounds, every node is marked visited and every reachable shortest distance is final.

**Return the requested destination**

If `dist[node2]` remains infinity, no directed path from source to destination exists, and the method returns `-1`.

Otherwise it returns the minimum accumulated cost.

When source and destination are the same node, initial distance zero is already the empty path cost. Positive cycles cannot lower it, so the method returns zero even though the diagonal matrix cell remains infinity.

**Trace the graph update**

Initially, edges $0\to1$ with cost two and $1\to2$ with cost one give path $0\to1\to2$ cost three, better than direct $0\to2$ cost five.

A query from zero settles zero, relaxes one to two and two to five, then settles one and improves two to three.

If node three is initially unreachable from zero, its distance remains infinity and the query returns `-1`.

After adding $1\to3$ with cost four, the next query recomputes from the current matrix and discovers path $0\to1\to3$ with cost six.


After each selection round:

- every visited node has its true shortest distance from `node1`;
- every unvisited `dist[v]` is the cheapest discovered path whose internal nodes are visited.

The positive-weight minimum-selection argument proves the newly selected node's tentative value is final. Relaxing every matrix entry from it updates all paths that use it as the last new internal node.

By induction, the invariant holds through all nodes. Hence the destination's finite distance is shortest, while infinity means no path exists.

**Exact implementation versus manifest summary**

The manifest mentions adjacency lists and heap-based Dijkstra with $O((n+e)\log n)$ query time. The exact source instead stores an adjacency matrix, chooses the next node by a linear scan, and scans all possible outgoing destinations.

The correct bound for this stored implementation is $O(n^2)$ per query, with $O(n^2)$ persistent matrix space. This explanation intentionally follows the executable code.

## Complexity detail

Construction allocates and initializes $n^2$ matrix cells, then writes $e$ input edges, costing $O(n^2+e)$ time and $O(n^2)$ space.

`addEdge` costs $O(1)$ time and no asymptotically new space.

One `shortestPath` call performs $n$ rounds. Each round scans $n$ nodes for selection and $n$ matrix entries for relaxation, so query time is $O(n^2)$. Its temporary `dist` and `vis` arrays use $O(n)$ space beyond the persistent matrix.

## Alternatives and edge cases

- **Heap-based adjacency-list Dijkstra:** Gives $O((n+e)\log n)$ per query and $O(n+e)$ storage, matching the manifest and helping sparse graphs.
- **Floyd–Warshall:** Precompute all-pairs paths in $O(n^3)$, then answer queries in $O(1)$, but dynamic edge updates need additional work.
- **Incremental all-pairs update:** A new edge can update every source-destination pair in $O(n^2)$ using existing all-pairs distances.
- **Directed edge:** Adding $f\to t$ must not create $t\to f$.
- **No path:** Infinity survives and becomes `-1`.
- **Source equals destination:** The empty path has cost zero.
- **Unreachable selection:** Infinity arithmetic leaves all distances unchanged.
- **Positive weights:** They are essential to Dijkstra's finalization proof.
- **Added edge:** Every later query sees it directly in the matrix.
- **No early destination exit:** The exact loop runs all $n$ rounds even after the target could be finalized.
