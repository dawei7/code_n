# Checking Existence of Edge Length Limited Paths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1697 |
| Difficulty | Hard |
| Topics | Array, Two Pointers, Union-Find, Graph Theory, Sorting |
| Official Link | [checking-existence-of-edge-length-limited-paths](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/) |

## Problem Description & Examples
### Goal
For each query `(p, q, limit)`, determine whether there is a path from `p` to `q` using only edges whose weights are strictly less than `limit`.

### Function Contract
**Inputs**

- `n`: the number of nodes labeled from `0` to `n - 1`.
- `edgeList`: weighted undirected edges `[u, v, distance]`.
- `queries`: path queries `[p, q, limit]`.

**Return value**

Return a boolean answer for each query in its original order.

### Examples
**Example 1**

- Input: `n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]`
- Output: `[false,true]`

**Example 2**

- Input: `n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]`
- Output: `[true,false]`

**Example 3**

- Input: `n = 4, edgeList = [[0,1,3],[1,2,5],[2,3,7]], queries = [[0,3,8],[0,2,5],[1,3,8]]`
- Output: `[true,false,true]`

---

## Underlying Base Algorithm(s)
Sort edges by distance and queries by limit. Sweep queries from smallest limit to largest, unioning every edge with distance below the current query limit. After those unions, the query answer is whether its two endpoints have the same disjoint-set representative.

---

## Complexity Analysis
- **Time Complexity**: `O((E + Q) log(E + Q))`
- **Space Complexity**: `O(n + Q)`
