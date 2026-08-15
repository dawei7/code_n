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

- `root`: The root `Node` of the original N-ary tree. Node values are unique, and child-list order is significant.
- `p`: The existing `Node` whose subtree must move.
- `q`: The distinct existing `Node` that must become `p`'s parent.
- The source contract guarantees $2 \leq n \leq 1000$.

JSON cases encode `root` as breadth-first `[value, child_values]` records and identify `p` and `q` by their unique values. The runner resolves all three arguments to nodes in the same object graph before calling `solve(root, p, q)`.

**Return value**

Return the root `Node` of the adjusted tree. The runner serializes it as breadth-first `[value, child_values]` records for display and validation.

### Examples

#### Example 1

- **Input:** `root = [[1, [2, 3]], [2, [4, 5]], [3, [6]], [4, [7, 8]], [5, []], [6, []], [7, []], [8, []]], p = 4, q = 1`
- **Output:** `[[1, [2, 3, 4]], [2, [5]], [3, [6]], [4, [7, 8]], [5, []], [6, []], [7, []], [8, []]]`
- **Explanation:** Node 4 leaves node 2 and becomes node 1's last child, carrying nodes 7 and 8 with it.

#### Example 2

- **Input:** `root = [[1, [2, 3]], [2, [4, 5]], [3, [6]], [4, [7, 8]], [5, []], [6, []], [7, []], [8, []]], p = 7, q = 4`
- **Output:** the same tree
- **Explanation:** Node 7 is already a direct child of node 4, so no reordering occurs.

#### Example 3

- **Input:** `tree = [[1, [2, 3]], [2, [4, 5]], [3, [6]], [4, [7, 8]], [5, []], [6, []], [7, []], [8, []]], p = 1, q = 8`
- Output root: `8`
- **Explanation:** Because node 8 starts below node 1, node 8 is detached first, becomes the root, and receives node 1 as its last child.
