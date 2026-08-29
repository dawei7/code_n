## General

**Use the special structure of a tree**

In a general weighted graph, changing one edge might alter shortest paths in complicated ways. Here the graph is a tree rooted at node `1`. Between the root and any node `x` there is exactly one simple path. Since no alternative path exists, the shortest-path distance is simply the sum of edge weights on that unique root-to-`x` path.

Now orient every undirected edge away from the root. An edge between a parent `p` and child `c` lies on the root path of exactly the nodes in `c`'s subtree. If that edge weight changes by

`delta = new_weight - old_weight`,

then:

- every node in `c`'s subtree has its root distance changed by `delta`;
- every node outside that subtree is unaffected.

Thus an edge update is a subtree range addition, and a distance query asks for the accumulated additions at one node. The protected solution turns tree subtrees into contiguous numeric intervals with a depth-first Euler order, then uses a Fenwick tree for range-add and point-query operations.

**Build the undirected tree and preserve current edge weights**

`adjacency` stores both directions of each input edge as `(neighbor, weight)` pairs. The initial DFS needs those weights to compute original root distances.

The dictionary `weights` maps a normalized undirected key

`(min(u, v), max(u, v))`

to the edge's current weight. Query endpoints may be supplied in either orientation, so normalization guarantees that initialization and later updates refer to the same dictionary entry. After every update, the dictionary is replaced with the new weight, allowing the next delta to be measured against the current value rather than the original value.

**Root the tree and compute initial distances iteratively**

The source uses an explicit stack instead of recursive DFS. Each stack record is:

`(node, previous, distance, exiting)`.

When `exiting` is false, the record represents entry into a node:

- `parent[node] = previous` fixes the rooted orientation;
- `initial_distance[node] = distance` stores the sum of original edge weights from node `1`;
- `entry[node] = timer` gives the node its preorder position;
- `timer` increases by one.

The source then pushes an exit marker for the node and pushes its children. Children are pushed in reversed adjacency order because the stack is last-in, first-out; this preserves a natural traversal order, although correctness needs only a consistent DFS order.

When the exit marker is eventually popped, every descendant has already been entered and assigned a preorder number. The current `timer` is stored as `exit\_time[node]`.

Therefore, the subtree of each node `v` occupies the half-open interval

`[entry[v], exit_time[v])`.

Preorder gives this contiguity because DFS completely finishes one subtree before entering a node outside it. The interval includes `v` itself, and `exit_time[v]` is the first index after all of its descendants.

The initial distances never change after preprocessing. Later query answers add only the cumulative differences caused by updates.

**Represent subtree additions as a difference array**

Suppose an array indexed by Euler position stores the total distance correction for each node. Adding `delta` directly to every position of a subtree could take linear time. Instead, use a difference-array idea.

To add `delta` to every index in half-open range `[left, right)`:

- add `delta` at difference position `left`;
- add `-delta` at difference position `right`, if `right` is inside the array.

The prefix sum at any position then includes `delta` exactly inside the range. Multiple updates add together naturally.

The list `fenwick` stores this difference array in Fenwick-tree form. The nested `add(index, delta)` function performs a point addition to the difference array in `O(\log n)` time. It accepts a zero-based Euler index, converts it to the Fenwick tree's one-based convention, and updates all responsible tree cells.

The nested `point(index)` function returns the prefix sum of the difference array through a zero-based Euler index. Although named “point,” it is implemented as a Fenwick prefix query. In the range-add/point-query interpretation, that prefix sum is exactly the correction applying at that one point.

No initial root distances are loaded into the Fenwick tree. It starts with zeros because `initial_distance` already stores the complete baseline; `fenwick` needs to represent only later deltas.

**Process an edge update**

For a query `[1, left, right, new_weight]`, the normalized edge key locates the old current weight. The source computes `delta` and immediately records `new_weight` in `weights`.

It then determines which endpoint is the child in the rooted tree:

`child = left if parent[left] == right else right`.

Because the query is guaranteed to name a real tree edge, exactly one endpoint is the parent of the other. If `left`'s parent is `right`, `left` is the child; otherwise `right` is.

Every affected root path is precisely the child's subtree, so the code applies the difference range update:

`add(entry[child], delta)`

and, when the exclusive end is less than `n`:

`add(exit_time[child], -delta)`.

If the subtree extends through the final Euler position, its exclusive endpoint is `n`, outside the represented zero-based positions. There is no later position at which the correction must be canceled, so the second update is correctly omitted.

A repeated update to the same edge remains correct. Since `delta` compares the new weight with the most recently stored weight, accumulated Fenwick corrections telescope to current weight minus original weight.

