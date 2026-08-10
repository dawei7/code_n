## General

**Why parent information is needed**

Each node exposes children but not its parent. Moving `p` requires detaching it from its old parent, and the special ancestor case also requires detaching `q` from its old parent. The stored solution first performs an iterative depth-first traversal to build `parent[node]` for every node.

The root maps to `None`. The stack begins with the root, and every child encountered receives its current node as parent before being pushed. Because the input is a tree, each non-root node is discovered through its unique parent edge.

This map also lets the algorithm decide whether `q` lies inside `p`'s subtree by walking upward from `q`.

**The already-direct-child rule**

`p_parent = parent[p]` identifies the current parent of `p`. If `p_parent is q`, the method returns the original root immediately.

This follows the explicit rule that no change should be made when `p` is already a direct child of `q`. The early return even preserves its current sibling position rather than moving it to the end, because “do not change anything” controls that special case.

Identity comparison is used rather than node values. The inputs `p` and `q` are actual objects from the tree.

**Detecting the dangerous ancestor case**

The algorithm starts at `q` and repeatedly follows `parent[current]` toward the root. If it encounters `p`, then `q` is in `p`'s subtree.

Simply removing `p` from its parent and appending it under descendant `q` would create a cycle: `p` already reaches `q` downward, and the new edge would make `q` reach `p` downward. It could also disconnect the structure from the original root.

The Boolean `q_is_below_p` selects the special rewiring needed to avoid that cycle.

**When q is below p**

First, the code gets `q_parent = parent[q]` and removes `q` from `q_parent.children`. This cuts the old downward path from `p` to `q`, so placing `p` below `q` later cannot form a cycle.

Next, `q` takes `p`'s old connection to the part of the tree above `p`:

- If `p` was the root, there is no parent connection to replace, so `root = q`.
- Otherwise, the code finds `p`'s index in `p_parent.children` and replaces that list entry with `q`.

Replacing in place preserves the old sibling position at `p`'s parent. Finally, `q.children.append(p)` makes `p` the last child of `q`.

The entire old `p` subtree moves below `q` except that `q` and its subtree were detached first. Those nodes remain connected through `q` at the higher position. Every node still appears exactly once.

**When q is not below p**

If `q` is outside `p`'s subtree, moving `p` cannot create a cycle. The code removes `p` from `p_parent.children` and appends it to `q.children`.

This covers both situations where `p` is somewhere below `q` but not a direct child and where the two nodes lie in separate branches. If `p` were the root, every other node would be below it, so this branch could not occur; therefore, `p_parent` is safely non-null here.

Appending rather than inserting ensures `p` becomes the last child.

**Why the result is still one tree**

In the ordinary case, one parent edge into `p` is removed and one new parent edge from `q` is added. Connectivity is preserved, edge count remains $n-1$, and no cycle is introduced because `q` was outside `p`'s subtree.

In the descendant case, the old edge into `q` and old edge into `p` are replaced by the edge into `q` and the new `q`-to-`p` edge. If `p` was root, root status moves to `q`. The prior ancestor path between them was broken before reversal, so the result remains connected and acyclic.

The parent map becomes stale after mutation, but the method performs no later structural queries with it. The final append and return are the last steps.

## Complexity detail

Let $N$ be the number of nodes. Building the parent map visits every node and each tree edge once, taking $O(N)$ time.

Walking from `q` to the root costs $O(N)$ in the worst case. `children.remove` and `children.index` scan child lists linearly; each can cost $O(N)$ for a very wide node. These operations occur only a constant number of times, so total time remains $O(N)$.

The parent dictionary and traversal stack each use $O(N)$ space, matching the manifest. Mutation itself reuses the existing node objects and children lists.

## Alternatives and edge cases

- **Recursive parent discovery:** DFS can find parents and ancestry, but a depth near one thousand can approach Python's recursion limit. The stored explicit stack avoids that risk.
- **Subtree membership DFS from p:** Searching downward for q is valid, but the parent map is still useful for detachment; the upward walk reuses one structure.
- **p already child of q:** The exact rule returns without reordering p to the last position.
- **p is root and q is below it:** q becomes the new root, and p is appended beneath q.
- **q is a direct child of p:** q is detached from p before p is attached under q, reversing their relationship without a cycle.
- **p below q but not direct:** p is detached from its current parent and appended to q.
- **Separate branches:** The ordinary detach-and-append operation applies.
- **Sibling order:** Replacing p with q preserves the old slot above, while appending p makes it q's last child.
- **Unique values:** The algorithm primarily uses object identity; uniqueness belongs to the tree contract and serialization.
- **Mutation:** The existing tree objects are rewired in place rather than cloned.
