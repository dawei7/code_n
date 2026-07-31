# Path Existence Queries in a Graph II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3534 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Dynamic Programming, Greedy, Bit Manipulation, Graph Theory, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/) |

## Problem Description

### Goal

There are `n` nodes labeled from `0` through `n - 1`, and node `i` carries the value `nums[i]`. The graph is implicit: two distinct nodes share an undirected, unweighted edge exactly when

$$
\lvert\texttt{nums[i]}-\texttt{nums[j]}\rvert \le \texttt{maxDiff}.
$$

For every pair `[u, v]` in `queries`, find the minimum number of edges in a path from `u` to `v`. Return `-1` when no such path exists. The distance from a node to itself is $0$.

Return all query results in their original order.

### Function Contract

**Inputs**

- `n`: The number of nodes, equal to the length of `nums`, where $1 \le n \le 10^5$.
- `nums`: The node values, each between $0$ and $10^5$; the input order is arbitrary.
- `maxDiff`: The greatest value difference allowed across one edge, where $0 \le \texttt{maxDiff} \le 10^5$.
- `queries`: Source-target pairs `[u, v]`, with both endpoints in $[0,n-1]$.

Let $Q = \lvert\texttt{queries}\rvert$, where $1 \le Q \le 10^5$.

**Return value**

- A list of minimum unweighted path lengths, using `-1` for disconnected endpoint pairs.

### Examples

**Example 1**

- Input: `n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]`
- Output: `[1,1]`
- Explanation: Values $1$ and $4$ differ by $3$, while values $3$ and $2$ differ by $1$, so both queried pairs share a direct edge.

**Example 2**

- Input: `n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]`
- Output: `[1,2,-1,1]`
- Explanation: The values $5,3,1$ form a three-node chain, while $9,10$ form a separate component.

**Example 3**

- Input: `n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]`
- Output: `[0,-1,-1]`
- Explanation: No two different values are close enough for an edge, but the self-query still has distance zero.
