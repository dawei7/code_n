# Subtree Inversion Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3544 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/subtree-inversion-sum/) |

## Problem Description

### Goal

An undirected tree is rooted at node `0`. Node `i` initially holds `nums[i]`. An inversion operation chooses a node and multiplies the value of every node in its rooted subtree by $-1$.

You may choose any subset of nodes to invert, subject to a spacing rule along ancestor chains. Whenever two chosen nodes have an ancestor-descendant relationship, their tree distance must be at least `k`. Chosen nodes in different branches are not constrained by their distance because neither is an ancestor of the other.

After applying all chosen subtree inversions, return the greatest possible sum of all node values. Nested inversions compose: a node's final sign changes once for every chosen ancestor, including itself.

### Function Contract

**Inputs**

- `edges`: The `n - 1` undirected edges of a valid tree.
- `nums`: The initial value at every node; its length defines $n$.
- `k`: The minimum distance permitted between two inverted nodes on the same ancestor chain.

The constraints are $2 \le n \le 5 \cdot 10^4$, $-5 \cdot 10^4 \le \texttt{nums[i]} \le 5 \cdot 10^4$, and $1 \le k \le 50$.

**Return value**

Return the maximum possible total node value after any valid collection of subtree inversions.

### Examples

#### Example 1

- **Input:** `edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], nums = [4, -8, -6, 3, 7, -2, 5], k = 2`
- **Output:** `27`
- **Explanation:** Inverting nodes `0`, `3`, `4`, and `6` produces `[-4, 8, 6, 3, 7, 2, 5]`.

#### Example 2

- **Input:** `edges = [[0, 1], [1, 2], [2, 3], [3, 4]], nums = [-1, 3, -2, 4, -5], k = 2`
- **Output:** `9`
- **Explanation:** Inverting the leaf at node `4` changes only `-5` to `5`.

#### Example 3

- **Input:** `edges = [[0, 1], [0, 2]], nums = [0, -1, -2], k = 3`
- **Output:** `3`
- **Explanation:** Nodes `1` and `2` are in different branches, so both may be inverted despite their common parent.

---
