# Closest Nodes Queries in a Binary Search Tree

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2476 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/) |

## Problem Description

### Goal

Given the root of a binary search tree and an array of positive query values, answer each query with the closest tree value on either side. Tree values are unique under the binary search tree ordering.

For a query `x`, find the greatest value in the tree that is at most `x` and the smallest value that is at least `x`. Use `-1` for either side when no qualifying tree value exists. Return the two values for every query in the original query order.

### Function Contract

**Inputs**

- `root`: The root of a binary search tree containing between $2$ and $2 \cdot 10^5$ nodes, with node values from $1$ through $10^6$.
- `queries`: An array of $q$ positive integers, where $1 \le q \le 10^5$ and every query is at most $10^6$.

**Return value**

Return a length-`q` array. For each query `x`, its row is `[lower, upper]`, where `lower` is the greatest tree value satisfying $\textit{lower} \le x$ and `upper` is the smallest tree value satisfying $\textit{upper} \ge x$; use `-1` when a side is absent.

### Examples

#### Example 1

- **Input:** `root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]`
- **Output:** `[[2,2],[4,6],[15,-1]]`
- **Explanation:** An exact match supplies both bounds for `2`; `5` lies between `4` and `6`; `16` exceeds the maximum tree value.

#### Example 2

- **Input:** `root = [4,null,9], queries = [3]`
- **Output:** `[[-1,4]]`
- **Explanation:** No tree value is at most `3`, while `4` is the least value above it.

#### Example 3

- **Input:** `root = [2,1,3], queries = [1,4]`
- **Output:** `[[1,1],[3,-1]]`
- **Explanation:** The first query is exact and the second exceeds the tree maximum.
