# Longest ZigZag Path in a Binary Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1372 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming, Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/) |

## Problem Description

### Goal

A ZigZag path in a binary tree may begin at any node. Choose an initial move to either the left or right child; after moving left, the next move must go right, and after moving right, the next move must go left. Continue downward while alternating directions.

The path length is its number of traversed edges, which is one less than its number of nodes. Return the maximum ZigZag length available anywhere in the tree. A path containing only one node has length zero.

### Function Contract

**Inputs**

- `root`: the root of a nonempty binary tree containing $N$ nodes and having height $H$.

**Return value**

- The greatest number of edges in any downward path whose directions strictly alternate left and right.

### Examples

**Example 1**

- Input: an alternating five-node chain.
- Output: `4`

**Example 2**

- Input: a three-node chain using two left edges.
- Output: `1`

**Example 3**

- Input: a one-node tree.
- Output: `0`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(H)$

<details>
<summary>Approach</summary>

#### General

**Carry both ways a path can end.** For every visited node, maintain two lengths: the longest alternating path ending at that node whose last edge moved left, and the corresponding length whose last edge moved right.

**Extend only from the opposite direction.** When moving to a left child, its new left-ending length is the parent's right-ending length plus one; its right-ending length resets to zero. Moving to a right child symmetrically extends the parent's left-ending length and resets the other state.

Traverse with an explicit depth-first stack and update a global maximum from both states at every node. Each carried value describes a valid alternating path by construction. Any ZigZag path ending at a child must arrive from its parent in that child's direction and can extend only a path whose prior direction was opposite, so the transition also considers every possible valid path. The maximum is therefore exact.

#### Complexity detail

Each of the $N$ nodes is pushed, popped, and processed once, yielding $O(N)$ time. A depth-first stack retains at most pending siblings along a root-to-leaf route, using $O(H)$ space.

#### Alternatives and edge cases

- **Restart at every node:** Follow both possible initial directions independently from each node. It is correct but can take $O(N^2)$ time on an alternating chain.
- **Recursive postorder DP:** Return left-starting and right-starting lengths from each subtree. This is also linear but may exceed the language recursion limit on a deep legal tree.
- **Straight chain:** Consecutive edges in one direction cannot both belong to a ZigZag, so the maximum is one when at least one edge exists.
- **Single node:** No edge can be traversed, producing length zero.
- **Path starts below root:** Reset states at each child allow every node to serve as a new start.
- **Edge count:** Do not return the number of nodes; a $k$-node path has length $k-1$.
- **Branching tree:** Left and right states are carried separately, so one branch cannot be spliced into another through siblings.

</details>
