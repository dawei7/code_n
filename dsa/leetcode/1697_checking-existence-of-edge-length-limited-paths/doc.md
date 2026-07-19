# Checking Existence of Edge Length Limited Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1697 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Union-Find, Graph Theory, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/) |

## Problem Description
### Goal

An undirected weighted graph has $n$ vertices labeled from 0 through $n-1$. Each entry `edgeList[i] = [u_i, v_i, distance_i]` connects its two different endpoints with the given distance. Multiple edges may connect the same pair of vertices.

For every query `[p_j, q_j, limit_j]`, decide whether some path connects `p_j` to `q_j` using only edges whose individual distances are strictly less than `limit_j`. The path may contain any number of edges, but one edge equal to the limit invalidates that candidate path. Return the boolean answers in the same order as the input queries.

### Function Contract
**Inputs**

- `n`: the number of graph vertices, with $2 \le n \le 10^5$
- `edgeList`: $E$ undirected triples `[u, v, distance]`, where $1 \le E \le 10^5$
- `queries`: $Q$ triples `[p, q, limit]`, where $1 \le Q \le 10^5$

Endpoints are valid vertex labels, each edge and query uses two different vertices, and every distance and limit lies between 1 and $10^9$.

**Return value**

A length-$Q$ boolean list whose entry at each index answers the corresponding input query.

### Examples
**Example 1**

- Input: `n = 3, edgeList = [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], queries = [[0, 1, 2], [0, 2, 5]]`
- Output: `[false, true]`

The weight-2 edge is not below the first limit. Under limit 5, weights 2 and 4 connect all three vertices.

**Example 2**

- Input: `n = 5, edgeList = [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], queries = [[0, 4, 14], [1, 4, 13]]`
- Output: `[true, false]`

**Example 3**

- Input: `n = 4, edgeList = [[0, 1, 3], [1, 2, 5], [2, 3, 7]], queries = [[0, 3, 8], [0, 2, 5], [1, 3, 8]]`
- Output: `[true, false, true]`
