## General
**Recognize the structure that a minimum solution must have.** Any valid selection induces a connected undirected graph. If that selection contains a cycle, removing its most expensive edge preserves connectivity and cannot increase the total cost. Therefore an optimal selection can be a spanning tree with exactly `n - 1` useful connections; the task is to construct a minimum spanning tree or determine that none exists.

**Take safe connections in ascending cost order.** Sort `connections` by cost. Maintain the current connected components with a disjoint-set union structure. For each `[city_a, city_b, cost]`, find the representative of each endpoint. If the representatives match, the connection would create a cycle and can be skipped. Otherwise add `cost` to `total`, merge the two components, and increment `used`.

The greedy choice is safe: immediately before a chosen connection joins two components, those components define a cut of the graph, and this is a minimum-cost still-available connection crossing that cut. The cut property guarantees that some minimum spanning tree contains that choice. Repeating the argument constructs a minimum spanning tree whenever one exists. Path compression and union by size keep component operations efficient.

**Detect an impossible network.** A successful spanning tree uses exactly `n - 1` merging connections. If processing all entries leaves `used < n - 1`, at least two components have no available connection between them, so return `-1`. For `n = 1`, zero connections are needed and the minimum cost is `0`.

## Complexity detail
Sorting the $m$ connections costs $O(m\log m)$. The disjoint-set operations contribute $O(m\alpha(n))$, where $\alpha$ is the inverse Ackermann function, and are dominated by sorting. The parent and size arrays use $O(n)$ auxiliary space; sorting storage is implementation-dependent and is not larger than $O(m)$ when the input is copied.

## Alternatives and edge cases
- **Prim's algorithm:** Grow a tree from one city with an adjacency list and a min-heap in $O(m\log n)$ time and $O(n+m)$ space; it is equally valid but stores every connection in adjacency form.
- **Repeated component relabeling:** Kruskal can label every city by component and scan all labels after each merge, but this degrades to $O(m\log m+n^2)$ time.
- **Disconnected graph:** Fewer than `n - 1` successful merges means no selection can connect every city, even if every listed connection is considered.
- **Zero-cost connections:** Cost `0` is valid and should be selected whenever it safely joins two components.
- **Redundant or parallel connections:** A connection whose endpoints are already joined is skipped; among parallel choices, ascending processing naturally considers the cheapest first.
- **Single city:** No connection is required, so the correct minimum total is `0`.
