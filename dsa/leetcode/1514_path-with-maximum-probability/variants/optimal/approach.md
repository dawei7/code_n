## General
**Reverse Dijkstra's ordering objective**

Ordinary Dijkstra finalizes the smallest additive distance. Here every edge probability lies in $[0,1]$, so extending a path can never increase its product. This gives an analogous greedy property: process the unfinished path with the largest current probability first.

Build an undirected adjacency list and store `best[v]`, the greatest probability discovered so far for reaching node `v`. Initialize the start to 1, representing the empty product, and every other node to zero. A max-heap is simulated with negative probabilities.

When a path to `node` is removed from the heap, multiply its probability by each incident edge probability. If that candidate improves the neighbor's best known product, record it and push a new heap entry. Ignore stale entries whose probability is below the current `best` value.

**Why the first destination pop is optimal**

Suppose the heap removes node $v$ with probability $p$. Any not-yet-processed path prefix has probability at most $p$. Extending such a prefix multiplies it by values no greater than 1, so it can never later produce a path to $v$ greater than $p$. Therefore $p$ is final when popped from a non-stale heap entry.

The same reasoning applies to the destination: the first non-stale destination entry is the globally maximum path probability and may be returned immediately. If the heap empties first, no sequence of graph edges reaches the destination, so zero is correct.

## Complexity detail
Constructing the adjacency list takes $O(n+e)$ time. Each successful relaxation adds a heap entry; with the standard adjacency-list Dijkstra bound, heap processing and edge scans take $O((n+e)\log n)$ time.

The graph stores two adjacency entries per undirected edge, `best` stores one value per node, and the heap can retain $O(n+e)$ entries, giving $O(n+e)$ space.

## Alternatives and edge cases
- **Negative logarithms:** transform each positive probability $p$ into weight $-\log p$ and run ordinary shortest-path Dijkstra. This is mathematically equivalent but must treat zero-probability edges separately.
- **Bellman-Ford-style relaxation:** repeatedly relax every edge in both directions. It is correct and simple but can require $O(ne)$ time.
- **Depth-first path enumeration:** tries every simple path and becomes exponential on dense cyclic graphs.
- **Direct versus indirect path:** multiplying several larger edges may beat one lower-probability direct edge.
- **Disconnected destination:** return `0.0` when the heap cannot reach it.
- **Zero-probability edge:** it cannot improve a node whose best probability is already zero and cannot create a positive-probability route.
- **Probability-one edges:** cycles of probability 1 do not cause repeated improvements because relaxation is strict.
- **Stale heap entries:** skip an older lower-probability entry after a better route to the same node has been found.
- **Undirected edges:** add both adjacency directions; omitting one changes reachability.
- **Floating-point tolerance:** compare candidate products normally and rely on the stated output tolerance for representation error.
