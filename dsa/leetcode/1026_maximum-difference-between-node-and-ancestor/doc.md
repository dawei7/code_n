# Maximum Difference Between Node and Ancestor

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1026 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Tree, Depth-First Search, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/) |

## Problem Description

### Goal

Given the `root` of a binary tree, consider two different nodes `a` and `b` such that `a` is an ancestor of `b`. Their difference is $lvert a.	ext{val} - b.	ext{val} vert$.

A node is an ancestor of each of its children and of every node that is an ancestor-descendant continuation through one of those children. Return the maximum difference over all valid ancestor-descendant pairs in the tree.

### Function Contract

**Inputs**

- `root`: the root of a binary tree with $N$ nodes, represented in cases by a level-order array using `null` for absent children.
- The tree satisfies $2 \le N \le 5000$, and every node value is between $0$ and $10^5$, inclusive.
- Let $H$ denote the tree height.

**Return value**

- The largest absolute value difference between two different nodes where one is an ancestor of the other.

### Examples

**Example 1**

- Input: `root = [8,3,10,1,6,null,14,null,null,4,7,13]`
- Output: `7`
- Explanation: Node `8` is an ancestor of node `1`, and their difference is $lvert 8-1vert=7$, the largest valid value.

**Example 2**

- Input: `root = [1,null,2,null,0,3]`
- Output: `3`
- Explanation: The root `1` is an ancestor of node `3`, giving $lvert 1-3vert=2$, while node `0` is a descendant of `1` and an ancestor of `3`; the pair `0` and `3` gives the maximum $3$.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(H)$

<details>
<summary>Approach</summary>

#### General

**Summarize the ancestor path:** For a node, every possible difference with an ancestor is bounded by the minimum and maximum values already seen from the root to its parent. No other ancestor value can be farther from the node's value than one of those two extremes.

**Carry extrema into each child:** Store triples of `(node, path_min, path_max)` on a depth-first stack. At a visited node, update the answer with `node.val - path_min` and `path_max - node.val`, then form `next_min` and `next_max` including the current value before pushing its children.

Each stack entry receives exactly the extrema of that node's ancestor path. Therefore every candidate difference considered is between a valid ancestor and descendant. Conversely, for every node, its farthest-valued ancestor is represented by one of the carried extrema, so the traversal cannot miss the global maximum.

**Keep traversal iterative:** A valid tree may contain 5000 nodes in one chain. An explicit stack retains the same depth-first state without depending on Python's recursion limit.

#### Complexity detail

Every one of the $N$ nodes is pushed and processed once, so the traversal takes $O(N)$ time. The stack contains at most one path plus deferred siblings, bounded by the tree height $H$, for $O(H)$ auxiliary space.

#### Alternatives and edge cases

- **Recursive depth-first search:** Pass the same path minimum and maximum through recursive calls for identical asymptotic bounds, but a deeply skewed tree can exceed the language's recursion limit.
- **Rescan each descendant subtree:** Treat every node as an ancestor and search below it for extreme values. This repeats work and takes $O(NH)$ time, which is $O(N^2)$ on a chain.
- **Equal values:** If all node values are identical, every valid difference is zero.
- **Extreme values:** Values `0` and `100000` may produce the maximum possible answer `100000`.
- **Distinct-node rule:** A node is not paired with itself; initializing the path extrema at the root and evaluating descendants respects that requirement.

</details>
