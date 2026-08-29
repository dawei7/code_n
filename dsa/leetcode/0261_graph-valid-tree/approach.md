## General

An undirected graph is a tree exactly when it is both connected and acyclic. The exact solution checks these two requirements while processing edges with a disjoint-set union structure, also called union-find.

Initially, every node is its own connected component. The parent array

```text
p = [0, 1, 2, ..., n - 1]
```

represents those singleton sets. A root is a node satisfying `p[x] == x`. Two nodes are connected by previously processed edges exactly when their roots are equal.

The source also reuses the variable `n` as the current number of connected components. It starts at the original node count and decreases by one after every successful merge. This repurposing is safe because the parent array has already been constructed with the original size and later code needs only the component count.

**Find the representative with path compression**

`find(x)` follows parent links until it reaches a root. On the recursive return path, it assigns

```text
p[x] = find(p[x])
```

so every visited node points directly to the representative. This is path compression. It preserves component membership while making future searches from those nodes shorter.

For example, if parent links are `0 -> 1 -> 3 -> 3`, calling `find(0)` returns `3` and changes the path so `0` and `1` both point directly to `3`.

**What one edge means**

For an undirected edge `[a, b]`, the algorithm computes `pa = find(a)` and `pb = find(b)`.

- If `pa != pb`, the endpoints were in different components. The edge connects those components, so setting `p[pa] = pb` merges them and reduces the component count by one.
- If `pa == pb`, there was already a path between `a` and `b`. Adding this edge creates a second route between the endpoints and therefore a cycle. A tree cannot contain a cycle, so the method returns `False` immediately.

It is important that the parent assignment links roots rather than arbitrary endpoint nodes. Joining `pa` to `pb` combines whole component trees while keeping the union-find representation valid.

**Why one component at the end is required**

Processing all edges without finding a cycle proves the graph is a forest: every connected component is a tree, but there may be several disconnected trees. Returning `n == 1` checks that exactly one component remains.

This catches an input such as four nodes with only edges `[0,1]` and `[2,3]`. Both unions succeed and no cycle exists, but the component count falls only from four to two. The graph is a forest, not one tree, so the result is `False`.

**Why an explicit edge-count check is unnecessary here**

Many tree validators begin by requiring exactly $N-1$ edges. The source does not perform that check directly. It gets the same conclusion from successful union counts.

Starting from $N$ components, reaching one component requires exactly $N-1$ successful merges. If there are fewer useful edges, more than one component remains. If an extra edge appears after its endpoints are already connected, the equal-root test detects a cycle. Thus “no failed union and one final component” implies exactly the structure of a tree without separately checking `len(edges)`.

**Trace of a valid tree**

For `n = 5` and edges `[[0,1],[0,2],[0,3],[1,4]]`:

1. All five nodes begin separate.
2. Edge `[0,1]` merges two roots; four components remain.
3. Edge `[0,2]` connects node `2` to the component containing `0`; three remain.
4. Edge `[0,3]` performs another merge; two remain.
5. Edge `[1,4]` finds that `1` belongs to the large component while `4` is separate, so it merges them; one remains.

No edge connected nodes already in the same component, and the final component count is one. The result is `True`.

For the cyclic example `[[0,1],[1,2],[2,3],[1,3],[1,4]]`, the first three edges connect nodes `0` through `3`. When `[1,3]` is processed, both endpoints already have the same representative. That edge closes a cycle, so the function rejects before later connectivity can matter.

**Why the two checks prove the result**

Every successful union corresponds to adding an edge between distinct components, which cannot create a cycle. Therefore, if processing completes, all accepted edges form an acyclic graph. If the final count is one, all nodes are connected. A connected acyclic undirected graph is exactly a tree.

Conversely, in a genuine tree, the endpoints of each edge cannot already be connected by previously processed tree edges; otherwise that prior path plus the edge would be a cycle. Every union succeeds, and the connected tree ultimately has one component. The algorithm returns `True` for every valid tree and `False` for every cyclic or disconnected graph.

## Complexity detail

Let $N$ be the original number of nodes and $E$ the number of edges. Initializing `p` takes $O(N)$ time and space. Each edge performs two `find` operations and at most one constant-time link.

The exact source uses path compression but does **not** use union by size or union by rank: it always assigns `p[pa] = pb`. With both balancing and compression, the classic bound would be $O((N+E)\alpha(N))$, effectively linear. With path compression alone, a standard amortized upper bound is $O((N+E)\log N)$, and an individual recursive `find` can encounter a chain of length $O(N)$ before compressing it. In practice the compression still makes repeated operations fast.

This differs from the manifest summary, which claims union by size and an $O(N+E)$ bound. Those properties are not present in the protected solution and should not be attributed to it.

The parent array uses $O(N)$ persistent space. Recursive `find` can also use $O(N)$ call-stack space in the worst unbalanced parent chain, though paths are shortened afterward. Overall auxiliary space remains $O(N)$.

## Alternatives and edge cases

- **Union by size plus path compression:** Track each root's component size and attach the smaller tree below the larger. This supplies the near-linear inverse-Ackermann guarantee described by the editorial and manifest.
- **Edge count plus DFS or BFS:** Require `E == N - 1`, build an adjacency list, and verify all nodes are reachable. It runs in $O(N+E)$ time but stores both directions of every edge.
- **Cycle-aware graph traversal:** DFS can track each node's parent and reject an already visited non-parent neighbor, then separately test connectivity. It is correct but has more undirected-edge bookkeeping than union-find.
- **One node and no edges:** The parent array contains one root, no union fails, and the component count is already one, so the graph is correctly a tree.
- **Disconnected acyclic graph:** No union detects a cycle, but more than one component remains and the final check rejects it.
- **Connected graph with an extra edge:** Once a spanning structure has connected the endpoints, the extra edge finds equal roots and is rejected as a cycle.
- **Self-loop:** The stated input excludes it. If present, both endpoints immediately have the same root, so the source would correctly reject it.
- **Repeated edge:** Also excluded by the contract. Its second occurrence would join already connected endpoints and be rejected.
- **Edge order:** Union-find correctness does not depend on order. Different orders may produce different parent-tree shapes but the same cycle/connectivity verdict.
- **Repurposed `n`:** After `p` is created, `n` means component count, not array length. Adding later code that treats it as the original node count would be an easy maintenance bug.
- **Recursive depth:** Because links are not balanced, an adversarial order can form a long parent chain. An iterative `find` or union-by-size policy avoids Python recursion-limit risk.
