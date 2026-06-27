# Minimum Cost Walk in Weighted Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3108 |
| Difficulty | Hard |
| Topics | Array, Bit Manipulation, Union-Find, Graph Theory |
| Official Link | [minimum-cost-walk-in-weighted-graph](https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/) |

## Problem Description & Examples
### Goal
Given an undirected weighted graph, determine the minimum cost to travel between specified pairs of nodes. The cost of a walk is defined as the bitwise AND of all edge weights traversed. Since we can traverse edges multiple times, the cost effectively becomes the bitwise AND of all edges within the connected component containing the start and end nodes.

### Function Contract
**Inputs**

- `n` (int): The number of nodes in the graph (labeled 0 to n-1).
- `edges` (List[List[int]]): A list of edges where each edge is `[u, v, w]`, representing an undirected edge between `u` and `v` with weight `w`.
- `query` (List[List[int]]): A list of queries where each query is `[start, end]`.

**Return value**

- `List[int]`: A list containing the minimum cost for each query. If a path does not exist, return -1.

### Examples
**Example 1**

- Input: `n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]`
- Output: `[1, -1]`

**Example 2**

- Input: `n = 3, edges = [[0,2,7],[0,1,15],[1,2,6]], query = [[1,2]]`
- Output: `[0]`

**Example 3**

- Input: `n = 4, edges = [[0,1,3],[1,2,10],[2,3,1]], query = [[0,3]]`
- Output: `[0]`

---

## Underlying Base Algorithm(s)
The problem relies on **Disjoint Set Union (DSU)** to group nodes into connected components. Because we can traverse edges multiple times, the bitwise AND of any path within a component is equivalent to the bitwise AND of all edges in that component. We maintain an array to store the cumulative bitwise AND of all edges connected to each component's root.

---

## Complexity Analysis
- **Time Complexity**: O(E * α(N) + Q * α(N)), where E is the number of edges, Q is the number of queries, N is the number of nodes, and α is the inverse Ackermann function.
- **Space Complexity**: O(N), used to store the DSU parent array and the bitwise AND values for each component.