**Answer a distance query**

For `[2, node]`, `point(entry[node])` sums every subtree-update delta whose Euler interval covers that node. An updated parent-child edge covers the node exactly when the edge lies on its root path. Thus this prefix query equals the total change across all updated edges on that path.

The answer is:

`initial_distance[node] + point(entry[node])`.

The first term accounts for every edge's original weight, and the second replaces those original contributions by their current values through accumulated differences.

For the root, `initial_distance[1] = 0`. No edge's child subtree contains the root, so its Fenwick correction is also zero; every root query correctly returns zero.

**Why the method stays correct after any query sequence**

The Euler preprocessing establishes a permanent subtree interval for every node because only weights change; the tree topology never changes. Each update adds exactly its weight difference to exactly the nodes whose unique root paths use that edge. Fenwick range additions are additive, so corrections from different edges and different update times combine without interference.

For any queried node, consider each edge on its unique root path. Its latest weight equals its initial weight plus the sum of deltas from updates to that edge. Every one of those deltas covers the node's Euler position. Edges not on the path have child subtrees that exclude the node, so their deltas do not appear. Therefore the returned baseline plus prefix correction is precisely the sum of current weights on the unique path.

## Complexity detail

Let `n` be the number of nodes and `q` the number of queries. Building adjacency and the weight dictionary takes `O(n)` time and space because a tree has `n - 1` edges. The iterative DFS enters and exits each node once and examines each undirected edge twice, so it takes `O(n)` time. Its parent, distance, entry, exit, and stack storage are all `O(n)`.

Each weight update performs at most two Fenwick additions, each `O(\log n)`. Edge lookup, delta computation, child selection, and interval lookup are `O(1)` expected time around those operations. Each distance query performs one Fenwick prefix query in `O(\log n)`. Processing all queries therefore costs `O(q \log n)` time.

The full time bound is `O(n + q \log n)`, which is contained in the manifest's `O((n + q)\log n)` bound and is slightly tighter for preprocessing.

The adjacency list, weight dictionary, preprocessing arrays, DFS stack, and Fenwick tree each use `O(n)` space. The returned answer list uses `O(r)` output space for `r` type-two queries; excluding required output, auxiliary space is `O(n)`.

Distances can reach roughly `(n - 1) \cdot 10^4`. Python integers cannot overflow. A fixed-width implementation should use at least 64-bit integers for stored distances and Fenwick deltas, especially across many updates.

## Alternatives and edge cases

- **Recompute DFS after every update:** This is straightforward but can cost `O(nq)` when many updates are followed by queries.
- **Update every descendant explicitly:** Euler order makes descendants contiguous, but writing all positions in the interval still costs subtree size. The Fenwick difference structure reduces it to two logarithmic updates.
- **Segment tree with lazy propagation:** It can also perform subtree range additions and point queries in `O(\log n)`. A Fenwick tree is smaller and simpler because only this exact range-add/point-query combination is needed.
- **Heavy-light decomposition:** HLD is useful for arbitrary path updates or queries. Rooted-edge updates here affect whole subtrees, so a single Euler interval is enough.
- **Recompute a queried path by walking parents:** This costs up to `O(n)` per query. Precomputed baseline distances plus accumulated subtree deltas avoid path traversal.
- **Treat the edge endpoints in query order as parent and child:** Updates are undirected and may name endpoints in either order. The `parent` array must determine the child.
- **Update the same edge repeatedly:** The dictionary must store the latest weight. Computing every delta from the original weight would double-count earlier changes.
- **Delta equals zero:** The two Fenwick additions change nothing. The source still processes them safely.
- **Weight decreases:** `delta` is negative, and range addition naturally lowers every affected distance.
- **Root query:** The root has distance zero and lies in no non-root child subtree, so it remains zero after all updates.
- **Leaf-edge update:** The child subtree interval has length one, so only that leaf's root distance changes.
- **Subtree reaches Euler index n:** `exit_time[child] == n` means no cancellation point exists inside the array. Omitting the second update is required, not an off-by-one error.
- **Single-node tree:** There are no edges. DFS assigns the root interval `[0,1)`, and all valid distance queries return zero.
- **Deep chain:** Recursive DFS could exceed Python's recursion limit at `10^5` nodes. The explicit stack avoids that failure.
- **Traversal order:** Reversing adjacency before stack pushes changes only the particular Euler numbering. Every DFS preorder still gives contiguous subtree intervals.
- **Tree guarantee:** The argument relies on one unique root path and fixed topology. In a general graph, an edge update would not correspond to one child subtree and shortest paths might reroute.
