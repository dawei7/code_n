# Minimum Number of Vertices to Reach All Nodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1557 |
| Difficulty | Medium |
| Topics | Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/) |

## Problem Description
### Goal

You are given a directed acyclic graph with `n` vertices numbered from `0` through `n - 1`. Each pair `[from, to]` in `edges` is a distinct directed edge from `from` to `to`.

Choose the smallest set of starting vertices such that every graph vertex is reachable from at least one chosen vertex. A starting vertex counts as reachable from itself. The contract guarantees that the minimum set is unique, although its vertices may be returned in any order.

### Function Contract
**Inputs**

- `n`: The number of vertices, with $2 \le n \le 10^5$.
- `edges`: A nonempty list of $M$ distinct directed pairs, where $1 \le M \le \min(10^5, n(n-1)/2)$. Every endpoint lies in $[0,n-1]$, and all edges together form a directed acyclic graph.

**Return value**

Return the unique minimum set of vertices from which all `n` vertices are reachable. The output order is unrestricted.

### Examples
**Example 1**

- Input: `n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]`
- Output: `[0,3]`

**Example 2**

- Input: `n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]`
- Output: `[0,2,3]`

**Example 3**

- Input: `n = 4, edges = [[0,1],[1,2],[2,3]]`
- Output: `[0]`
