# Longest Univalue Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 687 |
| Difficulty | Medium |
| Topics | Tree, Depth-First Search, Binary Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-univalue-path/) |

## Problem Description
### Goal
Given the root of a binary tree, find the longest path in which every node has the same value. A path follows parent-child edges and may start and end at any nodes; it may pass through their common ancestor and does not need to include the tree's root.

Return the path's length measured as the number of edges between its endpoints, not the number of nodes. The two sides of a path may extend through different children of one node only when all connected values remain equal. An empty tree has length `0`.

### Function Contract
**Inputs**

- `root`: the root of a binary tree, or `null`

**Return value**

- The maximum edge count of a same-valued path

### Examples
**Example 1**

- Input: `root = [5,4,5,1,1,null,5]`
- Output: `2`

**Example 2**

- Input: `root = [1,4,5,4,4,null,5]`
- Output: `2`

**Example 3**

- Input: `root = [1]`
- Output: `0`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(H)$

<details>
<summary>Approach</summary>

#### General

**Return one extendable arm from each subtree**

A parent can extend only a path that begins at its child and continues downward through nodes equal to that child. Let a postorder call return the longest such downward path measured in edges from its node. Child results are available before the parent decides whether their values match.

**Build the two arms through the current node**

If the left child has the current node's value, the left arm is the child's returned arm plus their connecting edge; otherwise it is zero. Compute the right arm the same way. A same-valued path whose highest node is the current node can join both arms, giving `left_arm + right_arm` edges.

**Separate the global path from the returned arm**

Update a global maximum with the joined two-arm path. Return only `max(left_arm, right_arm)`, because a path passed to the parent must remain a single downward chain and cannot branch in both directions. Every path has a unique highest node where its two sides meet, so the postorder update considers every possible longest path exactly where it can be formed.

#### Complexity detail

Postorder processing visits each of the `N` nodes once and performs constant work there, for $O(N)$ time. Recursion uses one frame per level, or $O(H)$ space for tree height `H`; this is logarithmic for a balanced tree and linear for a skewed tree.

#### Alternatives and edge cases

- **Iterative postorder:** store node states explicitly and compute the same downward arms; it remains $O(N)$ time but can use $O(N)$ auxiliary maps.
- **Recompute matching depth from every node:** independently explores descendant arms for each possible highest node and can take $O(N^2)$ time.
- **Build an undirected graph of equal-value edges:** then find component diameters, but this discards useful tree structure and adds $O(N)$ storage.
- The result counts edges, so a single-node path has length zero.
- A node may join matching arms from both children even when neither arm is globally longest by itself.
- An empty tree has no edges and returns zero.

</details>
