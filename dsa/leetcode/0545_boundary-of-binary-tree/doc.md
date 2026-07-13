# Boundary of Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 545 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/boundary-of-binary-tree/) |

## Problem Description
### Goal
Given a binary tree, its anti-clockwise boundary is assembled from structural regions. Begin with the root, then take the non-leaf left boundary from top to bottom, followed by every leaf from left to right, and finally the non-leaf right boundary from bottom to top.

Return the boundary node values in that order without listing any node twice. When a preferred left or right child is missing, the corresponding boundary continues through the available child. A leaf belongs to the leaf section rather than a side-boundary section, and an empty tree returns an empty list while a one-node tree returns the root once.

### Function Contract
**Inputs**

- `root`: the root of a binary tree

**Return value**

- A list of boundary node values in anti-clockwise order

### Examples
**Example 1**

- Input tree: `[1, null, 2, 3, 4]`
- Output: `[1, 3, 4, 2]`

**Example 2**

- Input tree: `[1, 2, 3, 4, 5, 6, null, null, null, 7, 8, 9, 10]`
- Output: `[1, 2, 4, 7, 8, 9, 10, 6, 3]`

**Example 3**

- Input tree: `[1]`
- Output: `[1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(h)$

<details>
<summary>Approach</summary>

#### General

**Separate the boundary into disjoint roles**

Add the root first. Both side-boundary walks deliberately omit leaves, while the leaf traversal deliberately omits the root. This division prevents duplicate nodes where the left or right edge reaches a leaf.

**Follow the outer child on each side**

For the left boundary, prefer a left child and fall back to the right child only when necessary. Append each non-leaf before descending. For the right boundary, symmetrically prefer the right child, collect non-leaves temporarily, and append them in reverse so their order runs upward.

**Visit leaves from left to right**

Use depth-first traversal that processes the left child before the right child. Whenever the current node has no children, append its value. An explicit stack pushes the right child first so the left child is popped first.

**Why the three pieces are exactly the anti-clockwise perimeter**

The left walk follows the unique outermost root-to-leftmost-leaf route, and the mirrored right walk follows the outermost route to the rightmost leaf. Every leaf between those extremes is encountered once in left-to-right order by depth-first traversal. Excluding leaves from both side walks and excluding the root from leaf handling makes the pieces disjoint, while their concatenation covers every boundary node in the required direction.

#### Complexity detail

The leaf traversal visits all `n` nodes once. A boundary node may also be touched by one side walk, which is only constant additional work, so total time is $O(n)$. The depth-first stack and temporary right-boundary list each contain at most $O(h)$ nodes, giving $O(h)$ auxiliary space beyond the returned list.

#### Alternatives and edge cases

- **Recursive depth-first traversal with boundary flags:** can emit the same order in $O(n)$ time, but the state transitions are easier to mishandle and a deep tree may exceed recursion limits.
- **Collect every root-to-leaf path:** can reconstruct both sides and all leaves, but copying long shared prefixes costs $O(nh)$ time and space, which becomes quadratic on comb-shaped trees.
- **Single node:** appears only as the root, not again as a leaf.
- **One-sided tree:** the missing preferred child must fall back to the existing child on the same outer boundary.
- **Boundary leaves:** are added by the leaf traversal and excluded from the side lists.
- **Duplicate values:** distinct boundary nodes with equal values must all remain in the result; deduplication by value is incorrect.
- **Right-side order:** must be reversed after collection to make the overall traversal anti-clockwise.

</details>
