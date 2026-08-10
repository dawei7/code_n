## General

Each query asks about one unique tree path. Once its number of edges `d` is known, the weight-assignment count is purely mathematical:

- if `d = 0`, the path cost is zero and no odd assignment exists;
- if `d > 0`, exactly half of the `2^d` assignments have odd cost, giving `2^{d-1}`.

The challenge is answering path lengths quickly for up to `10^5` queries. The source roots the tree, records every node’s depth, and builds a binary-lifting table for lowest common ancestors. A lowest common ancestor converts two root depths into their path distance.

**Converting labels to array indices**

Input nodes are labeled `1` through `n`, but the source stores them at indices `0` through `n - 1`. It subtracts one from every edge endpoint and every query endpoint.

This representation permits arrays of exactly `n` entries. Root label `1` becomes index zero. The conversion is applied consistently before adjacency, depth, and ancestor access.

**Rooting the undirected tree iteratively**

Each edge is added in both directions to `adjacency`. The stack begins with `(0, -1)`, meaning root zero has no real parent.

When `(node, parent)` is popped, every neighbor other than `parent` is a child. The code sets:

- `depth[neighbor] = depth[node] + 1`;
- `ancestor[0][neighbor] = node`;
- a stack entry carrying `node` as that child’s parent.

Because the graph is a valid tree, there is one route from the root to each node. Skipping the immediate parent prevents the only possible revisit. The iterative stack also remains safe for a chain of `10^5` nodes, unlike a recursive traversal using Python’s default recursion limit.

The root’s immediate ancestor remains zero because the ancestor table was initialized with zeros. Climbing above the root therefore stays at the root, which makes later table lookups safe.

**Building powers-of-two ancestors**

`ancestor[level][node]` represents the ancestor `2^{level}` edges above `node`.

Level zero contains immediate parents. If `previous` is level `p - 1`, then going upward `2^p` edges means making two `2^{p-1}` jumps:

`previous[previous[node]]`.

`level_count = node_count.bit_length()` supplies enough levels to cover every possible depth in an `n`-node tree. Building all levels once lets each query climb many edges using only `O(\log n)` table accesses.

**Finding the LCA inside each query**

The source first saves

`original_depth_sum = depth[first] + depth[second]`.

This must be saved before the node variables are moved upward, because the final distance formula needs the original endpoints’ depths.

It then ensures `first` is the deeper or equally deep node. Their depth difference is decomposed into binary. For every set bit `level`, `first` jumps to `ancestor[level][first]`. After these jumps, the endpoints stand at equal depth.

If they are equal, that node is already the lowest common ancestor. Otherwise, the code considers levels from largest to smallest. Whenever the two `2^{level}` ancestors differ, both nodes jump upward. Such a jump keeps them below their LCA; if the proposed ancestors were equal, jumping there could move to or above the LCA and lose the lowest location.

After all levels, the two nodes are distinct children of the same parent. The assignment

`first = ancestor[0][first]`

makes `first` the LCA. `second` no longer matters for the distance calculation.

**Deriving path length from root depths**

Let `l` be the LCA of original endpoints `u` and `v`. The path from `u` to `v` goes upward from `u` to `l` and downward from `l` to `v`. Its edge count is

$$
(\operatorname{depth}[u] - \operatorname{depth}[l])
+ (\operatorname{depth}[v] - \operatorname{depth}[l])
= \operatorname{depth}[u] + \operatorname{depth}[v]
- 2\operatorname{depth}[l].
$$

The source evaluates this as

`distance = original_depth_sum - 2 * depth[first]`,

where `first` now stores the LCA.

**Why half of all assignments are odd**

Along a path of positive length `d`, each edge independently gets weight `1` or `2`. A weight of `1` flips sum parity; a weight of `2` does not. Fix any one path edge and pair assignments that differ only on that edge. Toggling between `1` and `2` flips the total parity, so this pairing matches every even assignment with one odd assignment.

There are `2^d` total assignments, hence `2^{d-1}` odd ones. The three-argument call

`pow(2, distance - 1, MODULUS)`

computes that count modulo `10^9 + 7` efficiently.

For a same-node query, `distance = 0`. There are no path edges, the only empty assignment has cost zero, and zero valid odd-cost assignments exist. The explicit conditional returns `0` and avoids the invalid negative exponent `distance - 1`.

## Complexity detail

Let `n` be the number of nodes and `q` the number of queries. Adjacency construction and iterative tree traversal take `O(n)` time. The ancestor table has `O(\log n)` levels with `n` entries each, so preprocessing takes `O(n \log n)` time.

For one query, depth equalization and simultaneous lifting each inspect `O(\log n)` levels. Modular exponentiation also takes `O(\log d) \subseteq O(\log n)` time. Thus all queries take `O(q \log n)`, and total time is

$$
O(n\log n + q\log n)
= O((n+q)\log n).
$$

The adjacency and depth arrays use `O(n)` space. The binary-lifting table dominates with `O(n \log n)` entries. The iterative traversal stack can hold `O(n)` nodes, and the returned answers use `O(q)` output space. Auxiliary preprocessing space is `O(n \log n)`, or `O(n \log n + q)` including output.

## Alternatives and edge cases

- **DFS per query:** Traversing the tree anew to find each path would cost `O(nq)` in the worst case and cannot handle both limits at `10^5`.
- **Euler tour and RMQ:** An Euler tour can turn LCA into a range-minimum query, potentially providing constant-time LCAs after suitable preprocessing. Binary lifting is easier to implement and its logarithmic query time already satisfies the constraints.
- **Precompute powers of two:** Since every distance is at most `n - 1`, an array of `2^{d-1} mod M` could make the final parity lookup constant-time. The exact source instead calls modular `pow` per query, which remains within the stated `O(q\log n)` bound.
- **Breadth-first depth preprocessing:** BFS can replace the iterative DFS stack and produces the same depths and parents because the input is a tree.
- **Same endpoint twice:** The zero-edge path has cost zero and returns zero; this is why the explicit `distance == 0` branch is necessary.
- **Adjacent endpoints:** Distance one yields `2^0 = 1`; only assigning weight one produces an odd cost.
- **One endpoint is an ancestor:** After depth equalization the nodes become equal, and that node is correctly used as the LCA without the simultaneous-lifting phase.
- **Endpoints in different root branches:** Simultaneous lifting finds their branch point, possibly the root.
- **Root queries:** Root index zero has depth zero and is its own ancestor at every table level, so all formulas remain valid.
- **Maximum-depth chain:** The iterative preprocessing handles it without recursion failure; ancestor storage and query time remain within their asymptotic bounds.
- **Edges outside the queried path:** They contribute no assignment choices and must not multiply the answer.
- **Modulo:** Every answer is reduced independently through modular exponentiation, as required.
- **Tree requirement:** The unique path and parent-only traversal logic rely on a connected acyclic input. They do not extend unchanged to a general graph.
