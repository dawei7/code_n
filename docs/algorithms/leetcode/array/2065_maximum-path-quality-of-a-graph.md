# Maximum Path Quality of a Graph

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2065 |
| Difficulty | Hard |
| Topics | Array, Backtracking, Graph Theory |
| Official Link | [maximum-path-quality-of-a-graph](https://leetcode.com/problems/maximum-path-quality-of-a-graph/) |

## Problem Description & Examples
### Goal
Starting and ending at node `0`, walk through an undirected weighted graph within `maxTime`. Node values count only the first time each node is visited; maximize collected value.

### Function Contract
**Inputs**

- `values`: value for each node.
- `edges`: undirected weighted edges `[u, v, time]`.
- `maxTime`: time budget.

**Return value**

Return the maximum path quality of any valid route that returns to node `0`.

### Examples
**Example 1**

- Input: `values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49`
- Output: `75`

**Example 2**

- Input: `values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30`
- Output: `25`

**Example 3**

- Input: `values = [1], edges = [], maxTime = 10`
- Output: `1`

---

## Underlying Base Algorithm(s)
Use DFS/backtracking from node `0`, tracking elapsed time and visit counts. Add a node's value only when its count changes from zero to one. Whenever the path returns to node `0`, update the best score. Prune edges that would exceed `maxTime`.

---

## Complexity Analysis
- **Time Complexity**: exponential in feasible path length under the time budget.
- **Space Complexity**: `O(n + e)` for graph storage and recursion state.
