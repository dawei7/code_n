# Minimum Weighted Subgraph With the Required Paths II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3553 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Tree, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/) |

## Problem Description

### Goal

You are given an undirected weighted tree whose $n$ nodes are numbered from `0` through `n - 1`. Every entry `edges[i] = [u_i,v_i,w_i]` describes an edge of positive weight $w_i$ between $u_i$ and $v_i$.

Each query is `[src1,src2,dest]`. Choose a connected subtree of the original tree that contains paths from both source nodes to the destination. For every query, report the minimum possible sum of the selected edge weights.

Because the input is a tree, each pair of nodes has one unique path. The minimum connected subtree is therefore precisely the union of the paths connecting the three query nodes.

### Function Contract

**Inputs**

- `edges`: The $n-1$ weighted edges of a valid undirected tree, with each entry formatted as `[u,v,w]`.
- `queries`: A nonempty array of triples `[src1,src2,dest]`; the three nodes within each query are pairwise distinct.

The constraints are $3 \le n \le 10^5$, $1 \le w \le 10^4$, and $1 \le \lvert\texttt{queries}\rvert \le 10^5$.

**Return value**

Return an integer array in query order. Each value is the total weight of the minimum subtree connecting that query's two sources and destination.

### Examples

**Example 1**

- Input: `edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]], queries = [[2,3,4],[0,2,5]]`
- Output: `[12,11]`
- Explanation: The first subtree uses the three edges incident to node `1`, with total $3+5+4=12$. The second is the path from `0` through `1` and `2` to `5`, with total $2+3+6=11$.

**Example 2**

- Input: `edges = [[1,0,8],[0,2,7]], queries = [[0,1,2]]`
- Output: `[15]`
- Explanation: Both tree edges are required, so their weights sum to $8+7=15$.

---
