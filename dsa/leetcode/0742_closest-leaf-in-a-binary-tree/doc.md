# Closest Leaf in a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 742 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Breadth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/closest-leaf-in-a-binary-tree/) |

## Problem Description
### Goal
Given a binary tree whose node values are unique and a target value `k` that occurs in the tree, find a leaf having the shortest path from the target node. A leaf has no children, and distance is the number of tree edges along a path that may travel through parents as well as children.

Return the value of a closest leaf. The target itself qualifies when it is a leaf. If several leaves have the same minimum edge distance, returning any one of their values is acceptable.

### Function Contract
**Inputs**

- `root`: the root of a nonempty binary tree whose node values are unique
- `k`: a value guaranteed to occur in the tree

**Return value**

- The value of a closest leaf to node `k`; either value is valid when several leaves tie

### Examples
**Example 1**

- Input: `root = [1,3,2], k = 1`
- Output: `3` (the other child `2` is equally valid)

**Example 2**

- Input: `root = [1], k = 1`
- Output: `1`

**Example 3**

- Input: `root = [1,2,3,4,null,null,null,5,null,6], k = 2`
- Output: `3`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Allow paths to move upward as well as downward**

The closest leaf need not lie inside the target's subtree; it may be reached by moving through ancestors into a sibling branch. Traverse the tree once, recording each node's parent and locating the unique node whose value is `k`. These parent links turn the tree into an undirected graph without rebuilding node objects.

**Search outward from the target by distance layers**

Run breadth-first search from the target. From a node, the possible neighbors are its left child, right child, and parent. A visited set prevents traversing an edge back and forth. Because breadth-first search processes all nodes at distance $d$ before any at distance $d+1$, the first leaf removed from the queue has minimum distance.

**Recognize a leaf independently of search direction**

A leaf is a node with neither child; having a parent neighbor does not change that definition. Check this condition as each queued node is processed. The target itself is returned immediately when it is already a leaf.

**Why the first found leaf is valid**

Adding parent links represents every legal tree path as a graph path and introduces no shortcuts. Breadth-first search discovers nodes in nondecreasing edge distance from `k`, so no unprocessed node can be a closer leaf when the first leaf is found. If several leaves share that layer, returning whichever the queue encounters first satisfies the contract.

#### Complexity detail

The parent-building traversal visits all `n` nodes once, and breadth-first search visits each node at most once, for $O(n)$ time. Parent links, the visited set, and the queue use $O(n)$ space.

#### Alternatives and edge cases

- **Tree dynamic programming:** compute each subtree's nearest leaf and propagate the best outside-subtree option downward; this remains linear but requires more intricate two-pass state.
- **Compare a root path for every leaf:** locate every leaf and repeatedly search root-to-node paths to measure target distance; it is correct but can take $O(n^2)$ time.
- **Search only the target subtree:** this misses a closer leaf reached through an ancestor and sibling branch.
- **Target is a leaf:** its distance to itself is zero, so return `k`.
- **One-node tree:** the root is also the unique closest leaf.
- **Equal-distance leaves:** any tied leaf value is accepted.
- **Skewed tree:** iterative traversals avoid recursion-depth failure on a long chain.
- **Unique values:** the first node with value `k` is the only possible target.

</details>
