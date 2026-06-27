# Longest Special Path II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3486 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Tree, Depth-First Search, Prefix Sum |
| Official Link | [longest-special-path-ii](https://leetcode.com/problems/longest-special-path-ii/) |

## Problem Description & Examples
### Goal
Given a tree where each node has a value and each edge has a weight, identify the longest path such that no two nodes on the path share the same value. The length of a path is defined as the sum of the weights of the edges along that path.

### Function Contract
**Inputs**

- `edges`: A list of lists where each element `[u, v, w]` represents an undirected edge between nodes `u` and `v` with weight `w`.
- `values`: A list of integers where `values[i]` is the value associated with node `i`.

**Return value**

- A list of two integers: `[max_length, count]`, where `max_length` is the maximum path length found, and `count` is the number of paths that achieve this maximum length.

### Examples
**Example 1**

- Input: `edges = [[0,1,2],[1,2,3]], values = [1,2,3]`
- Output: `[5, 1]`

**Example 2**

- Input: `edges = [[0,1,1],[0,2,2],[1,3,3],[1,4,4]], values = [1,2,1,3,4]`
- Output: `[7, 1]`

**Example 3**

- Input: `edges = [[0,1,1],[1,2,2],[2,3,3]], values = [1,1,1,1]`
- Output: `[1, 1]`

---

## Underlying Base Algorithm(s)
The problem is solved using Depth-First Search (DFS) on the tree structure. To maintain the "special" property (no duplicate values), we track the current path's node values using a hash map (or frequency array) and the prefix sum of edge weights from the root. As we traverse, we maintain the starting point of the current valid path by tracking the depth of the most recent occurrence of each value.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of nodes. We visit each node and edge exactly once during the DFS traversal.
- **Space Complexity**: `O(N)`, required for the adjacency list, the recursion stack, and the hash map storing value positions.
