# Maximum Star Sum of a Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2497 |
| Difficulty | Medium |
| Topics | Array, Greedy, Graph Theory, Sorting, Heap (Priority Queue) |
| Official Link | [maximum-star-sum-of-a-graph](https://leetcode.com/problems/maximum-star-sum-of-a-graph/) |

## Problem Description & Examples
### Goal
Given an undirected graph represented by node values and a list of edges, identify the "star graph" (a center node and a subset of its adjacent edges) that yields the maximum possible sum of node values. You are constrained to select at most `k` edges connected to the chosen center node.

### Function Contract
**Inputs**

- `vals`: A list of integers representing the value of each node.
- `edges`: A list of pairs `[u, v]` representing undirected edges between nodes.
- `k`: An integer representing the maximum number of edges allowed in the star.

**Return value**

- An integer representing the maximum star sum possible.

### Examples
**Example 1**

- Input: `vals = [1, 2, 3, 4, 10, -10, -20]`, `edges = [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [3, 6]]`, `k = 2`
- Output: `16`

**Example 2**

- Input: `vals = [-5]`, `edges = []`, `k = 0`
- Output: `-5`

**Example 3**

- Input: `vals = [1, 2, 3, 4, 5, 6]`, `edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]`, `k = 2`
- Output: `11`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach**. For each node, we collect the values of all its neighbors. To maximize the sum, we sort the neighbor values in descending order and select up to `k` positive values. If a neighbor's value is negative, it is only included if we have not yet reached the `k` limit and the inclusion is necessary (though optimally, we only pick positive values unless forced, but here we can pick *at most* `k`, so we simply pick the top `k` positive values).

---

## Complexity Analysis
- **Time Complexity**: `O(E log E + V)`, where `E` is the number of edges and `V` is the number of nodes. We iterate over all edges to build adjacency lists, and for each node, we sort its neighbors.
- **Space Complexity**: `O(V + E)` to store the adjacency list representation of the graph.
