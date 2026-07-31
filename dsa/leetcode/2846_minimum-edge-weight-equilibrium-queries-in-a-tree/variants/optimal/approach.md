## General

**Reduce a query to a frequency maximum.** On a path containing $L$ edges, suppose weight $w$ occurs $f_w$ times. If every edge is changed to weight $w$, exactly $L-f_w$ operations are necessary. Choosing the most frequent path weight is therefore optimal, and the answer is

$$
L-\max_{1\le w\le26} f_w.
$$

The remaining task is to obtain the path length and all 26 frequencies without walking the path separately for every query.

**Root-prefix frequencies.** Root the tree at node `0`. For every node `v`, store `prefix_counts[v][w]`, the number of weight-$w$ edges from the root to `v`. An iterative depth-first traversal copies the parent's 26 counters, increments the incoming edge's counter, and records the node's depth.

Let `c` be the lowest common ancestor of query endpoints `a` and `b`. The two root paths share exactly the root-to-`c` prefix, so weight $w$ occurs on the queried path

$$
f_w=\texttt{prefix\_counts[a][w]}+\texttt{prefix\_counts[b][w]}-2\,\texttt{prefix\_counts[c][w]}.
$$

Similarly, the number of path edges is `depth[a] + depth[b] - 2 * depth[c]`. Scanning the fixed 26-weight alphabet then gives the maximum $f_w$ and the minimum operation count.

**Binary-lifting LCA.** Precompute `ancestors[v][j]`, the $2^j$th ancestor of every node. To answer a query, first lift the deeper endpoint until both depths match. If the nodes differ, lift both from the largest power of two downward whenever their candidate ancestors differ. Their parents are then the LCA. These jumps preserve the invariant that the LCA remains above both current nodes, so the returned parent is exactly their deepest shared ancestor. Combined with the prefix identity above, this accounts for every queried edge once and proves each reported minimum.

## Complexity detail

Let $m$ be the number of queries and let $W=26$ be the fixed number of possible weights. Building adjacency lists and root-prefix counts takes $O(nW)$ time. Constructing the ancestor table takes $O(n\log n)$ time. Each query takes $O(\log n+W)$ time for its LCA and frequency scan. Since $W$ is constant, total time is $O((n+m)\log n)$.

The ancestor table uses $O(n\log n)$ space. Adjacency, depths, traversal state, and the $n\times W$ prefix table use $O(nW)$ additional space, so total auxiliary space is $O(n\log n)$.

## Alternatives and edge cases

- **Walk the path for every query:** A DFS or BFS can recover each path and count its weights directly, but a long path costs $O(n)$ per query and produces $O(nm)$ worst-case time.
- **Tarjan offline LCA:** All LCAs can be found with disjoint-set union during a DFS. This achieves strong asymptotic performance but is more intricate because the path-frequency answers must be coordinated with offline query processing.
- **Euler tour with range-query LCA:** An Euler tour plus RMQ can answer LCAs quickly, while the same root-prefix counts provide weights. It requires a different preprocessing structure and does not simplify the fixed-alphabet calculation.
- **Equal endpoints:** When `a == b`, the path has no edges; every frequency and the path length are zero, so the answer is `0`.
- **Already uniform paths:** If one frequency equals the path length, no operation is needed.
- **Independent queries:** The method never mutates an edge. It evaluates every query against the original prefix data, exactly matching the reset-between-queries rule.
