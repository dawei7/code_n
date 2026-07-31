# Path Existence Queries in a Graph I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3532 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Union-Find, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-i/) |

## Problem Description

### Goal

There are `n` graph nodes labeled from `0` through `n - 1`. The non-decreasing array `nums` assigns value `nums[i]` to node `i`. Rather than receiving an explicit edge list, the graph contains an undirected edge between every pair of nodes `i` and `j` whose values differ by at most `maxDiff`:

$$
\lvert\texttt{nums[i]}-\texttt{nums[j]}\rvert \le \texttt{maxDiff}.
$$

For each pair `[u, v]` in `queries`, determine whether some path connects nodes `u` and `v`. A node always has a trivial path to itself. Return the answers in query order.

### Function Contract

**Inputs**

- `n`: The number of nodes, equal to the length of `nums`, where $1 \le n \le 10^5$.
- `nums`: Node values in non-decreasing order, each between $0$ and $10^5$.
- `maxDiff`: The largest allowed value difference for one edge, where $0 \le \texttt{maxDiff} \le 10^5$.
- `queries`: Node pairs `[u, v]`, with both endpoints in $[0,n-1]$.

Let $Q = \lvert\texttt{queries}\rvert$, where $1 \le Q \le 10^5$.

**Return value**

- A boolean list whose $i$-th value states whether the endpoints of `queries[i]` lie in the same connected component.

### Examples

**Example 1**

- Input: `n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]`
- Output: `[true,false]`
- Explanation: Node `0` reaches itself, but the value gap between the two different nodes is $2$, which exceeds `maxDiff`.

**Example 2**

- Input: `n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]`
- Output: `[false,false,true,true]`
- Explanation: The gap from `2` to `5` separates node `0`. Nodes `1`, `2`, and `3` remain connected through consecutive gaps of $1$ and $2$.
