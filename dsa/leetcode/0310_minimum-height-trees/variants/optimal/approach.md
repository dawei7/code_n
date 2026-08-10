## General

Choosing a root changes which paths point downward, but it does not change distances in the underlying undirected tree. The height obtained from root $r$ is the greatest distance from $r$ to any node. The desired roots are therefore the nodes whose maximum distance to the rest of the tree is as small as possible. These nodes are called the tree's centers.

A tree has either one center or two adjacent centers. The source finds them by repeatedly removing all current leaves, moving inward one distance layer at a time.

**Why leaves cannot be the best roots in a nontrivial tree**

A leaf has only one neighbor. If the tree has more than two nodes, moving the root from that leaf to its neighbor decreases the distance to every node reached through that neighbor—which is every other node in the tree—by one. The maximum distance cannot improve by staying at the outer leaf.

More generally, the nodes farthest from the center lie on the tree's periphery. Removing all peripheral leaves exposes the next inward layer without changing where the middle of the tree lies.

**Connection to a longest path**

A diameter is a longest simple path in the tree. If its length is $D$ edges, rooting at a node $r$ cannot make both diameter endpoints closer than the larger of their distances from $r$. Along the unique path between those endpoints, that larger distance is minimized at the middle.

- If $D$ is even, the diameter has one middle node.
- If $D$ is odd, it has two adjacent middle nodes.

Those middle nodes minimize the greatest distance to all nodes and are precisely the minimum-height roots.

When all current leaves are removed simultaneously, both ends of every longest surviving path move inward by one edge. The middle node or middle pair does not change. Repeating this symmetric trimming eventually leaves the diameter's middle as the final layer.

This explains both why leaf peeling works and why there can be no more than two answers.

**Building adjacency and degrees**

The source builds an adjacency list `g`. For every undirected edge `[a, b]`, it appends `b` to `g[a]` and `a` to `g[b]`.

The parallel array `degree` initially stores the number of neighbors of every node. In a tree with at least two nodes, a current leaf is exactly a node with degree one. The initial queue contains all such nodes.

The graph is guaranteed to be a tree, so it is connected and has $n-1$ edges. For $n\ge2$, at least two leaves exist, ensuring that the initial queue is nonempty.

**Processing one complete layer at a time**

At the start of every outer `while q` iteration, the queue contains exactly the leaves of the current unpeeled tree.

The source clears `ans`, then executes `for _ in range(len(q))`. Python evaluates `len(q)` when the range is created, so the loop processes only the nodes that were already in the current layer. Leaves appended during this loop wait for the next outer iteration.

For each removed leaf `a`, the source:

1. removes it from the left of the queue;
2. appends it to the current layer list `ans`;
3. decreases the degree of every neighbor `b` in `g[a]`;
4. enqueues `b` exactly when its degree becomes one.

Decreasing a neighbor's degree represents deleting the edge from the peeled leaf to that neighbor. When a surviving internal node has only one unpeeled connection left, it has become a leaf of the smaller tree and belongs in the next layer.

**Why `ans` is cleared each round**

This implementation does not stop as soon as at most two nodes remain. Instead, it peels those final center nodes too.

`ans.clear()` discards the previous outer layer just before the next layer is processed. After the final center layer is removed, no new degree-one node is created, so the queue becomes empty and the outer loop ends. Since there is no following round to clear `ans`, it still contains exactly that final nonempty layer.

Returning `ans` therefore returns one center or the adjacent pair of centers.

For a two-node tree, both nodes are initial leaves. They are processed in the only round, no later layer is enqueued, and `ans` correctly contains both nodes.

**Why scanning unchanged adjacency lists is safe**

The source does not physically delete neighbors from `g`; it only decreases degree counts. A node is enqueued when its degree becomes exactly one. After a leaf has been processed, later traversal from its former surviving neighbor may decrease that old leaf's degree from one to zero, but zero does not satisfy the enqueue condition.

Thus, processed nodes are not reintroduced. Every original adjacency entry is examined when its endpoint is eventually peeled, which remains linear total work. The degree values of already removed nodes no longer describe a live graph role, but only unprocessed nodes need meaningful positive degrees.

