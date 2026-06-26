# All Paths From Source to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 797 |
| Difficulty | Medium |
| Topics | Backtracking, Depth-First Search, Breadth-First Search, Graph Theory |
| Official Link | [all-paths-from-source-to-target](https://leetcode.com/problems/all-paths-from-source-to-target/) |

## Problem Description & Examples
### Goal
Given a directed acyclic graph represented by adjacency lists, return every path from node `0` to node `n - 1`.

### Function Contract
**Inputs**

- `graph`: List[List[int]] where `graph[i]` lists outgoing neighbors of node `i`

**Return value**

List[List[int]] - all source-to-target paths

### Examples
**Example 1**

- Input: `graph = [[1, 2], [3], [3], []]`
- Output: `[[0, 1, 3], [0, 2, 3]]`

**Example 2**

- Input: `graph = [[1], []]`
- Output: `[[0, 1]]`

**Example 3**

- Input: `graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]`
- Output: `[[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]`

---

## Underlying Base Algorithm(s)
DFS path enumeration in a DAG.

---

## Complexity Analysis
- **Time Complexity**: `O(p * n)` where `p` is the number of returned paths
- **Space Complexity**: `O(n)` auxiliary recursion/path space, plus output
