## General

**Root the underlying tree at the destination.** Ignoring road directions, the network is a tree. Root it at city zero. Every non-root city has exactly one parent: the next city on its unique undirected path toward zero.

For every city to reach zero, each edge must point from a child toward its parent. If an edge instead points from the parent out toward the child, it must be reversed. Because a tree has only one path to the root, there is no alternative route that could compensate for a wrongly directed parent-child edge.

The problem therefore becomes: traverse the tree outward from zero and count the edges whose original direction also points outward.

**Store both traversal directions with different costs.** The original connection `[a, b]` is a directed road from `a` to `b`. To traverse the entire underlying tree from root zero, the adjacency list needs entries in both directions.

The source adds `(b, 1)` to `g[a]`. If a traversal moves outward from `a` to `b` through this entry, it follows the original direction. In the rooted tree, that road points parent-to-child and must be reversed, so its cost is one.

It also adds `(a, 0)` to `g[b]`. Traversing from `b` to `a` through this artificial reverse entry means the original road actually points from child `a` toward parent `b`. It already leads toward zero and needs no reversal, so the cost is zero.

These costs do not represent travel distance. They encode whether choosing that adjacency entry as the rooted parent-to-child traversal reveals a road that faces the wrong way.

**Use the parent to avoid walking backward.** `dfs(a, fa)` explores city `a` while `fa` is its parent in the rooted traversal. Every underlying edge appears twice in `g`, so the condition `b != fa` skips the entry leading back to the caller.

A separate visited set is unnecessary because the undirected structure is a tree. Apart from the parent, every neighbor is an unvisited child. In a graph with cycles, parent-only skipping would not be sufficient, but the tree guarantee makes it exact.

**Add this edge's cost and the child's subtree cost.** For each child entry `(b, c)`, the expression contributes `c + dfs(b, a)`. The local cost says whether the edge from `a` to child `b` must be reversed. The recursive result counts all wrong-way edges strictly below `b`.

`sum(...)` combines the independent contributions from every child subtree. A leaf has no neighbor other than its parent, so its generator is empty and `sum` returns zero.

The initial call `dfs(0, -1)` uses a sentinel parent outside the city range. It lets every real neighbor of zero be processed.

**Trace one edge in each orientation.** Suppose connection `[0, 1]` exists. Root traversal moves from zero to child one using the cost-one entry, so the algorithm counts a reversal. Indeed, the road currently carries travelers away from the capital.

Suppose connection `[4, 0]` exists. Root traversal moves from zero to child four using the artificial cost-zero entry stored at zero. The original direction four to zero already serves travelers correctly, so no reversal is counted.

The same reasoning applies deeper in the tree because parent and child are defined by distance from zero, not by the order in `connections`.

**Why every counted reversal is necessary.** Consider a cost-one edge between rooted parent `a` and child `b`. Removing it separates the entire subtree at `b` from zero. That edge is the subtree's only connection to the rest of the tree, and its original direction points into the subtree. No city in that subtree can cross it toward zero unless it is reversed.

**Why reversing all counted edges is sufficient.** Every cost-zero edge already points child-to-parent, and reversing every cost-one edge makes it do the same. From any city, repeatedly following its parent edge then reduces its distance to root by one and eventually reaches zero. Thus the counted set produces a valid orientation.

Since each counted edge is individually necessary and the whole counted set is sufficient, its size is the minimum possible.

## Complexity detail

The tree has `n - 1` roads. Building `g` inserts two entries per road, taking `O(n)` time and `O(n)` space.

DFS visits every city once and examines each adjacency entry once. Total traversal time is `O(n)`. The generator and arithmetic do constant work per entry.

The adjacency list uses `O(n)` space. Recursive depth is the rooted tree height `h`, which can reach `n` for a chain, so worst-case stack space is `O(n)`. Total space matches the manifest's `O(n)`.

With up to fifty thousand cities, a path-shaped tree can exceed Python's default recursion depth. An iterative stack is operationally safer while preserving the same asymptotic bounds.

## Alternatives and edge cases

- **Iterative DFS:** Store node, parent pairs on an explicit stack and add edge costs while visiting children. It avoids Python recursion-depth failure.
- **Breadth-first search:** A queue can traverse outward from zero with the same labeled adjacency entries and count rule.
- **Visited array:** It is valid but unnecessary for a tree when the parent is passed. It becomes necessary if cycles are allowed.
- **Traverse original edges only:** This can fail to reach children whose roads point toward the current node. Artificial reverse entries are required for undirected exploration.
- **All roads already point to zero:** Every outward traversal uses cost-zero entries, and the answer is zero.
- **All rooted edges point away from zero:** Every road contributes one, so `n - 1` reversals are necessary.
- **Single chain:** Each road's cost is evaluated once according to whether it faces toward its parent.
- **Star centered at zero:** Roads directed zero-to-leaf must reverse; leaf-to-zero roads do not.
- **Input endpoint order:** `[a,b]` is directional, not an unordered pair. The two labeled adjacency entries preserve that fact.
- **Leaf city:** Its DFS returns zero after its incoming edge cost has already been counted by the parent.
- **Unique-path guarantee:** It proves that every outward edge is unavoidable and makes the count minimal.
- **Parent sentinel:** `-1` cannot equal a valid city, so root processes all neighbors.
- **Deep tree:** Prefer iterative traversal in Python if runtime recursion limits are not adjusted.
- **No actual mutation:** The method counts required reversals; it does not need to rewrite the connection list.
