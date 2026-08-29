## General

**The answer is the projection of one node onto a tree path**

For a query `(start, end, node)`, the simple path from `start` to `end` is unique because the graph is a tree. The closest path vertex to `node` is the junction where the three pairwise paths among `start`, `end`, and `node` meet. This junction is often called the median of the three tree vertices.

The solution finds that median using lowest common ancestors under an arbitrary root. For three vertices `a`, `b`, and `c`, their median is the deepest of

`lca(a, b)`, `lca(a, c)`, and `lca(b, c)`.

With `a = start`, `b = end`, and `c = node`, that median is exactly the closest point on the requested path.

**Build an undirected adjacency list**

`graph` contains one list per node. Every edge `[first, second]` is inserted in both directions because tree movement is bidirectional.

There are `n - 1` edges, so the complete adjacency representation has `2(n - 1)` neighbor entries. The later traversal chooses node zero as a root only for ancestry calculations; it does not change paths or distances in the original unrooted tree.

**Compute depth and immediate parents iteratively**

`stack = [(0, -1)]` starts a depth-first traversal at root zero. Each stack entry contains a node and the parent from which it was reached.

When popped, the code stores the immediate parent in `parent[0][node]`. The root is assigned itself rather than minus one, so taking ancestors above the root remains safely at zero.

For every neighbor other than `previous`, the algorithm sets its depth to one more than the current depth and pushes it with the current node as parent. A separate visited set is unnecessary because the graph is guaranteed to be a tree: the only already visited neighbor of a newly reached node is its parent.

At completion, `depth[v]` is the number of edges from root zero to `v`, and `parent[0][v]` is its one-step ancestor.

**Build binary-lifting ancestors**

`levels = n.bit_length()` provides enough powers of two to jump across any possible tree depth. Row `level` of `parent` stores the ancestor `2^{level}` edges above each node.

The recurrence

`parent[level][node] = parent[level - 1][parent[level - 1][node]]`

takes two jumps of `2^{level-1}` edges to form one jump of `2^{level}`. The root's self-parent convention makes every oversized jump remain at the root.

This table turns an ancestor climb of up to `n - 1` edges into at most `O(\log n)` jumps.

**Lift two nodes to equal depth**

To find `lca(first, second)`, the deeper node must first be brought to the shallower node's depth. If necessary, the function swaps them so `first` is deeper.

Let `difference = depth[first] - depth[second]`. Each one bit at position `level` in that difference represents a needed upward jump of `2^{level}`. The test `difference >> level & 1` detects that bit, and the corresponding ancestor-table lookup performs the jump.

After processing all levels, both nodes have equal depth. If they are now equal, that node is already the LCA.

**Lift both nodes just below their LCA**

If the equal-depth nodes differ, the function scans lifting levels from largest to smallest. Whenever their `2^{level}` ancestors differ, both nodes jump upward by that amount.

Skipping a jump when the ancestors are equal prevents moving to or above the LCA too early. After all levels, `first` and `second` are distinct children below their common ancestor. Returning `parent[0][first]` gives the LCA.

This standard descending-jump argument works because every too-large differing jump is taken, progressively closing the remaining distance while preserving that the true LCA is above both nodes.

**Why three LCAs reveal the tree median**

Consider the minimal connected subtree joining `start`, `end`, and `node`. It has one junction where the three routes meet; the junction may equal one of the three queried vertices.

Under any chosen root, two of the pairwise LCAs coincide at or above this junction, while the deepest of the three pairwise LCAs is the junction itself. Intuitively, the pair whose paths stay together farthest from the root exposes the lowest meeting point. This structural fact is independent of choosing node zero as root.

The candidate tuple contains exactly these three LCAs, and

`max(candidates, key=depth.__getitem__)`

selects the candidate with greatest root depth. If duplicate candidates tie, returning the first duplicate has no effect because they name the same node; the tree-median structure prevents two different deepest answers.

**Why the median is closest to** `node`

The median lies on the path from `start` to `end` and also on the route from `node` into that path. For any other path vertex `x`, the unique route from `node` to `x` first reaches the median and then travels along the `start`-to-`end` path. Hence

$$
\operatorname{dist}(\texttt{node},x)
=
\operatorname{dist}(\texttt{node},\text{median})
+
\operatorname{dist}(\text{median},x).
$$

The second term is nonnegative and is zero only at the median. Therefore, no other path node is closer.

**Trace special query shapes**

If `node` already lies on the path from `start` to `end`, the median is `node` and the answer has distance zero. If `start == end`, the path contains only that one vertex; `lca(start, end)` equals it and is at least as deep as the other relevant ancestors, so it is selected.

If `node` lies in a branch attached to the path, the median is the branch's attachment point. This is exactly the intuitive nearest path vertex.

**Answer all queries after one preprocessing pass**

The graph, depths, and ancestor table depend only on the fixed tree. They are built once. Each query performs three LCA computations and one constant-size depth comparison, then appends its median to `answer`.

This separation is what improves on running a new path search and distance search for every query.

## Complexity detail

Let `n` be the number of nodes and `m` the number of queries. Building the adjacency list and traversing the tree take `O(n)` time. Constructing `n` entries at each of `O(\log n)` ancestor levels takes `O(n \log n)`.

Each LCA call takes `O(\log n)` time. Three calls per query remain `O(\log n)`, so all queries take `O(m \log n)`. Total time is `O((n+m)\log n)`.

The adjacency list uses `O(n)` space, the parent table uses `O(n \log n)`, and depth, stack, and output use `O(n+m)`. Excluding the required output, the dominant auxiliary bound is `O(n \log n)`. The iterative traversal avoids a recursion stack.

## Alternatives and edge cases

- **BFS from the query node:** Compute distances and inspect the start-end path per query. It is simple but costs `O(n)` per query.
- **Find each path explicitly:** Parent searches can recover a path, but repeating them for up to 1,000 queries wastes the fixed-tree structure.
- **All-pairs distances:** It gives constant-time distance comparisons but uses `O(n^2)` time and space.
- **Heavy-light decomposition:** It can support richer path operations, but binary lifting and the tree-median identity are simpler for this static query.
- **Start equals end:** The only path node is returned.
- **Query node lies on the path:** It is the median and has distance zero.
- **Query node equals an endpoint:** That endpoint is the closest node.
- **Single-node tree:** The graph has no edges, all LCAs are node zero, and every valid query returns zero.
- **Arbitrary root choice:** Root zero affects LCA representation and depths but not the unrooted median selected by the three-LCA theorem.
- **Root parent:** Assigning the root as its own ancestor keeps binary jumps inside valid indices.
- **No visited set:** Parent exclusion is sufficient only because the graph is guaranteed to be a tree.
- **Depth alignment:** The deeper LCA argument requires lifting the first node to equal depth before paired jumps.
- **Descending lift order:** Large-to-small levels ensure both nodes finish immediately below their LCA.
- **Candidate ties:** Pairwise LCAs may repeat; `max` returning the first equal node is harmless.
- **Input preservation:** Edges and queries are read into derived structures and never modified.