**Tracing the two-center example**

For `n = 6` and edges `[[3,0],[3,1],[3,2],[3,4],[5,4]]`, the initial degrees identify leaves 0, 1, 2, and 5.

During the first round:

- removing 0, 1, and 2 reduces node 3's degree from four to one, so node 3 enters the next queue;
- removing 5 reduces node 4's degree from two to one, so node 4 also enters the next queue.

At the beginning of the second round, `ans` is cleared. Nodes 3 and 4 are processed as the final layer. Their shared edge disappears, no new leaf remains, and the queue becomes empty. The returned list is `[3, 4]`.

Rooting at either center gives the same minimum height. Moving to any outer node places one diameter endpoint farther away and increases the maximum distance.

**Why the final layer is exact**

The initial queue is precisely the outermost distance layer. Assuming the queue at some round contains every leaf of the current tree, decrementing degrees for all of them removes that entire boundary. A surviving node is enqueued precisely when it has one surviving connection, so the next queue is exactly the next tree's leaf set. The layer invariant holds by induction.

Simultaneous leaf removal preserves the middle of every diameter while shortening it from both ends. The process cannot finish anywhere except its one or two middle nodes. Those nodes minimize maximum distance and hence rooted height. The final saved layer is therefore exactly the complete set of minimum-height roots.

## Complexity detail

The tree has $n$ nodes and $n-1$ edges. Building the two-sided adjacency list processes every edge once and stores two neighbor entries, costing $O(n)$ time and space. Computing initial leaves scans the $n$ degrees once.

Each node enters the queue at most once and is processed once. When a node is processed, the source scans its original adjacency list. Across all nodes, this visits exactly $2(n-1)$ adjacency entries. The trimming phase is therefore $O(n)$ time.

Total time complexity is $O(n)$. The adjacency list, degree array, queue, and final layer together use $O(n)$ space.

The queue can itself contain $O(n)$ nodes, as in a star where all outer nodes are initial leaves. `ans` can also temporarily hold that many labels during the first round, but both remain within the same linear bound.

## Alternatives and edge cases

- **Run BFS or DFS from every possible root:** Measuring every root's farthest distance is direct but costs $O(n^2)$ time on a tree, which is too slow for $n=2\cdot10^4$.
- **Find a diameter, then take its middle:** Run BFS or DFS from any node to find a farthest endpoint, run again from that endpoint while recording parents, and return the middle one or two nodes of the resulting diameter. This is also $O(n)$ time and $O(n)$ space.
- **Stop when at most two nodes remain:** Track a remaining-node count and halt before peeling the center layer. This is the common variant. The exact source instead processes all layers and preserves the last one in `ans`.
- **Process newly enqueued leaves immediately:** That would mix distance layers and could erase the intended final-layer distinction. Snapshotting `len(q)` keeps rounds simultaneous.
- **Use directed indegrees:** The input edges are undirected. Both adjacency directions and ordinary neighbor counts are required.
- **One node:** Its degree is zero, not one, so the normal queue would be empty. The explicit `n == 1` case correctly returns `[0]`.
- **Two nodes:** Both are leaves and both are valid minimum-height roots with height one.
- **Path with an odd number of nodes:** Repeated endpoint peeling leaves one middle node.
- **Path with an even number of nodes:** Peeling leaves two adjacent middle nodes.
- **Star:** All outer nodes are removed in the first round, leaving the central node as the sole answer.
- **Balanced tree:** Entire depth layers are peeled together until the central root or central edge remains.
- **Arbitrary labels:** Labels are exactly 0 through $n-1$, so they index `g` and `degree` directly.
- **Answer order:** The queue's discovery order determines output order, but any order is accepted.
- **Tree guarantee:** Connectivity and acyclicity are essential. A general graph may have no degree-one node or may leave a cyclic core, so this leaf-peeling proof would not apply.
- **No repeated edges:** Degree counts match actual distinct neighbors, and no duplicate adjacency entry can cause premature decrements.
