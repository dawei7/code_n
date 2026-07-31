# Maximum Profit from Valid Topological Order in DAG

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3530 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Graph Theory, Topological Sort, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/) |

## Problem Description

### Goal

You are given a directed acyclic graph with `n` nodes labeled from `0` through `n - 1`. Every pair `[u, v]` in `edges` is a directed edge requiring node `u` to appear before node `v`.

Choose a valid topological ordering containing every node exactly once. Positions are numbered from $1$ to $n$. If node `x` is placed at position $i$, it contributes $i \cdot \texttt{score[x]}$ to the profit.

Return the maximum total profit attainable by any topological ordering that respects every edge.

### Function Contract

**Inputs**

- `n`: The number of nodes, where $1 \le n \le 22$.
- `edges`: The directed edges `[u, v]`; the graph is a DAG and contains no duplicate edges.
- `score`: The positive node scores, where `score[i]` belongs to node `i`.

Every endpoint is in $[0,n-1]$, and `score` has length `n`.

**Return value**

- The largest possible sum of position-weighted node scores over all valid topological orders.

### Examples

**Example 1**

- Input: `n = 2, edges = [[0, 1]], score = [2, 3]`
- Output: `8`
- Explanation: The edge forces the order `[0, 1]`, whose profit is $1 \cdot 2 + 2 \cdot 3 = 8$.

**Example 2**

- Input: `n = 3, edges = [[0, 1], [0, 2]], score = [1, 6, 3]`
- Output: `25`
- Explanation: The order `[0, 2, 1]` is valid and earns $1 \cdot 1 + 2 \cdot 3 + 3 \cdot 6 = 25$.
