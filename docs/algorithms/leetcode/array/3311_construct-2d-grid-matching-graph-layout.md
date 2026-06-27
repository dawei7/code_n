# Construct 2D Grid Matching Graph Layout

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3311 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Graph Theory, Matrix |
| Official Link | [construct-2d-grid-matching-graph-layout](https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/) |

## Problem Description & Examples
### Goal
Given a set of edges representing a graph that is guaranteed to be a grid, reconstruct the original 2D grid layout. The grid dimensions are unknown, but the connectivity of the nodes must match the provided edge list.

### Function Contract
**Inputs**

- `n`: An integer representing the number of nodes (labeled 0 to n-1).
- `edges`: A list of lists, where each inner list `[u, v]` represents an undirected edge between nodes `u` and `v`.

**Return value**

- A 2D list of integers representing the reconstructed grid layout.

### Examples
**Example 1**

- Input: `n = 4, edges = [[0,1],[0,2],[1,3],[2,3]]`
- Output: `[[0,1],[2,3]]`

**Example 2**

- Input: `n = 5, edges = [[0,1],[1,3],[2,3],[3,4]]`
- Output: `[[0],[1],[3],[2],[4]]`

**Example 3**

- Input: `n = 9, edges = [[0,1],[0,4],[1,2],[1,5],[2,6],[3,4],[3,7],[4,5],[4,8],[5,9]...]` (simplified)
- Output: `[[0,1,2],[3,4,5],[6,7,8]]`

## Underlying Base Algorithm(s)
The solution relies on graph degree analysis to identify corner, edge, and interior nodes. By identifying a corner node (degree 2) and its neighbors, we can determine the grid's width. Once the width is established, we perform a Breadth-First Search (BFS) or a row-by-row traversal to fill the grid, ensuring that each node's neighbors in the grid match the adjacency list provided.

## Complexity Analysis
- **Time Complexity**: O(n), where n is the number of nodes. We iterate through the edges to build an adjacency list and then traverse the grid once.
- **Space Complexity**: O(n), required to store the adjacency list and the resulting 2D grid.
