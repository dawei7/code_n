## General

**A tree node normally cannot move toward its parent**

Starting from the target, nodes at distance `k` may lie below it, above it, or in a different branch reached through an ancestor. Ordinary `left` and `right` pointers permit only downward movement, so they cannot explore all three directions.

The solution first records a parent pointer for every node. The binary tree can then be treated as an undirected graph where each node has up to three neighbors:

- its left child;
- its right child;
- its parent.

After this conversion, a depth-limited graph traversal from `target` finds exactly the nodes at distance `k`.

**Build parent pointers**

The first DFS receives current node `root` and its parent `fa`.

For every non-null node, it stores:

`g[root] = fa`.

It then recurses into both children while passing the current node as their parent.

The original tree root receives parent `None`. Every other node is reached once through its unique tree parent, so the dictionary obtains one correct entry per node.

The dictionary uses node objects as keys. The exact function signature also receives `target` as the target node object, so there is no need to search by value. Unique values are useful for output clarity but are not needed for dictionary identity.

**Second DFS state**

`dfs2(root, fa, k)` means:

> Explore from this node, without immediately returning to `fa`, and collect nodes exactly `k` edges away from the original target along this path.

Here, `fa` is the node visited immediately before `root` in the undirected traversal. It prevents walking back over the same edge and cycling forever.

The local parameter `k` is remaining distance, not the original fixed value.

**Distance-zero base case**

When `k == 0`, current node is exactly the desired distance from the target. The code appends `root.val` and returns immediately.

Returning matters: descendants would be farther than requested and must not be explored.

If `root is None`, that direction contains no node and returns without output.

**Explore all three directions**

For positive remaining distance, the traversal considers:

`(root.left, root.right, g[root])`.

Any neighbor equal to `fa` is skipped. Every other neighbor receives a recursive call with remaining distance `k-1`.

In a tree, excluding the edge just used is sufficient. There is exactly one simple path between any two nodes, so no different cycle can return to an already visited node.

**Trace the main example**

From target node 5 with `k=2`:

- downward through child 2 reaches children 7 and 4 after two edges;
- upward through parent 3 reaches sibling branch root 1 after two edges;
- child 6 is only one edge away and is not collected.

The output contains `7,4,1` in traversal order, but any order is accepted.

**Why nodes are not duplicated**

Every tree node has one unique simple path from the target. The traversal follows that path once. Parent exclusion prevents the only possible immediate reversal, so a node cannot be reached through a second route.

No visited set is required specifically because the underlying structure is a tree rather than a general graph.

**Why the result is exact**

Parent mapping adds precisely the missing reverse direction without adding edges that were not in the tree. Therefore, paths in the resulting neighbor relation correspond exactly to tree paths.

The second DFS decreases remaining distance by one per traversed edge. A value is appended if and only if exactly `k` edges were taken. Unique paths guarantee every qualifying node is reached once, proving completeness and absence of false results.

## Complexity detail

Let `n` be the number of tree nodes.

The parent-building DFS visits every node once, taking `O(n)` time. The second traversal visits at most every node once, also `O(n)`. Total time is `O(n)`.

The parent dictionary stores `n` entries. Recursive call stacks can reach tree height `h`, at most `n` for a skewed tree. The answer may also contain `O(n)` values. Total auxiliary/output space is `O(n)`.

The second traversal can terminate much earlier when `k` is small, but the worst-case bound remains linear.

## Alternatives and edge cases

- **Build a full undirected adjacency list:** It works but stores both child and parent edges explicitly. A parent map reuses existing child pointers.

- **BFS from the target:** With parent pointers and a visited set, level `k` gives the result. It is equally linear and may make distance levels more explicit.

- **Recursive distance propagation without parent map:** One can return target distances while unwinding from the root and explore opposite subtrees. It avoids a dictionary but has more intricate cases.

- **`k=0`:** The target's own value is the only answer.

- **`k` exceeds every possible distance:** Traversal reaches null boundaries before zero and returns an empty list.

- **Target is the root:** Its parent neighbor is `None`; only descendants are explored.

- **Target is a leaf:** Parent edges still allow reaching ancestors and other branches.

- **One-node tree:** It returns the root for `k=0` and empty for positive `k`.

- **Avoiding `fa`:** Without this check, child-to-parent and parent-to-child recursion would loop.

- **Any output order:** DFS order need not be sorted.

- **Input immutability:** The tree's node pointers are not modified; parents live in a separate dictionary.
