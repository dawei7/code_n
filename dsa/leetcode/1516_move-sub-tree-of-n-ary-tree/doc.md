# Move Sub-Tree of N-Ary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1516 |
| Difficulty | Hard |
| Topics | Tree, Depth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/) |

## Problem Description
### Goal

An N-ary tree contains unique node values, and two distinct existing nodes are designated as `p` and `q`. Detach the entire subtree rooted at `p` from its current position and make `p` the last direct child of `q`.

If `p` is already a direct child of `q`, leave the tree unchanged. Otherwise, preserve the order of every child list except for the removals and insertions required by the move.

Special care is required when `q` belongs to the subtree rooted at `p`: attaching `p` below `q` without another change would form a cycle and disconnect the original parent side. In that case, first detach `q` from its parent, place `q` where `p` used to be (or make `q` the root when `p` was the root), and then append `p` to `q`. Return the root of the resulting valid tree.

### Function Contract
**Inputs**

Let $n$ be the number of nodes.

- `tree`: The app-local representation of the original tree as $n$ records `[value, child_values]`. Values are unique, every non-root value appears in exactly one child list, and child-list order is significant.
- `p`: The unique value of the subtree root to move.
- `q`: The unique value of the new parent; `p` and `q` are distinct and both occur in `tree`.
- The source contract guarantees $2 \leq n \leq 1000$.

**Return value**

Return the adjusted tree as breadth-first `[value, child_values]` records beginning with its possibly changed root. The order inside each child list must match the adjusted N-ary tree.

### Examples
**Example 1**

- Input: `tree = [[1, [2, 3]], [2, [4, 5]], [3, [6]], [4, [7, 8]], [5, []], [6, []], [7, []], [8, []]], p = 4, q = 1`
- Output: `[[1, [2, 3, 4]], [2, [5]], [3, [6]], [4, [7, 8]], [5, []], [6, []], [7, []], [8, []]]`
- Explanation: Node 4 leaves node 2 and becomes node 1's last child, carrying nodes 7 and 8 with it.

**Example 2**

- Input: `tree = [[1, [2, 3]], [2, [4, 5]], [3, [6]], [4, [7, 8]], [5, []], [6, []], [7, []], [8, []]], p = 7, q = 4`
- Output: the same tree
- Explanation: Node 7 is already a direct child of node 4, so no reordering occurs.

**Example 3**

- Input: `tree = [[1, [2, 3]], [2, [4, 5]], [3, [6]], [4, [7, 8]], [5, []], [6, []], [7, []], [8, []]], p = 1, q = 8`
- Output root: `8`
- Explanation: Because node 8 starts below node 1, node 8 is detached first, becomes the root, and receives node 1 as its last child.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Record every parent before changing the tree**

Traverse all nodes once and map each non-root node to its parent. This also identifies the root as the only value that never appears in a child list. The parent map makes it possible to detach either target in constant time once its child-list position is found, and it provides an upward path from `q` for determining whether `q` lies inside `p`'s subtree.

Check the no-op rule first. If `parent[q]` is not relevant but `parent[p] == q`, the contract requires returning the tree unchanged even when `p` is not currently `q`'s last child.

**Separate the cycle-producing case**

Walk from `q` toward the root through the parent map. If this walk reaches `p`, then `q` is below `p`. Detach `q` from its old parent before moving anything else. Replace `p` by `q` in `p`'s former parent's child list, preserving that position; if `p` had no parent, set `q` as the new root. Finally append `p` to `q`'s child list.

This replacement reconnects the component above `p` to `q`, while detaching `q` first removes the only downward path that would otherwise close a cycle. All nodes remain reachable exactly once.

If the upward walk does not reach `p`, moving `p` cannot put one of its ancestors below itself. Remove `p` from its old parent's children and append it to `q` directly. The subtree below `p` is never dismantled, so all of its internal edges and child orders remain intact.

**Serialize without changing semantics**

After rewiring, perform breadth-first traversal from the resulting root and emit each value with its ordered child-value list. This app-local serialization is deterministic; the native Accepted artifact performs the same pointer rewiring and returns the actual root node.

#### Complexity detail

Building child and parent maps visits every node and edge once. The ancestor walk, list removals or replacement search, and final breadth-first serialization each take at most $O(n)$ time, so the total is $O(n)$.

The copied child lists, parent map, and traversal queue each contain at most $n$ values, giving $O(n)$ auxiliary space. The native pointer-based form likewise needs an $O(n)$ parent map and traversal stack.

#### Alternatives and edge cases

- **Subtree DFS from `p`:** searching downward from `p` can detect whether `q` is inside it, but parent discovery is still required for safe detachment. A single global traversal plus an upward walk keeps all required relationships together.
- **Repeated parent searches:** locating a node's parent by rescanning the whole tree for every ancestor is correct but can require $O(n^2)$ time on a chain.
- **Recursive traversal:** recursion expresses the tree walk concisely, but a legal chain can contain 1000 nodes and approach Python's recursion limit; an explicit stack is safer.
- **`p` already below `q`:** only a direct-child relationship is a no-op. A deeper descendant must still be detached and appended directly to `q`.
- **`q` below `p`:** detach `q` first and replace `p` with it; simply appending `p` to `q` creates a cycle.
- **`p` is the root:** this can occur only when `q` lies below `p`, and `q` becomes the new root.
- **Child order:** removing a child closes its position without disturbing the relative order of siblings, while `p` is always appended at the end of `q`'s children.
- **Direct child not last:** the explicit no-op rule leaves the ordering unchanged rather than moving `p` to the end.

</details>
