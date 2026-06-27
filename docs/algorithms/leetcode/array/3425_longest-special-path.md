# Longest Special Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3425 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Tree, Depth-First Search, Prefix Sum |
| Official Link | [longest-special-path](https://leetcode.com/problems/longest-special-path/) |

## Problem Description & Examples
### Goal
Given a tree where each node has a value and each edge has a weight, find the length of the longest path such that all node values on the path are unique. The length of a path is defined as the sum of the weights of the edges along that path.

### Function Contract
**Inputs**

- `edges`: A list of lists where each element `[u, v, w]` represents an undirected edge between nodes `u` and `v` with weight `w`.
- `values`: A list of integers where `values[i]` is the value associated with node `i`.

**Return value**

- A list of two integers: `[max_length, number_of_paths]`. `max_length` is the length of the longest path with unique node values, and `number_of_paths` is the count of such paths.

### Examples
**Example 1**

- Input: `edges = [[0,1,2],[1,2,3],[1,3,5]], values = [1,2,3,4]`
- Output: `[8, 1]`

**Example 2**

- Input: `edges = [[0,1,1],[1,2,2],[2,3,3]], values = [1,1,2,2]`
- Output: `[3, 1]`

**Example 3**

- Input: `edges = [[0,1,1]], values = [1,1]`
- Output: `[1, 1]`

---

## Underlying Base Algorithm(s)
The problem is solved using Depth-First Search (DFS) on the tree structure. To maintain the "unique node values" constraint, we track the current path's node values using a hash map (or dictionary) that stores the depth (or prefix sum) at which each value was last encountered. As we traverse, we maintain the current prefix sum of edge weights. If a node value is repeated, we identify the valid sub-path by checking the last recorded position of that value.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of nodes. We visit each node and edge exactly once during the DFS traversal.
- **Space Complexity**: `O(N)`, required for the adjacency list, the recursion stack, and the hash map storing node values and their associated prefix sums.
