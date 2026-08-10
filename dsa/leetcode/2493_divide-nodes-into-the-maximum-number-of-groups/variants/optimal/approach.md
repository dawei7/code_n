## General

**Group numbers behave like BFS levels**

For every edge, endpoint group indices must differ by exactly one. If one node is placed in a group and graph distance is measured from it, assigning each node to one plus its shortest-path distance is a natural candidate: adjacent vertices have distances differing by at most one.

However, an edge whose endpoints have the same distance would violate the exact-difference rule. A graph permits this level assignment precisely when it is bipartite. An odd cycle forces some edge to connect equal-parity levels and makes every valid grouping impossible.

The exact solution combines bipartiteness checking and layer counting inside a breadth-first search started from every node.

**One BFS from source `i`**

Array `dist` begins with zeros, meaning unvisited. The source receives distance label one rather than zero, and `mx` also begins at one. These labels are directly the number of occupied BFS layers.

When BFS crosses from `a` to an unvisited neighbor `b`, it assigns

`dist[b] = dist[a]+1`,

updates `mx`, and enqueues `b`. Standard BFS guarantees this is one plus the shortest unweighted distance from source `i`.

For an already visited neighbor, the code requires

`abs(dist[b]-dist[a]) == 1`.

In an undirected graph, shortest-path distances of adjacent vertices can differ by at most one. Therefore, failure means they are equal. Such a same-level edge joins vertices of the same parity and exposes an odd cycle, so no valid grouping exists and the method returns `-1`.

Conversely, in a bipartite component every edge crosses between the two parity classes. BFS distances then have opposite parity at its endpoints; combined with the at-most-one property, their difference must be exactly one. The check accepts every edge.

**Why the maximum BFS layer count is the component answer**

For a fixed source, assigning nodes according to `dist` creates `mx` consecutive groups and satisfies every edge when the component is bipartite. Thus `mx` groups are achievable.

The farthest node from that source has shortest-path distance `mx-1`. Across every possible source, the greatest such distance is the component's diameter, the longest shortest-path distance between any two vertices. The code runs BFS from every node and takes the largest `mx`, so it obtains

$$
\text{diameter}+1
$$

groups for the component.

No valid grouping can use more. Along any edge, the group number changes by one. Choose nodes in the smallest and largest occupied groups of a connected component. Any graph path between them must make enough unit changes to cover that group-index difference, so their shortest-path distance is at least the difference. That difference cannot exceed the diameter. Therefore, the number of occupied consecutive groups is at most diameter plus one.

The BFS construction reaches this bound, proving maximality.

**Identify components without a separate component pass**

During each BFS, `root` is updated to the smallest numbered vertex encountered. Because BFS visits the entire connected component, every source in the same component finishes with the same minimum vertex as its `root`.

Dictionary `d` uses that minimum vertex as a component key. Assignment

`d[root] = max(d[root],mx)`

retains the greatest layer count found among all BFS sources in the component. This is how the all-source searches are consolidated instead of summed repeatedly.

For an isolated vertex, BFS visits only itself, `root` is that vertex, and `mx=1`. It correctly contributes one group.

**Why disconnected component answers add**

There are no edges between distinct components, so their group placements impose no constraints on each other. Place the optimal groups of the first component in one consecutive block, the next component's groups in a following block, and so on. All groups are non-empty, and every edge remains inside a component where adjacent labels differ by one.

Consequently, `sum(d.values())` is achievable. Each component independently cannot exceed its stored diameter-plus-one bound, so the sum is also globally maximal.

**Index conversion**

Input nodes are labeled from 1 to `n`, while adjacency list indices run from 0 to `n-1`. Both endpoints are reduced by one during graph construction. All later BFS state consistently uses zero-based indices.

## Complexity detail

Let $m$ be the number of edges. Building `g` takes $O(n+m)$ space and time. A BFS from one source allocates an $O(n)$ distance array and, in the worst case, scans its component's vertices and edges in $O(n+m)$ time. Repeating for all $n$ sources gives $O(n(n+m))$ worst-case time.

Only one `dist` array and queue exist at a time. Along with the adjacency list and dictionary, peak auxiliary space is $O(n+m)$.

The constraint $n\le500$ makes the deliberate all-source BFS feasible and allows exact diameter discovery without a more specialized method.

## Alternatives and edge cases

- **Separate coloring pass:** First test bipartiteness per component, then BFS from every component node for diameter. It is conceptually separated but has the same asymptotic cost.
- **Union-find for component keys:** It can replace the minimum-vertex `root` technique but does not test bipartiteness or compute diameters by itself.
- **Odd cycle:** Some BFS encounters an already visited same-level neighbor and returns `-1`.
- **Even cycle:** Alternating BFS layers satisfy every edge, so it is valid.
- **Disconnected graph:** Store one maximum layer count per component and add them.
- **Isolated node:** It forms a valid one-group component.
- **One BFS per component is insufficient:** An arbitrary source may not be a diameter endpoint and may yield too few layers.
- **Labels start at one:** Zero remains available as the unvisited sentinel in `dist`.
- **Common component key:** Taking the minimum visited index makes all sources in a component update the same dictionary entry.
- **Parallel or self edges:** The contract excludes them, simplifying adjacency behavior.
