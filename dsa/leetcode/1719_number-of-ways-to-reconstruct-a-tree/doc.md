# Number Of Ways To Reconstruct A Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1719 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Tree, Graph Theory, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/) |

## Problem Description

### Goal

You are given distinct pairs `[x, y]` with $x < y$. The node values appearing anywhere in `pairs` are exactly the nodes of an unknown rooted tree, which may have any number of children per node. A pair is present if and only if one of its values is an ancestor of the other in that tree. An ancestor lies on the root-to-node path and excludes the node itself.

Count how many rooted trees have exactly those ancestor-comparability pairs. Two reconstructions differ when at least one node has a different parent. Return `0` when no tree works, `1` when exactly one works, and `2` when more than one reconstruction works; the exact count beyond one is not required.

### Function Contract

**Inputs**

- `pairs`: between $1$ and $10^5$ distinct two-element arrays `[x, y]`, where $1 \le x < y \le 500$.
- Let $V$ be the number of distinct node values appearing in `pairs`.

**Return value**

- Return `0`, `1`, or `2` according to whether the number of matching rooted trees is zero, exactly one, or greater than one.

### Examples

**Example 1**

- Input: `pairs = [[1,2],[2,3]]`
- Output: `1`
- Explanation: Node $2$ must be the root with $1$ and $3$ as its children, so the reconstruction is unique.

**Example 2**

- Input: `pairs = [[1,2],[2,3],[1,3]]`
- Output: `2`
- Explanation: All three nodes are mutually comparable, and more than one parent assignment forms a valid chain.

**Example 3**

- Input: `pairs = [[1,2],[2,3],[2,4],[1,5]]`
- Output: `0`
- Explanation: No node is comparable with every other node, so none can serve as the required root.
