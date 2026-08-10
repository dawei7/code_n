## General

For each query, three nodes matter: `src1`, `src2`, and `dest`. The selected edges must let both sources reach the destination. Because the original graph is a tree, there is exactly one simple path between any two nodes. Therefore the minimum valid subtree is not something we need to search for among many candidates: it is exactly the union of the paths connecting the three query nodes.

The implementation answers the weight of that union from three pairwise distances. To make those distances fast across as many as `10^5` queries, it preprocesses depths, root distances, and binary-lifting ancestors for lowest common ancestor queries.

**Why the required subtree is uniquely determined**

Any connected subgraph containing two tree nodes must include the unique path between them. Thus a subtree that lets `src1` reach `dest` must contain their path, and one that lets `src2` reach `dest` must contain their path. Their union is connected, contains all three terminals, and is itself a tree, so it is valid.

Removing any edge from this union would break at least one of those required paths. All edge weights are positive, so adding any edge outside the union can only increase the total weight. The union is consequently the unique minimum edge set for the query.

**The half-sum identity for three terminals**

Let the three query nodes be `a`, `b`, and `c`. Consider the minimal subtree connecting them. Every edge in this subtree separates the three terminals into a group of one on one side and a group of two on the other. Exactly two of the three terminal pairs have endpoints on opposite sides of that edge, so exactly two pairwise paths use it.

Therefore, when we add

$$
\operatorname{dist}(a,b)
+ \operatorname{dist}(a,c)
+ \operatorname{dist}(b,c),
$$

every selected edge weight is counted exactly twice. Dividing by two gives the total weight of the union:

$$
\operatorname{answer}
= \frac{
\operatorname{dist}(a,b)
+ \operatorname{dist}(a,c)
+ \operatorname{dist}(b,c)
}{2}.
$$

This is the formula implemented by `pairwise_sum // 2`. The numerator is always even as an integer-weight expression because every contributing edge appears twice; integer division therefore loses no information.

An equivalent picture is that the three pairwise paths meet at one branching node, sometimes called the median of the three terminals. If the three branch lengths from that meeting point are `x`, `y`, and `z`, the pairwise distances are `x + y`, `x + z`, and `y + z`. Their sum is `2(x + y + z)`, twice the desired subtree weight.

**Rooting the tree without recursion**

The undirected adjacency list `graph` stores both directions of every weighted edge. The code roots the tree at node `0` and uses `traversal = [0]` as a list-backed traversal queue. Python’s `for node in traversal` continues over elements appended during iteration, so every discovered child is eventually processed.

For each child, preprocessing records:

- `parent[child]`, its immediate parent toward root `0`;
- `depth[child]`, its number of edges below the root;
- `root_distance[child]`, the total edge weight from root `0` to that child.

The condition `neighbor == parent[node]` prevents walking directly back along the edge just used. Since the input is guaranteed to be a tree, there are no other cycles and no separate visited set is necessary.

This iterative traversal avoids recursion-depth problems on a chain of `10^5` nodes.

**Building binary-lifting ancestors**

`ancestors[0][v]` is the immediate parent of `v`. For each higher level `p`,

`ancestors[p][v]`

is the ancestor `2^p` edges above `v`. It is computed by going `2^{p-1}` steps twice:

`previous[previous[v]]`.

The number of levels is `node_count.bit_length()`, enough to represent every possible depth difference in binary. Root `0` has parent `0`, so climbing beyond the root safely remains at the root rather than leaving the array.

**Finding the lowest common ancestor**

To find the lowest common ancestor of `first` and `second`, the helper first ensures `first` is at least as deep. It writes their depth difference in binary and lifts `first` by the corresponding powers of two. The nodes are then at equal depth.

If they are already equal, that node is the answer. Otherwise the helper examines powers of two from largest to smallest. Whenever the two proposed ancestors differ, both nodes climb to those ancestors. This keeps them below their lowest common ancestor while making the largest safe jumps. At the end, the nodes are distinct children of the same parent, so `ancestors[0][first]` is their lowest common ancestor.

**Converting an LCA into a weighted distance**

If `l` is the lowest common ancestor of nodes `u` and `v`, the root-to-`u` path and root-to-`v` path share the entire root-to-`l` prefix. Hence

$$
\operatorname{dist}(u,v)
= \operatorname{rootDistance}[u]
+ \operatorname{rootDistance}[v]
- 2\operatorname{rootDistance}[l].
$$

The `distance` helper evaluates exactly this formula. Each query makes three distance calls and then applies the half-sum identity. Preprocessing is shared by every query, which is why the method remains efficient for a large query list.

## Complexity detail

Let `n` be the number of tree nodes and `q` the number of queries. Building the adjacency list and traversing the tree take `O(n)` time. The binary-lifting table has `O(\log n)` levels, and constructing each level visits all `n` nodes, for `O(n \log n)` preprocessing time.

One lowest common ancestor operation checks `O(\log n)` levels. A query performs three such operations, which is still `O(\log n)` per query because the factor three is constant. Total time is

$$
O(n \log n + q \log n)
= O((n+q)\log n).
$$

The adjacency list uses `O(n)` space for a tree, and the traversal, parent, depth, and root-distance arrays use `O(n)` more. The ancestor table dominates with `O(n \log n)` entries. The answer uses `O(q)` output space. Auxiliary preprocessing space is `O(n \log n)`, or `O(n \log n + q)` if the required returned array is included.

## Alternatives and edge cases

- **Per-query traversal:** Running a DFS or BFS to build the two required paths for every query is conceptually straightforward but costs `O(nq)` in the worst case, which is infeasible at the maximum constraints.
- **Euler tour plus range-minimum queries:** An Euler tour can reduce LCA to a range-minimum query. With a sparse table it offers constant-time LCAs after `O(n \log n)` preprocessing, while other RMQ structures offer different tradeoffs. Binary lifting is simpler and already meets the required bound.
- **Heavy-light decomposition:** HLD can answer weighted path queries and supports future edge updates, but this problem has static weights and needs only path sums, so root distances plus LCA are smaller and clearer.
- **Direct median-node formula:** One could identify the three-terminal meeting node from pairwise LCAs and sum distances to it. The half-sum formula avoids case distinctions and needs only ordinary pairwise distances.
- **A query node equal to the root:** Its root distance and ancestors are already defined correctly, so no special handling is necessary.
- **Ancestor relationships among query nodes:** If one terminal lies on the path between the other two, the minimal subtree is simply the outer pair’s path. The half-sum identity still counts every edge twice and returns that path’s weight.
- **Branching at one query node:** The same proof applies when the three-path meeting point equals `src1`, `src2`, or `dest`.
- **Pairwise distinct query nodes:** The source statement guarantees distinct terminals, although the formula would also work if two were equal.
- **Large accumulated weights:** A path may contain many edges of weight up to `10^4`. Python integers grow as needed, so `root_distance` and the pairwise sum do not overflow.
- **Tree guarantee:** Skipping only the immediate parent is safe because the graph is a valid tree. On a general undirected graph, this traversal would need a visited set and the unique-path/half-sum reasoning would no longer apply.
- **Positive edge weights:** Positivity guarantees that adding unused branches cannot improve a solution. The unique required-path union remains structurally necessary even with zero weights, but positive weights make minimality immediate.
